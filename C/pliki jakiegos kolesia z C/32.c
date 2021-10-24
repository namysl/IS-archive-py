#include <stdio.h>

typedef union liczba {
    double x;
    struct {
        long long dol:63;
        long long gora:1;
    };
} liczba;

void main(){
    liczba y;
    y.x = -10.0;
    y.gora = 0;
    printf("%f \n", y.x);
}
