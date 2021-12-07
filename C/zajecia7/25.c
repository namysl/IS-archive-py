#include <stdio.h>

double dodaj(double x, double y){
    return (x+y);
}

double mnoz(double x, double y){
    return (x*y);
}


int main()
{
    double (*wsk)(double,double);
    printf("Podaj dane\n");
    double x, y;
    char c;
    scanf(" %lf %lf", &x, &y);
    printf("Wybierz operacje\n");
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
        printf("Nieprawidłowe działanie");
        return 0;
    }
    
}
