#include <stdio.h>

int main(){

    int n;
    printf("Podaj n: ");
    scanf(" %d", &n);

    //int array[n];

    for (int i=2; i<n; i++){
        if (((i % 2 != 0)||(i==2)) && (i % 3 != 0 ||(i==3))
            && (i % 5 != 0 ||(i==5)) && (i % 7 != 0) || (i==7)){
            printf("%d, ", i);
        }
    }

    return 0;
}
