#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct{
    char* tytul;
    char* autor;
    double cena;
    unsigned ilosc;

}ksiazka;


typedef struct wezel{
    ksiazka dane;
    struct wezel *nastepny, *poprzedni;

}wezel;

wezel *pierwszy;  //pierwszy->nastepny


unsigned ile_ksiazek_autora(char* autor){
    wezel *temp = pierwszy;
    unsigned licznik = 0;

    while(temp){
        if(strcmp(autor, (temp->dane).autor) == 0){
            licznik++;
        }
        temp = temp->nastepny;
    }
    return licznik;
}


void usun_ksiazki_z_zerowym_stanem(){

    wezel *temp = pierwszy, *usuwamy;

    if(temp==0){  //pusta lista ksiazek
        printf("Lista wezlow jest pusta\n");
    }
    else{
        do{
            if( (temp->dane).ilosc == 0 ){
                free((temp->dane).tytul);

                if(ile_ksiazek_autora( (temp->dane).autor ) == 1 ){
                    free( (temp->dane).autor);
                }

                if( temp->nastepny ){
                    (temp->nastepny)->poprzedni = temp->poprzedni;
                }
                if( temp-> poprzedni ){
                    (temp->poprzedni)->nastepny = temp->nastepny;
                }else{
                    pierwszy = temp->nastepny;
                }

                usuwamy = temp;

                printf("Usunieto!\n");

                temp = temp->nastepny;
                free(usuwamy);


            }else{
                temp = temp->nastepny;
            }
        }while(temp);  //while temp != 0

    }
}

char* znajdz_autora(char* autor){
    wezel *temp = pierwszy;

    while(temp){
        if(strcmp( (temp->dane).autor, autor)==0){
            return (temp->dane).autor;
        }
        temp = temp->nastepny;
    }
    return 0;
}

void dodaj_ksiazke(){
    char bufor[256];
    printf("Podaj tytul: ");
    scanf(" %[^\n]s", bufor);

    unsigned dlugosc = strlen(bufor);

    wezel *nowy = (wezel*)malloc(sizeof(wezel));

    if(nowy){
        (nowy->dane).tytul = (char*)malloc(dlugosc+1);

        if ( (nowy->dane).tytul ){
            strcpy( (nowy->dane).tytul, bufor);
        }
    //}

        printf("Podaj autora: ");
        scanf(" %[^\n]s", bufor);

        if(ile_ksiazek_autora(bufor) > 0){
            (nowy->dane).autor = znajdz_autora(bufor);
        }else{
            dlugosc = strlen(bufor);
            (nowy->dane).autor = (char*)malloc(dlugosc+1);

            if( (nowy->dane).autor){
                strcpy( (nowy->dane).autor, bufor );
            }
        }

        printf("Podaj cene i ilosc ksiazek: ");
        scanf(" %lf %u", &( (nowy->dane).cena ), &( (nowy->dane).ilosc ));

        nowy->poprzedni = 0;
        nowy->nastepny = pierwszy;

        if(pierwszy){
            pierwszy->poprzedni = nowy;
        }

        pierwszy = nowy;
    }
}


void wyswietl_liste(){

    wezel* temp = pierwszy;
    while(temp){
        printf("%s\n%s\n%f, %u\n\n",
               (temp->dane).tytul, (temp->dane).autor,
               (temp->dane).cena, (temp->dane).ilosc);
        temp = temp->nastepny;
    }
}


void zapisz_do_pliku(){
    wezel *temp = pierwszy;
    FILE *plik = fopen("baza.txt", "w");

    if(plik){
        while(temp){
            fprintf(plik, "%s\n%s\n%f, %u\n\n",
            (temp->dane).tytul, (temp->dane).autor,
            (temp->dane).cena, (temp->dane).ilosc);

            temp = temp->nastepny;
        }
     fclose(plik);
    }
}

int main(){

    int menu;

    do{
        printf("Menu: ");
        scanf("%d", &menu);

        if(menu==1) dodaj_ksiazke();
        else if(menu==2) usun_ksiazki_z_zerowym_stanem();
        else if(menu==3) wyswietl_liste();
        else if(menu==4) zapisz_do_pliku();

    }while(menu!=5);

    return 0;
}
