#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <time.h>
#include <stdlib.h>

int main(){
    char mail[256];
    bool poprawny = true;

    do {
        printf("Podaj adres mailowy: ");
        scanf(" %s", mail);

        //printf("Podany adres: %s\n", mail);

        int len = strlen(mail);
        //printf("len:%d\n", len);

        int malpa = 0;
        int blad = 0;

        //SCANF DO SKUTKU
        for(int x=0; x<len; x++){
            if(mail[x] == '@'){
                malpa++;
                if (malpa > 1){
                    poprawny = false;
                    break;
                }
            }
            else if( (mail[x] > 47 && mail[x] < 58) ||
                    (mail[x] > 64 && mail[x] < 91) ||
                    (mail[x] > 96 && mail[x] < 123) ){
                continue;
            }
            else{
                poprawny = false;
                blad++;
                break;
            }
        }

        if(malpa != 1 || blad > 0){
            printf("Blad\n");
            poprawny = false;
        }
        else{
            printf("Podano prawidlowy adres\n");
            poprawny = true;
        }

    }while(poprawny == false);


    //DUZE LITERY
    printf("Adres z duzymi literami: ");

    int len = strlen(mail);

    for(int x=0; x<len; x++){
        if (mail[x] > 96 && mail[x] < 123){
            printf("%c", toupper(mail[x]));
        }
        else{
            printf("%c", mail[x]);
        }
    }
    printf("\n");

    //ALOKACJA O LOSOWYM ROZMIARZE (1kB, 2kB lub 4kB)

    int m = 1;
    int n = 4;
    int liczba;

    srand(time(0));
    do{
        liczba = m + (rand() % (n+1-m));
    } while(liczba == 3);

    printf("wylosowana: ");
    printf("%d\n", liczba);

    //1kB = 1024B
    //2kB = 2048B
    //4kb = 4096B

    char *tablica;
    int rozmiar;

    if (liczba == 1){
        rozmiar = 1024;
        char *tablica = (char*)malloc(rozmiar * sizeof(char));
    }
    if (liczba == 2){
        rozmiar = 2048;
        char *tablica = (char*)malloc(rozmiar * sizeof(char));
    }
    if (liczba == 4){
        rozmiar = 4096;
        char *tablica = (char*)malloc(rozmiar * sizeof(char));
    }

    printf("Wpisz tekst wiadomosci: ");




    scanf(" %[^\n]s", tablica);
    printf("%s\n", tablica);

    printf("Rozmiar tablicy: %d\n", rozmiar);

    /*
    char znak;
    int liczba_znakow;

    do{
        znak = getchar();
        if (tablica){
            if (liczba_znakow < rozmiar){
                tablica[liczba_znakow] = znak;
                liczba_znakow++;
            }
            else{
                printf("Za malo pamieci");
                break;
            }
        }
        else{
            printf("Co sie stalo z tablica?");
            char *tablica = (char*)malloc(sizeof(char)*rozmiar);
        }
    } while(znak != '\n' && liczba_znakow < rozmiar);
    */

    return 0;
}
