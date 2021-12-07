#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    unsigned m;
    printf("Podaj ilość słów: ");
    scanf(" %u",&m);
    char* wsk=(char*)malloc(24*m);

    if(wsk){
        for(int i=0; i<m; i++){
            scanf(" %23s", wsk+24*i);
        }
        qsort(wsk, m, 24, strcmp);

        printf("\nPosortowano\n");

        for(int i=0;i<m;i++){
            printf("%s\n", wsk+24*i);
        }
    }
    else{
        printf("Błąd alokacji pamięci");
    }
}
