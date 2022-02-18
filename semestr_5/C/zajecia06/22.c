#include <stdio.h>
#include <string.h>

char lancuch1[128];
char lancuch2[128];

int main(){

    printf("Pisz:\n");
    //wczytaj zdanie do lancucha1

    for(int i=0; i<128; i++){
        lancuch1[i] = getchar();
        if (lancuch1[i] == '\n'){
            lancuch1[i] = 0;
            break;
        }
    }

    //scanf("%[^\n]128s", lancuch1;

    //odnalezc ostatnia kropke
    char* pozycja = strrchr(lancuch1, '.');

    //pozycja to wskaznik
    if (pozycja){
        //skopiowac do lancuch2 od 0 do kropki
        strncpy(lancuch2, lancuch1, pozycja-lancuch1+1);
        lancuch2[pozycja-lancuch1+1] = 0;
    }
    else{
        strcpy(lancuch2, lancuch1);
    }

    printf("Len lancuch2: %lu\n", strlen(lancuch2));

    printf("%s\n", lancuch2);

    //zerowanie lancuch2
    lancuch2[0] = 0;

    //wyodrebnic cyfy z lancuch1 i zapisac je do lancuch1

    char cyfry[] = "1234567890";
    size_t poczatek = 0;
    size_t koniec;
    size_t dlugosc2 = 0;

    while(1){
        poczatek += strcspn(lancuch1+poczatek, cyfry);
        if (poczatek==strlen(lancuch1)){
            break;
        }
        koniec = strspn(lancuch1+poczatek, cyfry);
        strncpy(lancuch2+dlugosc2, lancuch1+poczatek, koniec);
        dlugosc2 += koniec;
        poczatek += koniec;
    }
    lancuch2[dlugosc2] = 0;

    printf("%s\n", lancuch2);

    return 0;
}
