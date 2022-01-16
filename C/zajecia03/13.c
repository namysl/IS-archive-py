#include <stdio.h>

int main(){
    char symbol;
    double liczba1;
    double liczba2;
    double wynik = 0;

    printf("Podaj dzialanie: ");
    scanf(" %c", &symbol);
    //fflush(stdin);

    printf("Podaj pierwsza liczbe: ");
    scanf(" %lf", &liczba1);

    //fflush(stdin);
    printf("Podaj druga liczbe: ");
    scanf(" %lf", &liczba2);

    switch (symbol){
        case '+':
            wynik = liczba1 + liczba2;
            break;
        case '-':
            wynik = liczba1 - liczba2;
            break;
        case '*':
            wynik = liczba1 * liczba2;
            break;
        case '/':
            if (liczba2 == 0){
                printf("Dzielenie przez 0!\n");
                break;
            }
            wynik = liczba1 / liczba2;
            break;
        default:
            printf("Zly znak lub brak takiego dzialania\n");
            break;
    }

    printf("Wynik dzialania %c : %f\n", symbol, wynik);

    return 0;
}
