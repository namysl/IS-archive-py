#include <stdio.h>

char zmienna_znaku = 'm';
int zmienna_integer = 12;

// komentarz

/*
int main() {
    printf("tekst: %c, liczba: %d", zmienna_znaku, zmienna_integer);
    return 0;
}
*/

//char znak = '\n';

// liczba odpowiadaj¹ca znakom: \n, \r, \t, \b, \a, \f, \\, \', \"

char znaki[9] = { '\n', '\r', '\t', '\b', '\a', '\f', '\\', '\'', '\"' };

void main() {
    for (int i = 0; i < 9; i++) {
        printf("znak: %c liczba: %d\n", znaki[i], znaki[i]);
    }
}


/*
char: -128 -> 127
short
int
long int
long long int
unsigned ...type... -> domyœlnie int - typ ca³kowity bez znaku

printf();
signed:
%c, %hd, %d, %ld, %lld

unsigned:
%hu, %i, %lu, %llu

---

float: 4 bajty
double: 8 bajtów
long double: 8/12/16 B (wielokrotnoœci dwójki, zale¿y od kompa)

printf();
%f, %Lf

---

type array_name[quantity] = {..., ..., ...};

---

rzutowanie:
z typu mniejszego na wiêkszego -> spoko

double x;
float y = 1.2f;         f <- float, L <- long double
x = y;
ale! x != 1.2

---

konwersja na mniejszy typ:

int x = 257;
char z;
z = x;          // -> z = 1
0x00000101 <- zapis szesnastkowy, zapis liczby 257
0x000000FF -> z = -1

zmniejszamy rozmiar danych, kompilator nie zg³osi b³êdu

char z = -1
int x = z
x -> -1

---

long long int x = 1024 * 1024 * 1024 * 4; -> wychodzi poza zakres inta
printf("%lld", x); // -> 0
1024lld <- wtedy kompilator rozumie, ¿e to typ long long int

*/