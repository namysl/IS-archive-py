#include <stdio.h>
#include <time.h>

int main(){
    char menu;

    while(1){
        printf("1: zapisz date i komunikat\n2: Wyswietl wszystkie komunikaty\n3: koniec\n");
        scanf(" %c", &menu);

        if(menu=='1'){
            printf("Podaj date (rok, miesiac, dzien)");
            int zmienna;
            FILE *plik = fopen("baza.txt", "a");

            if(plik){
                for(int i=0; i<3; i++){
                    scanf(" %d", &zmienna);
                    fprintf(plik, "%d ", zmienna);
                }

                printf("Podaj komunikat: ");
                char znak;
                // tutaj wyczyscic bufor
                do{
                    znak = getchar();
                    fputc(znak, plik);
                }while(znak != "\n");
            }
            else{
                perror("oops opcja 1 padla");
            }
        }

        if(menu=='2'){
            time_t czas;
            struct tm* data;
            czas = time(0);
            data = localtime(&czas);

            FILE* plik = fopen("baza.txt", "r");

            if(plik){
                while(!feof(plik)){
                    int rok, miesiac, dzien;
                    fscanf(plik, " %d", &rok);
                    fscanf(plik, " %d", &miesiac);
                    fscanf(plik, " %d", &dzien);

                    char czywypisywac = 0;
                    char znak;
                    if ( (rok==data->tm_year+1900) && (miesiac==data->tm_mon+1) && (dzien==data->tm_mday) ){
                        czywypisywac = 1;
                    }

                    fgetc(plik);
                    do{
                        znak = fgetc(plik);
                        if(czywypisywac){
                            putchar(znak);
                        }
                    }while(znak!='\n');
                }
            }
            else{
                perror("Blad 2");
            }
        }

        if(menu=='3'){
            printf("Zakonczono");
            break;
        }
    }

    return 0;
}
