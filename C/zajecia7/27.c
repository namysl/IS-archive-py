#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdarg.h>

double norma(unsigned n,...){
    va_list wspolrzedne;
    va_start(wspolrzedne, n);
    double suma = 0, x;

    for(int i=0; i<n; i++){
        x = va_arg(wspolrzedne, double);
        suma += x*x;
    }

    va_end(wspolrzedne);
    return sqrt(suma);
}


int main()
{
    printf("||(1,2,3)|| = %f\n",norma(3, 1.0, 2.0, 3.0));
    return 0;
}
