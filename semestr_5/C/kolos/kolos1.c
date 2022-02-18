#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <time.h>
#include <stdlib.h>
#include <ctype.h>

int main(){
    char mail[256];
    bool poprawny = true;

    do {
        printf("Podaj adres mailowy (do 256 znakow): ");
        scanf(" %256s", mail);
        fflush(stdin);

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

    //char *tablica;
    int rozmiar;

    if (liczba == 1){
        rozmiar = 1024;
    }
    if (liczba == 2){
        rozmiar = 2048;
    }
    if (liczba == 4){
        rozmiar = 4096;

    }

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

    return 0;
}

/*
Punkty 78/100

Zestaw 1
- pobranie adresu 3/5, poprawność (@,1,A,a) 10/10, pętla poprawiająca 5/5, wyświetlenie z dużych 10/10
- alokacja 10/10, poprawność 0/5, zwolnienie 0/5
- losowość rozmiaru 15/15, wczytanie tekstu 15/15, limit 0/5, ignorowanie pozostałych 0/5

+ linia 13, zbyt długi mail nie zostanie wczytany
+ linia 110, zbyt długa zawartość maila nie zostanie wczytany, rozumiem, że wykomentowany kod nie działał dobrze i stąd ta proteza
+ linia 117, powinna być przypisana wartość 0
+ linia 121, powinno to być przed pętlą sprawdzone
+ linie 131-134 powinny być poza linią bez ponownej alokacji, tylko komunikat o błędzie wystarczy
+ linia 135, wewnątrz pętli sprawdzamy już drugi warunek i wypisujemy stosowny komunikat, tu należy więc go usunąć
*/
