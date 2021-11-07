#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef union rzeczywista {
    double liczba;
    struct {
       long long mantysa:52;
       long long wykladnik:11;
       long long znak:1;
    };
} rzeczywista;

typedef struct wyniki {
    float punkty;
    char nazwisko[16];
    char imie[16];
} wyniki;


int my_compare(const void *a, const void *b) {
    int _a = *(int*)a;
    int _b = *(int*)b;
    if (_a < _b) return 1;
    else if(_a == _b) return 0;
    else return -1;
}

void main(){
    rzeczywista x;
    printf("Proszę podać liczbę typu double: ");
    scanf(" %lf", &x.liczba);
    printf("znak: %d, mantysa: %ld, wykladnik: %d \n", -x.znak, x.mantysa, x.wykladnik);
    int size=2;
    wyniki *tab = (wyniki*)malloc(size*sizeof(wyniki));
    float pnkt = 0;
    char nazw[16];
    char im[16];
    for (int i=0; i<size; i++) {
        printf("Prosze podać punkty dla persony #%d \n", i+1);
        scanf(" %f", &pnkt);
        tab[i].punkty = pnkt;
        printf("Prosze podać nazwisko dla persony #%d \n", i+1);
        scanf(" %s", nazw);
        strcpy(tab[i].nazwisko, nazw);
        printf("Prosze podać imię dla persony #%d \n", i+1);
        scanf(" %s", im);
        strcpy(tab[i].imie, im);
    }
    qsort(tab, size, sizeof(wyniki), my_compare);
    for (int i=0; i<size; i++){
        printf("punkty: %f, imię: %s, nazwisko: %s \n", (tab+i)->punkty, (tab+i)->imie, (tab+i)->nazwisko);
    }
    FILE *plik;
    int len;
    plik = fopen("dane.txt", "w+");
    if (plik){
        for (int i=0; i<size; i++){
            fprintf(plik, "punkty: %f, imię: %s, nazwisko: %s \n", (tab+i)->punkty, (tab+i)->imie, (tab+i)->nazwisko);
        }
        fclose(plik);
    }

    plik = fopen("dane.txt", "r");
    char *line = NULL;
    size_t l = 0;
    ssize_t read;
    if (plik){
        while (read = getline(&line, &l, plik) != -1) {
            printf("%s", line);
        }
    }
    fclose(plik);
}
