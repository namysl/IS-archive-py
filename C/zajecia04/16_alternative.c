#include <stdio.h>

int main(){

    int n;
    printf("Podaj n: ");
    scanf(" %d", &n);

    int array[n];
    array[0] = 0;
    array[1] = 0;

    for (int i=2; i<n; i++){
        array[i] = i;
    }

    for (int i=2; i<n; i++){
        if (((i % 2 != 0)||(i==2)) && (i % 3 != 0 ||(i==3))
        && (i % 5 != 0 ||(i==5)) && (i % 7 != 0) || (i==7)){
            continue;
        }
        else{
            array[i] = 0;
        }
    }

    for (int i=2; i<n; i++){
        if (array[i] != 0){
            printf("%d, ", array[i]);
        }
    }

    return 0;
}

