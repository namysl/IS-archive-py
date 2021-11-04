#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(){
    int m = 1;  // zakres od (oczka kostki)
    int n = 6;  // zakres do

    do {
        srand(time(0));
        int liczba = m + (rand() % (n+1-m));

        printf("Wylosowano: %i\n", liczba);
        rysuj(liczba);
        char user_input[10];
        printf("k+enter to end\n");
        scanf("%c", user_input);

        if (user_input[0] == 'k'){
            break;
        }
    } while (1);

    return 0;
}


void rysuj(int liczba){
    //int ascii[6] = {218, 191, 192, 217, 196, 179};

    int kostka[25] = {218, 196, 196, 196, 191,
                      179, 32, 32, 32, 179,
                      179, 32, 32, 32, 179,
                      179, 32, 32, 32, 179,
                      192, 196, 196, 196, 217};

    int parzyste[9] = {42, 32, 42,
                       42, 32, 42,
                       42, 32, 42};

    int nieparzyste[9] = {42, 32, 42,
                          32, 42, 32,
                          42, 32, 42};

    int licznik = 0;
    for(int x=0; x<25; x++){
        licznik++;
        printf("%c", kostka[x]);

        if (licznik == 5){
            printf("\n");
            licznik = 0;
        }
    }


    for(int x=0; x<5; x++){
        printf("%c", kostka[x]);
    }
    printf("\n");
    if (liczba % 2 == 0){
        for(int x=0; x<9; x++){
        printf("%c", parzyste[x]);
        }
    }
    if (liczba % 2 == 1){
        for(int x=0; x<9; x++){
        printf("%c", nieparzyste[x]);
        }
    printf("\n");
    }
    for(int x=20; x<25; x++){
        printf("%c", kostka[x]);
    }

    /*
    printf("%c%c%c%c%c\n", ascii[0], ascii[4], ascii[4], ascii[4], ascii[1]);
    printf("%c   %c\n", ascii[5], ascii[5]);
    printf("%c * %c\n", ascii[5], ascii[5]);
    printf("%c   %c\n", ascii[5], ascii[5]);
    printf("%c%c%c%c%c\n\n", ascii[2], ascii[4], ascii[4], ascii[4], ascii[3]);
    */

}

//          *           *           * *         * *      * *
//  *                    *                       *       * *
//            *           *         * *         * *      * *
