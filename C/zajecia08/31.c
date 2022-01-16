#include <stdio.h>

typedef union mix{

    int liczba;

    struct{
        char bajt0;
        char bajt1;
        char bajt2;
        char bajt3;
    };

}mix;

int main(){

    mix zmienna;
    printf("Podaj inta: ");
    scanf(" %d", &(zmienna.liczba));
    printf("Bajty zmiennej: %hhd, %hhd, %hhd, %hhd", zmienna.bajt0, zmienna.bajt1, zmienna.bajt2, zmienna.bajt3);

    return 0;
}
