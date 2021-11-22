#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void wyswietl(int *A, int n){
    int nn = 0;

    for (int i=0; i<n; i++){
        for (int j=0; j<n; j++){
            printf(" %d", A[n*i+j]);
            nn++;

            if (nn == (int) n){
                printf("\n");
                nn = 0;
            }
        }
    }
}

int wypelnij(int *A, int n){
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            A[n*i+j] = i+j;
        }
    }
    return 0;
}

int main(){
    int n;
    printf("Podaj n: ");
    scanf(" %d", &n);

    int *tablica = (int*)malloc(sizeof(int)*n*n);

    /*
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            tablica[n*i+j] = i+j;
        }
    }*/

    wypelnij(tablica, n);
    wyswietl(tablica, n);

    for(int x=0; x<n; x++){
        for(int y=0; y<n; y++){
            printf("%d ", (*tablica)++);
        }
    }

    return 0;
}
