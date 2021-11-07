#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    short int n;
    scanf("%hd", &n);
    while (n <= 0){
       printf("Proszę podać nie ujemną liczbę");
       scanf("%hd", &n);
    } 

    int *tab=(int*)malloc(n*sizeof(int));

    int i;
    int max = 0, min = 0, sum = 0;

    char c;
    short int m;
    short int k;

    srand(time(0));

    for (i = 0; i < n; i++){
        tab[i] = -10+(rand()%(20+1+10));
        if (max < tab[i]) {
            max = tab[i];
        }
        if (min > tab[i]) {
            min = tab[i];
        }
        sum += tab[i];
        printf("%d \n", tab[i]);
    }

    printf("śriednia: %d, max: %d, min: %d \n", sum/n, max, min);

    printf("Podaj jeden ze znaków (+, -, *) \n");
    scanf(" %c", &c);
    printf("Podaj liczbę mniejszą od %hd \n", n);
    scanf(" %hd", &m);

    
    for (i = 0; i < n; i++){
        printf("%d ", tab[i]);
    }

    printf("\n");

    switch (c){
        case '+':
           k = n+m;
           break;
        case '-':
           k = n-m;
           break;
        case '*':
           k = n*m;
           break;
    }
    tab = (int*)realloc(tab, k*sizeof(int));

    if (k > n){
        memcpy(tab+n, tab, k);
    }

    for (i = 0; i < k; i++){
        printf("%d ", tab[i]);
    }

    free(tab);
}
