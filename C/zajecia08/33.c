#include <stdio.h>

typedef union rzeczywista{
    double x;
    long long int y;

    /*
    struct{
        long lont int resztabitow:63;
        long long int znak:1;
    }
    */

}rzeczywista;


int main(){

    rzeczywista zmienna;
    printf("Podaj liczbe rzeczywista: ");
    scanf(" %lf", &(zmienna.x));

    zmienna.y &= 0x7FFFFFFFFFFFFFFF; // zmienna.znak=0;
    printf("Wartosc bezwzgledna = %f", zmienna.x);

    return 0;
}
