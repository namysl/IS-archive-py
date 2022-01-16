#include <stdio.h>


typedef struct dataigodzina{
    /* IDEALNIE:
    rok 14 bitow
    miesiac 4bity
    dzien 5bitow
    godzina 5bitow
    minuta 6bitow
    sekunda 6bitow

    = 26+14 = 40bitow
    */

    //char rok:14; //tak sie nie da
    short dzien:5;
    short godzina:5;
    short minuta:6;
    //to zajmuje 1 shorta
    short sekunda:6;
    short miesiac:4;
    //to nie zajmuje calego shorta
    short rok;
    //rok wypelnia caly 1 short

} dataigodzina;


int main(){


    return 0;
}
