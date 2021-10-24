#include <stdio.h>
#include <string.h>
#include <stdarg.h>
#include <stdlib.h>


typedef struct wezel{
    int number;
    struct wezel_ *lewy, *prawy;
}wezel;

wezel *korzen;


unsigned liscie(wezel *korzen){
    if (korzen==0) return 0;
    if (korzen->lewy == 0)
        return 1;
    unsigned ilelisci=liscie(korzen->lewy);
    return ilelisci;
}

void wspolnywezel(wezel *jeden, wezel *dwa){
    int t1[100];
    int t2[100];
    int a=0;
    int b=0;
    int t;

    t=droga(jeden,korzen);
    while (droga!=korzen){
        t1[a]=t;
        t=droga(t);
    }
    t=droga(dwa,korzen);
    while (droga!=korzen){
        t2[b]=t;
        t=droga(t);
    }
    for(a;a>0;a--){
        for(b;b>0;b--){
            if (t1[a]==t2[b])
                return t1[a];
        }
    }
}

void droga(wezel *aktualny, wezel *korzen){

    if (korzen){
        wezel *temp;
        if (korzen->lewy == aktualny || korzen->prawy == aktualny)
            return korzen;
        temp = droga(aktualny, korzen->lewy);
        if (temp)
            return temp;
        temp=droga(aktualny,korzen->prawy);
        if (temp)
            return temp;

    }

}

int main(){


}
