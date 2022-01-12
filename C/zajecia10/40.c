#include <stdio.h>
#include <stdlib.h>

typedef struct wezel{
    char nazwa[16];
    struct wezel *lewy, *prawy;
}wezel;

wezel* korzen;


void utworz_losowe_drzewo(unsigned cos){
    printf(":O");
}


void dodaj_wezel(wezel* nadwezel){
    static unsigned nr=0;
    wezel *nowy = (wezel*)malloc(sizeof(wezel));

    if(nowy){
        nowy->nazwa[0] = nr+'a';
        nowy->nazwa[1] = 0;
        nowy->lewy = 0;
        nowy->prawy = 0;

        nr++;

        if(nadwezel){
            if(nadwezel->lewy){
                if(nadwezel->prawy){
                    printf("nadwezel ma juz oba podwezly");
                    free(nowy);
                }
                else{
                    nadwezel->prawy = nowy;
                }
            }else{
                nadwezel->lewy = nowy;
            }
        }else{
            if(korzen==0){
                korzen = nowy;
            }
            else{
                free(nowy);
                printf("free(nowy)");
            }
        }
    }
}


//zakladamy, ze pierwszy jest nad wezlem drugiego
int odleglosc_miedzy_wezlami(wezel *pierwszy, wezel *drugi){  //drugi jest staly
    int l1 = -1;
    int l2 = -1;


    if (pierwszy == drugi){
            return 0;
    }

    if (pierwszy->lewy){
        l1 = odleglosc_miedzy_wezlami(pierwszy->lewy, drugi);
    }

    if(pierwszy->prawy){
        l2 = odleglosc_miedzy_wezlami(pierwszy->prawy, drugi);
    }

    if (l1 >= 0){
        return (l1+1);
    }

    if (l2 >= 0){
        return (l2+2);
    }

    return -1;
}


int main(){

    dodaj_wezel(0);
    dodaj_wezel(korzen);
    dodaj_wezel(korzen);
    dodaj_wezel(korzen->lewy);
    dodaj_wezel(korzen->prawy);
    dodaj_wezel(korzen->prawy);
    dodaj_wezel(korzen->prawy->lewy);

    printf("%d", odleglosc_miedzy_wezlami(korzen, korzen->prawy->lewy));

    return 0;
}


//egzamin po 6/02
