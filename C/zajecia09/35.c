#include <stdio.h>

typedef struct int128{

    unsigned long long gorna;  //64 bity
    unsigned long long dolna;  //64 bity

}int128;


/*
    1011 0100 = -76 (pierwszy bit to znak)
    0011 1001 =  57
    1110 1101 = wynik dodawania to -19 (237)

*/

int128 dodaj(int128 x, int128 y){

    int128 z;
    z.dolna = x.dolna + y.dolna;

    if (z.dolna < x.dolna){ // jest przepelnienie
        z.gorna = 1;
    }
    else{
        z.gorna = 0;
    }

    z.gorna += x.gorna + y.gorna;

    return z;
}

    // x*y= (x.gorna*2^64 + x.dolna) * (y.gorna*2^64 + y.dolna) =
    // = x.gorna * y.gorna * 2^128  <- overflow
    // + 2^64 * (x.gorna * y.dolna + y.gorna * x.dolna)  <- gorna czesc
    // + x.dolna * y.dolna  <- dolna czesc

    //x.dolna xdg xdd (32 bity, 32 bity)
    //y.dolna ydg ydd

    //x.dolna * y.dolna = xdg*ydg * 2^64 + (xdg * ydd * ydg * xdd)* 2^64 + xdd * ydd


int128 mnoz(int128 x, int128 y){

    int128 z, temp;
    char znak = 0;

    if (x.gorna < 0){
        znak++;
        x.gorna = -x.gorna;
        x.dolna = -x.dolna;
    }
    if (y.gorna < 0){
        znak++;
        y.gorna = -y.gorna;
        y.dolna = -y.dolna;
    }

    unsigned long long xdd, xdg, xgd, xgg, ydd, ydg, ygd, ygg;

    xdd = x.dolna & 0x0FFFFFFFF;
    ydd = y.dolna & 0x0FFFFFFFF;

    xgd = x.gorna & 0x0FFFFFFFF;
    ygd = y.gorna & 0x0FFFFFFFF;

    xdg = x.dolna >> 32;
    ydg = y.dolna >> 32;
    xgg = x.gorna; xgg >>= 32;
    ygg = y.gorna; ygg >>= 32;

    //x*y = 2^96*(xgg*ydd+xgd*ydg+xdg*ygd+xdd*ygg)
    //    + 2^64*(xgd*ydd+ygd*xdd+xdg*ydg)
    //    + 2^32*(xdg*ydd+xdd*ydg)
    //    + xdd*ydd

    z.gorna = (xdg*ydd) >> 32;
    z.dolna = xdg*ydd << 32;
    temp.gorna = (xdd*ydg) >> 32;
    temp.dolna = (xdd*ydg) << 32;
    z = dodaj(z, temp);

    temp.dolna = xdd * ydd;
    temp.gorna = 0;
    z = dodaj(z, temp);
    z.gorna += xgd * ydd + ygd * xdd + xdg * ydg;

    temp.gorna = xgg * ydd + xgd * ygd + xdg * ygd + xdd * ygg;
    temp.gorna <<= 32;
    z.gorna += temp.gorna;

    if(znak == 1){
        z.gorna |= 0x8000000000000000;
    }
    return z;
}


int main(){
    int128 liczba1;
    liczba1.gorna = 12345;
    liczba1.dolna = 67890;

    int128 liczba2;
    liczba2.gorna = 0;
    liczba2.dolna = 2;

    printf("%llu %llu\n", dodaj(liczba1, liczba2));
    printf("%llu %llu", mnoz(liczba1, liczba2));

    return 0;
}
