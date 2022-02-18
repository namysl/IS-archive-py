#include <stdio.h>
#include <math.h>

unsigned long long n;
unsigned pierwiastek, p, k;

int main(){
    scanf("%llu", &n);

    if (n < 4){
        return n;
    }
    else{
        p = 2;
        pierwiastek = sqrt(n);

        for (p=2; p <= pierwiastek; p++){
            //p^k | n
            k = 0;

            while (n % p == 0){
                k++;
                n /= p;
            }

            if (k > 0){
                if (k > 1){
                    printf("%u^%u*", p, k);
                }
                else{
                    printf("%u*", p);
                }
            }
        }

        if (n>1){
            printf("%llu", n);
        }
        else{
            printf("\b ");
        }
    }
}
