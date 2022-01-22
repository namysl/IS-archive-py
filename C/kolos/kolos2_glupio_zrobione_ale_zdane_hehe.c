#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//Zestaw 4

typedef struct szkola{
    char nazwa[500];
    int ilu_nauczycieli;
    int ilu_uczniow;

    struct szkola *poprzednia;
}szkola;


szkola *pierwsza;
FILE *plik;


szkola dodaj(){
    //dodaj nowa szkole

    //printf("%s", pierwsza->nazwa);
    szkola *nowa = (szkola*) malloc(sizeof(szkola));

    if(nowa){
        printf("Nazwa szkoly: ");
        scanf(" %[^\n]s", &(nowa->nazwa));

        printf("Liczba nauczycieli: ");
        scanf(" %d", &(nowa->ilu_nauczycieli));

        printf("Liczba uczniow: ");
        scanf(" %d", &(nowa->ilu_uczniow));
    }
    else{
        printf("Blad alokacji");
    }

    //printf("NAZWA: %s, NAUCZYCIELE: %d, UCZNIOWIE: %d\n", nowa->nazwa, nowa->ilu_nauczycieli, nowa->ilu_uczniow);

    printf("Dodano\n");
    return *nowa;
}


int edytuj(szkola *wskaznik){
    //zmien dane ilosciowe szkoly
    int liczba;

    if(wskaznik){
        printf("Podaj nowa liczbe nauczycieli: ");
        scanf(" %d", &liczba);
        wskaznik->ilu_nauczycieli = liczba;

        printf("Podaj nowa liczbe uczniow: ");
        scanf(" %d", &liczba);
        wskaznik->ilu_uczniow = liczba;
    }

    printf("Zmieniono\n");

    return 0;
}


int zapisz_do_pliku(szkola *wskaznik){
    //zapisz liste szkol do pliku

    plik = fopen("szkoly.dat", "a");

    if (plik){
        fprintf(plik, "nazwa: %s\n", wskaznik->nazwa);
        fprintf(plik, "nauczyciele: %d\n", wskaznik->ilu_nauczycieli);
        fprintf(plik, "uczniowie: %d\n\n", wskaznik->ilu_uczniow);
    }
    else{
        perror("Blad, nie mozna otworzyc pliku\n");
    }
    fclose(plik);

    printf("Zapisano do pliku\n");

    return 0;
}


int odczyt_z_pliku(){
    //odczytaj liste szkol z pliku
    char znak;
    plik = fopen("szkoly.dat", "r");

    if (plik){
        while((znak=fgetc(plik))!=EOF){
            putchar(znak);
        }
        if(feof(plik)){
            printf("\n Odczytano caly plik\n");
        }
        if(ferror(plik)){
            printf("\nWystapil blad przy odczytywaniu pliku\n");
        }
    }

    else{
        perror("Blad, nie mozna otworzyc pliku\n");
    }
    printf("\n");
    fclose(plik);

    return 0;
}


int main(){

    //testy:
    szkola nowa1 = {"Jakas nazwa", 10, 100};
    printf("%s, %d, %d\n", nowa1.nazwa, nowa1.ilu_nauczycieli, nowa1.ilu_uczniow);

    szkola nowa2 = dodaj();
    printf("Nowa szkola test: %s\n", nowa2.nazwa);

    edytuj(&nowa2);

    printf("Liczba nauczycieli: %d\n", nowa2.ilu_nauczycieli);
    printf("Liczba uczniow: %d\n", nowa2.ilu_uczniow);

    zapisz_do_pliku(&nowa2);

    printf("Odczyt z pliku\n");
    odczyt_z_pliku();
    //koniec


    char znak;

    printf("\n0 -> wyjscie\n");
    printf("1 -> dodaj szkole\n");
    printf("2 -> edytuj szkole\n");
    printf("3 -> zapisz do pliku szkoly.dat\n");
    printf("4 -> odczyt z pliku szkoly.dat\n");

    do{
        znak = getchar();

        szkola nowa;

        if(znak=='0')
            return 0;
        else if(znak=='1')
            nowa = dodaj();
        else if(znak=='2')
            edytuj(&nowa);
        else if(znak=='3')
            zapisz_do_pliku(&nowa);
        else if(znak=='4')
            odczyt_z_pliku();

    }while(znak!='0');

    return 0;
}



/*
Suma: 50/100
- struktura 10/10, menu 10/10,
- otwieranie i zamykanie pliku 10/10, zapis do pliku 5/10, odczyt z pliku 0/10,
- wyœwietlanie uporz¹dkowane 0/15, wyszukiwanie 0/15, funkcja dodaj¹ca/zmieniaj¹ca 15/20

Szczegó³y:
- linie 138-142 powinny byæ równie¿ w pêtli 144-160
- zapis do pliku, nie zapisujmy znaków, które nam utrudni¹ wczytanie z pliku listy
- odczyt z pliku do listy nie istnieje
- nie mamy listy szkó³, tylko jedna zmienna lokalna (w funkcji dodaj¹cej jest wyciek pamiêci!)
- nie ma funkcji wyszukuj¹cej
- nie ma funkcji wyœwietlaj¹cej listê posortowan¹
*/
