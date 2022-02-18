#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdarg.h>


int main()
{
    FILE *plik;
    char nazwa_pliku[64];
    char c, menu;
    do{
        printf("Wybierz ocje:\n1)Wyswietl zawartosc\n2)Zapisz tekst do pliku\n3)Aby zakonczyc\n");
        scanf(" %c", &menu);
        if(menu=='1'){
            printf("Podaj nazwe pliku: ");
            scanf(" %[^\n]s", nazwa_pliku);
            plik = fopen(nazwa_pliku, "r");
            if(plik){
                while(1){
                    c = fgetc(plik);
                    if(c!=EOF){
                        putchar(c);
                    }
                    else{
                        break;
                    }

                }fclose(plik);
                printf("\n\n");
            }
            else{
                perror("Problem z otworzeniem pliku!");
            }
        }
        else if(menu=='2'){
            printf("Podaj nazwe pliku: ");
            scanf(" %[^\n]s", nazwa_pliku);

            plik = fopen(nazwa_pliku, "w");

            if(plik == NULL){
                perror("Problem z otworzeniem pliku!");
            }

            printf("\nPodaj tekst do zapisania: ");

            while( (c = getchar()) != '*' ) {
                putc(c, plik);
            }

            fclose(plik);
            }

        else if(menu=='3'){
            return 0;
        }
        else{
            printf("Nieprawidlowy wybor");
        }
    }while(menu != '3');
}
