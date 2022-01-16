#include <stdio.h>

/* struktura trojkat przechowujaca dlugosci bokow trojkata.
napisz funkcje, ktora jako argument ma zmienna typu trojkat,
i zwraca jako wartosc obwod trojkata przekazanego w argumencie */


typedef struct{
    double a;
    double b;
    double c;

}trojkat;

double obwod(trojkat t){
    return (t.a + t.b + t.c);
}


int main(){

    trojkat tr;
    tr.a = 1;
    tr.b = 2;
    tr.c = 3;

    printf("%f", obwod(tr));

    return 0;
}
