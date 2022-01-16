#include <stdio.h>

int main(){

    int n;
    printf("Podaj n: ");
    scanf(" %d", &n);

    int array[n][n];
    int liczba = 1;

    /*
    for (int i=0; i<n ; i++){
        array[0][i] = liczba;
        liczba++;
    }

    for (int j=1; j<n; j++){
        array[j][n-1] = liczba;
        liczba++;
    }

    int k = n-1;
    for (k; k==0; k--){
        printf("k: %d\n", k);
        array[n-1][k] = liczba;
        liczba++;
    }
    */

    int k = 0;

    do {
    for (int j=k; j < n-k; j++){
        array[k][j] = liczba;
        liczba++;
    }


    for (int i=k+1; i<n-k; i++){
        array[i][n-1-k] = liczba;
        liczba++;
    }

    for (int j=n-2-k; j>=k; j--){
        array[n-k-1][j] = liczba;
        liczba++;
    }

    for (int i=n-2-k; i>k; i--){
        array[i][k] = liczba;
        liczba++;
    }

    k++;

    } while (k < n);


    printf("Utworzona tablica:\n");
    for (int i=0; i<n; i++){
        for (int j=0; j<n; j++){
            printf("%d  ", array[i][j]);
        }
        printf("\n");
    }


    return 0;
}


