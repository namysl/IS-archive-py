#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdarg.h>


int main()
{
    FILE * plik;
    char nazwa_pliku[64];
    char c, menu;
    do{
        printf("Wybierz ocje:\n1)Wyswietl zawartosc\n2)Zapisz tekst do pliku\n");
        scanf(" %c",&menu);
        if(menu=='1'){
            printf("Podaj nazwe pliku\n");
            scanf(" %[^\n]s", nazwa_pliku);
            plik = fopen(nazwa_pliku,"r");
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
            
            }
            else{
                perror("Problem z otworzeniem pliku!");
            }
        }
        else if(menu=='2'){
            printf("Podaj nazwe pliku\n");
            scanf(" %[^\n]s", nazwa_pliku);
            plik = fopen(nazwa_pliku,"w");
            if(plik){
                printf("Podaj tekst do zapisania");
                while(1){
                    c = getchar();
                    if(c!='\n'){
                        fputc(c,plik);
                    }                  
                    else{
                        break;
                    }
                    
                }fclose(plik);
            }
            else{
                perror("Problem z otworzeniem pliku!");
            }
        }
        else{
            printf("Nieprawidłowy wybór");
        }
    }while(menu!='3');
}
