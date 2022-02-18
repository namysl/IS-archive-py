#include <stdio.h>

#define suma(x, y, z) (x)+(y)+(z)

int main(){
    double x, y, z;

    printf("Podaj trzy liczby rzeczywiste: ");
    scanf(" %lf %lf %lf", &x, &y, &z);
    printf("Suma: &f\n", suma(x, y, z));

    int k, m, n;

    printf("Podaj trzy liczby calkowite: ");
    scanf(" %d %d %d", &k, &m, &n);
    printf("Suma: %d", suma(k, m, n));

    return 0;
}