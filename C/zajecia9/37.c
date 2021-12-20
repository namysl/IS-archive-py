#include <stdio.h>
#include <stdlib.h>

typedef struct wielomian{
    unsigned stopien;
    float *wsp; //wskaznik na wspolczynniki

}wielomian;


int nowy_wielomian(wielomian P){
    printf("Podaj stopien wielomianu: ");
    scanf(" %u", &(P.stopien));

    printf("Podaj wspolczynniki poczawszy od najwyzszego: ");

    P.wsp = (float*)malloc ((P.stopien+1)*sizeof(float));
    if(P.wsp){
        for(int i=0; i<=P.stopien; i++){
            scanf(" %f", &(P.wsp[i]));
        }
    }
    else{
        printf("Brak wolnej pamieci");
        return 1;
    }
    return 0;
}


void zwolnij_wielomian(wielomian P){
    free(P.wsp);
}


float wartosc_w_punkcie(wielomian P, float x){
    float w = P.wsp[P.stopien];
    for(int i=P.stopien-1; i>=0; i--){
        w = w*x + P.wsp[i];
    }
    return w;
}


int dodaj_wielomian(wielomian P, wielomian Q, wielomian R){
    //R = P + Q
    //R nie jest zainicjowane

    if(P.stopien == Q.stopien){
        R.stopien = P.stopien;
        for (int i=P.stopien; i>=0; i--){
            if(P.wsp[i] + Q.wsp[i] == 0){
                R.stopien--;
            }
            else{
                break;
            }
        }
    }
    else{
        R.stopien = P.stopien;
        if(P.stopien < Q.stopien){
            R.stopien = Q.stopien;
        }
    }

    R.wsp = (float*)malloc( (R.stopien+1) * sizeof(float));

    if(R.wsp){
        unsigned m = R.stopien;
        if (m > P.stopien){
            m=P.stopien;
        }
        for (int i=m; i>=0; i--){
            R.wsp[i] == P.wsp[i] + Q.wsp[i];
        }
        for(int i=P.stopien; i>m; i--){
            R.wsp[i] = P.wsp[i];
        }
        for(int i=Q.stopien; i>m; i--){
            R.wsp[i] = Q.wsp[i];
        }
    }
    else{
        printf("Brak pamieci");
        return 1;
    }
    return 0;
}

int mnoz_wielomiany(wielomian P, wielomian Q, wielomian R){
    // R = P * Q
    // R nie jest zainicjalizowany

    R.stopien = P.stopien + Q.stopien;
    R.wsp = (float*)malloc((R.stopien+1) * 4);

    if(R.wsp){
        for(int i=R.stopien; i>=0; i--){
            R.wsp[i] = 0;
        }
        for(int i=P.stopien; i>=0; i--){
            for(int j=Q.stopien; j>=0; j--){
                R.wsp[i+j] += P.wsp[i] * Q.wsp[j];
            }
        }
    }
    else{
        printf("Brak pamieci");
        return 1;
    }
    return 0;
}


int main(){

    wielomian przyklad;
    nowy_wielomian(przyklad);

    return 0;
}
