#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <ctype.h>
int main()
{
unsigned long z;
unsigned long long n, k, x;
char nastki[19][16] = {"jeden", "dwa", "trzy", "cztery", "pięć", "sześć", "siedem", "osiem", "dziwięć", "dziesięć",
                       "jedenaście", "dwanaście", "trynaście", "czternaście", "piętnaście", "szesnaście", "siedemnaście", "osiemnaście", "dziewiętnaście" }
char dwudziestki[8][20] = {"dwadzieścia", "trzydzieści", "czterdzieści", "pięćdziesiąt", "sześćdziesiąt", "siedemdziesiąt", "osiemdzieśiąt", "dizewięćdzieśiąt"}
char setki[9][16] = {"sto", "dwieście", "trzysta", "czterysta", "pięćset", "szesćset", "siedemset", "osiemset", "dziewięćset"}
char tysiace[][3][16]={{"tysiąc", "tysiące", "tysiący"}, {"million", "miliony", "milionów"}, {"bilion" "biliony", "bilionów"}}
if(n == 0) {
    printf("zero\n");
} else {
    k = 1;
    while (k*1000 <= n) {
        k *= 1000;
        z ++;
    }
    x = n/k;
    if (x/100 != 0) {
        printf("%s ", setki[x/100-1]);
    }
    if ((x/10) % 10 > 2)) {
        print( , setki[(x/10)%10])
        print( , nastki[()])
    }
}
}
