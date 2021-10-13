#include <stdio.h>

int n; // ilosc segmentow
int k; // numer segmentu -> 1, ..., n
int ik; // i-ty wiersz w segmencie
char spacja = ' ';
char gwiazdka = '*';
/*

   *
  ***
   *
  ***
 *****

*/

int main() {

    scanf("%i\n", n);

    for (k=1; k<=n; k++) {
        for (ik=1; ik<=k+1; k++) {
            // n+1-ik spacji + 2*ik-1 gwiazdek
            putchar('%c%c', spacja, gwiazdka);
            printf('\n');
        }
    }

    return 0;
}
