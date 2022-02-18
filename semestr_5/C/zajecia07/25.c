#include <stdio.h>

double dodaj(double x, double y){
    return (x+y);
}

double mnoz(double x, double y){
    return (x*y);
}


int main()
{
    double (*wsk)(double, double);

    double x, y;
    char c;

    printf("Podaj dwie liczby: \n");
    scanf(" %lf %lf", &x, &y);

    printf("Wybierz operacje: \n");
    scanf(" %c", &c);

    switch(c){
        case '+':
            wsk = dodaj;
            break;
        case '*':
            wsk = mnoz;
            break;
        default:
            wsk = 0;
            break;
    }

    if(wsk){
        printf("Wynik = %f\n", wsk(x, y));
    }
    else{
        printf("Nieprawidlowe dzialanie");
        return 0;
    }

}
