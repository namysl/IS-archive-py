#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void wyswietl(double *A, unsigned n){
    int nn = 0;

    for (int i=0; i<n; i++){
        for (int j=0; j<n; j++){
            printf(" %2.1f", A[n*i+j]);
            nn++;

            if (nn == (int) n){
                printf("\n");
                nn = 0;
            }
        }
    }
}


double wyznacznik(double* A, unsigned n){
    if (n==2){
        return (A[0]*A[3]-A[1]*A[2]);
    }
    else{
        double suma = 0;
        for(int j=0; j<n; j++){
            double* Aj = (double*) malloc((n-1)*(n-1)*sizeof(double));
            if(Aj){
                int wiersz = 0;
                for(int i=0; i<n; i++){
                    if (i==j){
                        continue;
                    }
                    for(int k=0; k<n-1; k++){
                        Aj[wiersz*(n-1)+k] = A[n*i+k];
                    }

                }
                wiersz++;
                if ((n+j+1)&1){
                    suma -= A[n*j+n-1] * wyznacznik(Aj, n-1);
                }
                else{
                    suma += A[n*j+n-1]*wyznacznik(Aj, n-1);
                }
            }
            else{
                printf("Za malo pamieci\n");
                suma=0;
                break;
            }
        }//koniec for
        return suma;
    }
}


int main(){
    unsigned n;

    printf("Podaj n: ");
    scanf(" %u", &n);

    if (n>1){
        double *M = (double*) malloc(n*n*sizeof(double));

        if (M){
            srand(time(0));
            for(int i=0; i<n; i++){
                for(int j=0; j<n; j++){
                    M[n*i+j] = rand() % 10;
                }
            }

            wyswietl(M, n);
            printf("Wyznacznik: %f\n", wyznacznik(M, n));
        }
        else{
            printf("Za malo pamieci");
        }
    }
    else{
        printf("n<=1");
    }

    return 0;
}
