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

    int kostka[10] = {218, 196, 196, 196, 191,
                      192, 196, 196, 196, 217};

    int parzyste[15] = {179, 42, 32, 42, 179,
                       179, 42, 32, 42, 179,
                       179, 42, 32, 42, 179};

    int nieparzyste[15] = {179, 42, 32, 42, 179,
                          179, 32, 42, 32, 179,
                          179, 42, 32, 42, 179};


    for(int x=0; x<5; x++){
        printf("%c", kostka[x]);
    }
    printf("\n");

    int licznik = 0;

    if (liczba % 2 == 0){
        switch(liczba) {
            case 2:
                for (int x=0; x<15; x++){
                    if(x==3 || x==6 || x==8 || x==11){
                        printf(" ");
                    }
                    else{
                        printf("%c", parzyste[x]);
                    }
                    licznik++;

                    if (licznik==5){
                        printf("\n");
                        licznik = 0;
                    }
                }
                break;

            case 4:
                for (int x=0; x<15; x++){
                    if(x==6 || x==8){
                        printf(" ");
                    }
                    else{
                        printf("%c", parzyste[x]);
                    }
                    licznik++;

                    if (licznik==5){
                        printf("\n");
                        licznik = 0;
                    }
                }
                break;

            case 6:
                for (int x=0; x<15; x++){
                    printf("%c", parzyste[x]);
                    licznik++;

                    if (licznik==5){
                        printf("\n");
                        licznik = 0;
                    }
                }
                break;
        }
    }

    if (liczba % 2 == 1){
        switch(liczba){
            case 1:
                for (int x=0; x<15; x++){
                    if(x==1 || x==3 || x==11 || x==13){
                        printf(" ");
                    }
                    else{
                        printf("%c", nieparzyste[x]);
                    }
                    licznik++;

                    if (licznik==5){
                        printf("\n");
                        licznik = 0;
                    }
                }
                break;

            case 3:
                for (int x=0; x<15; x++){
                    if(x==3 || x==11){
                        printf(" ");
                    }
                    else{
                        printf("%c", nieparzyste[x]);
                    }
                    licznik++;

                    if (licznik==5){
                        printf("\n");
                        licznik = 0;
                    }
                }
                break;

            case 5:
                for (int x=0; x<15; x++){
                    printf("%c", nieparzyste[x]);
                    licznik++;

                    if (licznik==5){
                        printf("\n");
                        licznik = 0;
                    }
                }
                break;
        }
    }

    for(int x=5; x<10; x++){
        printf("%c", kostka[x]);
    }

    printf("\n");
}
