#include <stdio.h>

char gwiazdka=42;
char spacja=32;
int n=0;

int main() {
    printf("Podaj n: ");
    scanf("%d", &n);

	for (int i=2; i<=n; i++) {
		for (int j=1; j<=i; j++) {
			for (int k=0; k<(n-j); k++){
                putchar(spacja);
			}
            for (int p=0; p<(j*2-1); p++){
                putchar(gwiazdka);
            }
            printf("\n");
		}
	}

    return 0;
}

/*#include <stdio.h>

int n; // ilosc segmentow
int k; // numer segmentu -> 1, ..., n
int ik; // i-ty wiersz w segmencie
char spacja = 32;
char gwiazdka = 42;

/*
   *
  ***
   *
  ***
 *****
*/

/*
int main(){
    printf("Podaj n: ");
    scanf("%i\n", &n);

    for (k=2; k<=n; k++){
        for (ik=1; ik<=k; k++){
            for (int q=0; q<=n+1-ik; q++){
                putchar(spacja);
            }
            for (int w=0; w<=2*ik-1; w++){
                putchar(gwiazdka);
            }
            // n+1-ik spacji + 2*ik-1 gwiazdek

            printf("\n");
        }
    }

    return 0;
}
*/
