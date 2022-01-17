#include <stdio.h>
#include <stdlib.h>
#include <time.h>

time_t czas;
struct tm *data;
FILE *plik;

/*
typedef struct{
    int d, m, y; //day, month, year
    int h, mi; //hour, minutes
    char description[];
}event;
*/

void add_entry(){
    czas = time(0);
    data = localtime(&czas);
    plik = fopen("czasidata.txt", "a");

    if(plik == NULL){
        perror("Plik nie mogl zostac otwarty: ADD_ENTRY");
        exit(EXIT_FAILURE);
    }

    fprintf(plik, "%04d %02d %02d\n%02d %02d %02d\n",
            data->tm_year+1900, data->tm_mon+1, data->tm_mday,
            data->tm_hour, data->tm_min, data->tm_sec);

    fclose(plik);
    printf("Zapisano date\n");
}

void add_text(){
    char ch;
    plik = fopen("czasidata.txt", "a");

    if(plik == NULL){
        perror("Plik nie mogl zostac otwarty: ADD_TEXT ");
        exit(EXIT_FAILURE);
    }

    printf("Podaj wiadomosc: ");

    while( (ch = getchar()) != '\n' ) {
        putc(ch, plik);
    }
    putc('\n', plik);
    putc('#', plik);

    fclose(plik);
    printf("Zapisano wiadomosc");
}

int local_time(){
    time_t T = time(NULL);
    struct tm tm = *localtime(&T);

    printf("System Date is: %02d/%02d/%04d\n", tm.tm_mday, tm.tm_mon+1, tm.tm_year+1900);
    printf("System Time is: %02d:%02d:%02d\n", tm.tm_hour, tm.tm_min, tm.tm_sec);

    return 0;
}

void show_entry(){
    int zmienna;
    char c;
    plik = fopen("czasidata.txt", "r");

    if(plik){
        for(int j=0; j<3; j++){
            fscanf(plik, " %d", &zmienna);
            printf("%02d/", zmienna);
        }
        printf("\b ");  //usuwa ostatni slash i dodaje spacje
        for(int j=0; j<3; j++){
            fscanf(plik, " %d", &zmienna);
            printf("%02d:", zmienna);
        }
        printf("\b \n"); //usuwa ostatni dwukropek

        do{
            fscanf(plik, "%c", &c);
            printf("%c", c);
        }while(c != '#');

        printf("\b \n");

        fclose(plik);
    }
    else{
        perror("Plik nie mogl zostac otwarty: SHOW_ENTRY ");
    }
}

int main(){
    char menu;

    do{
        printf("Wybierz opcje:\n");
        printf("1 Zapis czasu i daty do pliku\n2 Odczyt czasu i daty z pliku\n3 Dodaj tekst\n4 Pokaz czas lokalny\n9 Exit\n");
        scanf("%[^\n]%*c", &menu);

        switch(menu){
        case '1':
            add_entry();
            break;
        case '2':
            show_entry();
            break;
        case '3':
            add_text();
            break;
        case '4':
            local_time();
            break;
        case '5':
            add_entry();
            add_text();
            break;
        case '9':
            exit(0);
        default:
            printf(". . .");
            break;
        }
    }while (menu!=9);
    return 0;
}