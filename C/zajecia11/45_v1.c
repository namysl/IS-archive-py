#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <x86intrin.h>
#define N 1024*1024
#define il_watkow 8

int main(){
    unsigned long long c1, c2;
    int rdzen;
    int *tab = (int*)malloc(N*sizeof(int));

    if(tab){
        printf("Alokacja powiodla sie\n");
        srand(time(0));
        for(int i=N-1; i>=0; i--)
            tab[i] = 0;
        c1 = __rdtscp(&rdzen);
        for(int i=N-1;i>=0;i--)
            tab[i] = rand();
        c2 = __rdtscp(&rdzen);
        printf("Ilosc cykli dla wypelniania losowymi 1 watkiem: %llu\n", c2-c1);
    }else{
        printf("Alokacja nie powiodla sie\n");
    }
    return 0;
}