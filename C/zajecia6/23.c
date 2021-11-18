#include <stdio.h>

int main(){
    int licznik;
    int mianownik;

    printf("Podaj licznik: ");
    scanf(" %d", &licznik);
    printf("Podaj mianownik: ");
    scanf(" %d", &mianownik);

    if (mianownik != 0){
        skroc(&licznik, &mianownik);
        printf("licznik: %d, mianownik: %d\n", licznik, mianownik);
    }

    return 0;
}

int nwd(int a, int b){
    while(b != 0){
        int r=a%b;
        a=b;
        b=r;
    }
    //printf("%d", a);
    return a;
}

void skroc(int *licznik, int *mianownik){
    int r = nwd(*licznik, *mianownik);
    *licznik /= r;
    *mianownik /= r;
}

