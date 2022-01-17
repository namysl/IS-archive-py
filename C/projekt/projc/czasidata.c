#include <stdio.h>
#include <time.h>

time_t czas;
struct tm *data;
FILE *plik;

void add_entry(){
    czas = time(0);
    data = localtime(&czas);
    plik = fopen("czasidata.txt", "w");

    if(plik){
        fprintf(plik, "%d %d %d\n%d %d %d\n",
                data->tm_year+1900, data->tm_mon+1, data->tm_mday,
                data->tm_hour, data->tm_min, data->tm_sec);

        fclose(plik);
        printf("Zapisano\n");
    }
    else{
        perror("Plik nie mogl zostac otwarty: ");
    }
}

void edit_entry(){

}

void delete_entry(){

}

void check_date(){

}

int local_time(){
    time_t T = time(NULL);
    struct tm tm = *localtime(&T);

    printf("System Date is: %02d/%02d/%04d\n", tm.tm_mday, tm.tm_mon+1, tm.tm_year + 1900);
    printf("System Time is: %02d:%02d:%02d\n", tm.tm_hour, tm.tm_min, tm.tm_sec);

    return 0;
}

void show_entry(){
    int zmienna;
    plik = fopen("czasidata.txt", "r");

    if(plik){
        for(int j=0; j<3; j++){
            fscanf(plik, " %d", &zmienna);
            printf("%d/", zmienna);
        }
        printf("\b ");  //usuwa ostatni slash i dodaje spacje
        for(int j=0; j<3; j++){
            fscanf(plik, " %d", &zmienna);
            printf("%d:", zmienna);
        }
        printf("\b \n\n"); //usuwa ostatni dwukropek
    }

    else{
        perror("Plik nie mogl zostac otwarty2");
    }
}

int main(){
    char menu;

    while(1){
        printf("Wybierz opcje:\n");
        printf("1 Zapis czasu i daty do pliku\n2 Odczyt czasu i daty z pliku\n3 Koniec\n\n");
        scanf(" %c", &menu);

        if(menu=='1')
            add_entry();
        else if(menu=='2')
            show_entry();
        else if(menu=='3')
            break;
        else if(menu == '4')
            local_time();
        else
            printf("Bledny wybor");
            continue;
    }
    return 0;
}
