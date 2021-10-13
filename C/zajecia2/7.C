#include <stdio.h>

int liczba_top = 128;
int liczba_mid = 64;
int liczba_bot = 1;
char odp;

int main() {

    do {
        printf("%i ?\n", liczba_mid);
        odp = getchar();
        getchar();

        if (odp == '<') {
            liczba_top = liczba_mid;
        }
        else if (odp == '>') {

            liczba_bot = liczba_mid;
        }
        liczba_mid = (liczba_top + liczba_bot) / 2;

    } while (odp != '=');

printf("Szukana liczba to: %i\n", liczba_mid);

return 0;
}


