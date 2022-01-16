#include <stdio.h>
#include <stdlib.h>

int* tab = 0;
unsigned rozmiar;

int main(){
    int x;

    printf("Podaj rozmiar tablicy: ");
    scanf(" %u", &rozmiar);
    tab = (int*)malloc(rozmiar*sizeof(int));
    printf("Adres tablicy dynamicznej: %p\n", tab);
    int tab2[rozmiar];
    printf("Adres tablicy statycznej: %p\n", tab2);

    int y;

    printf("Adres x: %p\nAdres y: %p", &x, &y);

    return 0;
}
