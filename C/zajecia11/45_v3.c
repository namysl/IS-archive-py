/*
Napisz wielowątkowy program, który jak najszybciej wypełnia losowymi liczbami podaną tablicę.
Porównaj jego szybkość działania do jednowątkowego programu. Zastanów się nad otrzymanymi czasami.
*/
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <x86intrin.h>
#include <pthread.h>
#include <stdint.h>
#define N 1024*1024*64
#define il_watkow 8
int *tab;
int liczby[il_watkow];

 

// Inicjuje MT[] dla generatora Mersenne Twister
uint32_t MT[il_watkow][624];
uint32_t mti = 0;
void InicjujMT(int watek,uint32_t x0){
    uint64_t x;
    uint32_t i=0;
    MT[watek][0] = x0;
    do{
        x = MT[watek][i];
        x = (23023 * x) & 0xffffffffull;
        i++;
        x = (    3 * x) & 0xffffffffull;
        MT[watek][i] = x;
    }while(i < 623);
}
// Generator liczb losowych Mersenne Twister
uint32_t MTrand(int watek){
  const uint32_t MA[] = {0,0x9908b0df};
  uint32_t y,i1,i397;
  i1      = mti +   1; if(  i1 > 623) i1 = 0;
  i397    = mti + 397; if(i397 > 623) i397 -= 624;
  y       = (MT[watek][mti] & 0x80000000) | (MT[watek][i1] & 0x7fffffff);
  MT[watek][mti] = MT[watek][i397] ^ (y >> 1) ^ MA[y & 1];
  y       = MT[watek][mti];
  y       ^=  y >> 11;
  y       ^= (y <<  7) & 0x9d2c5680;
  y       ^= (y << 15) & 0xefc60000;
  y       ^=  y >> 18;
  mti     = i1;
  return y;
}

 

void* losujtablice(void *arg){
    int watek = (*(int*)arg);
    int przesuniecie = (N/il_watkow)* watek;
    const uint32_t MA[] = {0,0x9908b0df};
    uint32_t y,i1,i397;

 

    for(int i=(N/il_watkow -1);i>=0;i--){
        i1      = mti +   1; if(  i1 > 623) i1 = 0;
        i397    = mti + 397; if(i397 > 623) i397 -= 624;
        y       = (MT[watek][mti] & 0x80000000) | (MT[watek][i1] & 0x7fffffff);
        MT[watek][mti] = MT[watek][i397] ^ (y >> 1) ^ MA[y & 1];
        y       = MT[watek][mti];
        y       ^=  y >> 11;
        y       ^= (y <<  7) & 0x9d2c5680;
        y       ^= (y << 15) & 0xefc60000;
        y       ^=  y >> 18;
        mti     = i1;
        tab[i+przesuniecie]= y;
    }
    return NULL;
}

 

int main(){
    pthread_t watki[il_watkow];
    unsigned long long c1,c2;
    int rdzen,zwrot;
    for(int i =0;i<il_watkow;i++){
        liczby[i]=i;
        InicjujMT(i,time(0));
    }
    tab = (int*) malloc(N*sizeof(int));
    if(tab){
        printf("Alokacja powiodla sie\n");
        srand(time(0));
        for(int i=N-1;i>=0;i--)
            tab[i]= 0;
        // jeden wątek
        c1 = __rdtscp(&rdzen);
        for(int i=N-1;i>=0;i--)
            tab[i]= MTrand(0);
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