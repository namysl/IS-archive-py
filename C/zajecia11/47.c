#include <stdio.h>

#define parzystosc(x) ((x) & 1 == 1) ? 0 : 1

#define parzystosc2(x)\
    if(x & 1 == 1)\
        puts("nieparzysta");\
    else\
        puts("parzysta");

int main(){
    int k;

    printf("Podaj liczbe calkowita: ");
    scanf(" %d", &k);
    printf("Parzysta?: %d\n", parzystosc(k));
    parzystosc2(k);

    return 0;
}