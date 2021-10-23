#include <stdio.h>
#include <string.h>

int main(){

    unsigned long long int liczba = 0;

    printf("Podaj liczbe: ");
    scanf(" %llu", &liczba);

    //printf("%llu\n", liczba);

    char str_liczba[21];
    sprintf(str_liczba, "%llu\n", liczba);

    //printf("%s\n", str_liczba);

    size_t len = strlen(str_liczba);

    for (int i=0; i<len; i++){
        //printf("%c\n", str_liczba[i]);
        sprawdz_znak(str_liczba[i]);
        printf(" ");
    }

    printf("\n");

    return 0;
}


void sprawdz_znak(char znak){

    switch (znak){
        case '0':
            printf("zero");
            break;
        case '1':
            printf("jeden");
            break;
        case '2':
            printf("dwa");
            break;
        case '3':
            printf("trzy");
            break;
        case '4':
            printf("cztery");
            break;
        case '5':
            printf("piec");
            break;
        case '6':
            printf("szesc");
            break;
        case '7':
            printf("siedem");
            break;
        case '8':
            printf("osiem");
            break;
        case '9':
            printf("dziewiec");
            break;
    }
}
