#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

int main(){
/*
    int x, y;

    printf("Podaj x: ");
    scanf(" %d", &x);
    printf("Wartosc x: %d\n", x);

    printf("Podaj y: ");
    scanf(" %d", &y);
    printf("Wartosc y: %d\n", y);
*/



/*
    char a;

    printf("Podaj znak: ");
    a = getchar();
    printf("Podany znak: %c\n", a);

    fflush(stdin);

    char lancuch[10];

    printf("Pisz: ");
    for(int i=0; i<10; i++){
        lancuch[i] = getchar();
    }

    for(int i=0; i<10; i++){
        printf("%c", lancuch[i]);
    }
    printf("%\n");
    clean_stdin();

    puts("To byl test\n");

    printf("Pisz cos: \n");
    do{
        a = getchar();
        putchar(a);
    }while(a!='\n');
*/



/*
    char napis[16];

    printf("Mozna tez tak: \n");
    puts ("Wpisz zdanie:\n");
    fgets(napis, 16, stdin);
    printf("%s\n",napis);
    fflush(stdin);
    fgets(napis, 16, stdin);
    printf("%s\n",napis);
*/



/*
    int tablica2[3][3];

    for(int i=0;i<3;i++)
        for(int j=0;j<3;j++)
            tablica2[i][j]=i*j;

    for(int i=0; i<3; i++){
        for(int j=0; j<3; j++){
            printf("%d ", tablica2[i][j]);
        }
        printf("\n");
    }
*/


/*
    int x = 666;
    int *pointer_x = 0; //pusty wskaznik
    pointer_x = &x; //wskazuje na x, czyli zawiera jej adres

    int y = *pointer_x; //y=x
    (*pointer_x)++; //zwieksza x o 1; x=667
    *pointer_x++; //zwieksza wskaznik o rozmiar typu wskaznik (intsize=4, pointer_x nie wskazuje juz na x?)

    printf("x = %d\n", x);
    printf("*pointer_x WARTOSC = %d\n", *pointer_x);
    printf("pointer_x ADRES = %d\n", pointer_x);
    printf("&pointer_x ADRES WSKAZNIKA = %d\n", &pointer_x);
    printf("y = %d\n", y);
*/



/*
    int rozmiar = 60;
    char *tablica = (char*)malloc(rozmiar * sizeof(char));
    printf("Wpisz tekst wiadomosci: ");


    //scanf(" %[^\n]s", tablica);
    //printf("%s\n", tablica);

    //printf("Rozmiar tablicy: %d\n", rozmiar);


    char znak;
    int liczba_znakow = 0;

    if (tablica){
        do{
            znak = getchar();
            if (liczba_znakow < rozmiar){
                tablica[liczba_znakow] = znak;
                liczba_znakow++;
            }
            else{
                printf("Za malo pamieci");
                break;
            }
        } while(znak != '\n');
    }
    else{
        printf("Co sie stalo z tablica?");
        printf("Blad");
    }

    for(int i=0; i<rozmiar; i++){  //problem z rozmiarem, jak nie wykorzysta sie wszystkiego, to pamiec nie jest pusta!
        printf("%c", tablica[i]);
    }

    printf("%s", tablica);
    puts(tablica);
*/


/*
    int n=64;
    int *pTab1=(int*) malloc(n);
    int *pTab2=(int*) malloc(n);

    if(pTab1==0 || pTab2==0)
        printf("Za malo pamieci\n");
    else{
        memset(pTab1, 0, n); //wypelnia pTab1 wartoscia 0
        memcpy(pTab2, pTab1, n);  //kopia do pTab2
    }

    printf("%d\n", *pTab1);
    printf("%d\n", *pTab2);
*/



/*
    const char *src = "elo";

    // strlen zwraca d³ugoœæ ³añcucha bez znaku '\0'
    char dst[strlen(src)+1];

    // strcpy kopiuje równie¿ znak '\0'
    strcpy(dst, src);

    puts(dst);
*/


/*)
    char szA[32]={"Nowak Jan"};
    char szB[32]={"Kowalski Piotr"};
    char szTmp[32];

    if(strcmp(szA,szB)>0){// sortowanie
        strcpy(szTmp, szA);
        strcpy(szA, szB);
        strcpy(szB, szTmp);
    }

    puts(szA);
    puts(szB);
*/

    int len=0;
    char bufor[256];
    FILE *plik;
    plik=fopen("wyjscie.txt","r+");

    if(plik){
        printf("Otwarto plik. Pierwsze 26 znaki beda zmienione:\n");
        fscanf(plik, "%[26]s", bufor);
        bufor[26]=0;

        while(len<26){
            bufor[len] = 'A'+len;
            len++;
        }
        len=fprintf(plik, "%s", bufor);
        printf("Zapisano znakow %d\n", len);

    }else{
        printf("Nie udalo sie otworzyc pliku.\n");
    }

    fclose(plik);




    return 0;
}



void clean_stdin(void){
    //czyœcik
    for(char c=getchar();c!='\n' && c!=EOF; c=getchar());
}
