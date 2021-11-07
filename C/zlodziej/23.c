#include <stdio.h>
#include <stdlib.h>

int nwd(int a, int b){
    int c;
    while ((a % b) != 0) {
        c = a % b;
        a = b;
        b = c;
    }
    return b;
}

void skr(int *licz, int *mian){
    int c;
    c = nwd(*licz, *mian);
    *licz = (*licz / c);
    *mian = (*mian / c);
}

int main() {
    int l;
    int m;
    printf("Podaj l: \n");
    scanf(" %d", &l);
    printf("Podaj m: \n");
    scanf(" %d", &m);

    skr(&l, &m);
    printf("licznik: %d \n", l);
    printf("mia: %d \n", m);
}
