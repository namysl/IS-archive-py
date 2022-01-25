/*
Napisz wielowątkowy program, który jak najszybciej wypełnia losowymi liczbami podaną tablicę.
Porównaj jego szybkość działania do jednowątkowego programu. Zastanów się nad otrzymanymi czasami.
*/
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <x86intrin.h>
#include <pthread.h>
#define N 1024*1024
#define il_watkow 8
int *tab;

 

int liczby[il_watkow];

 

void* losujtablice(void *arg){
    int przesuniecie = (N/il_watkow)* (*(int*)arg);
    for(int i=(N/il_watkow -1);i>=0;i--)
        tab[i+przesuniecie]= rand();
    return NULL;
}

 

int main(){
    pthread_t watki[il_watkow];
    unsigned long long c1,c2;
    int rdzen,zwrot;
    for(int i =0;i<il_watkow;i++) liczby[i]=i;
    tab = (int*) malloc(N*sizeof(int));
    if(tab){
        printf("Alokacja powiodla sie\n");
        srand(time(0));
        for(int i=N-1;i>=0;i--)
            tab[i]= 0;
        // jeden wątek
        c1 = __rdtscp(&rdzen);
        for(int i=N-1;i>=0;i--)
            tab[i]= rand();
        c2 = __rdtscp(&rdzen);
        printf("Ilosc cykli dla wypelniania losowymi 1 watkiem: %llu\n",c2-c1);
        // wiele wątków
        c1 = __rdtscp(&rdzen);
        for(int i=il_watkow -1;i>=0;i--){
            zwrot = pthread_create(&watki[i],NULL,losujtablice,(void*) &(liczby[i]));
            if(zwrot) printf("Nie udalo sie utworzyc watku nr. %d\n",i);
        }
        for(int i=il_watkow -1;i>=0;i--){
            if(pthread_join(watki[i],NULL)) printf("Blad konczenia watku nr. %d\n",i);
        }
        c2 = __rdtscp(&rdzen);
        printf("Ilosc cykli dla wypelniania losowymi %d watkami: %llu\n",il_watkow,c2-c1);
    } else {
        printf("Alokacja nie powiodla sie\n");
    }
    return 0;
}