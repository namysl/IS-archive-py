#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#define mini 0x00000000
#define maks 0x7fffffff
int main()
{
    // first
    int i;
    char napis[] = "\n\r\t\b\a\f\"\'\\";
    for (i=0; i < sizeof(napis); i++) {
        int numer_znaku = (int) napis[i];
        int znak = napis[i];
        printf("Znak o wartości %d, wyświtla się %c tak \n", numer_znaku, znak);
    }

    //second
    unsigned int a = -1;
    unsigned char c = -1;
    unsigned short s = -1;
    unsigned long l = -1;
    unsigned long long ll = -1;

    printf("unsigned int %u \n unsigned char %hhu \n unsigned short %hu \n unsigned long %lu \n unisgned long long %llu \n", a, c, s, l, ll);

    //third
    /*
    float new_a;
    int rzut_a;

    scanf("%f", &new_a);

    if(new_a < -maks) {
        printf("%d", -maks);
    } else if (new_a > maks) {
        printf("%d", maks);
    } else {
        rzut_a = (int) new_a;
        printf("%d, %f", rzut_a, new_a-rzut_a);
    }
    */
    //fourth
    /*
    char z;
    unsigned short il = 0;
    bool spac = true;

    do {
        z = getchar();
        if (z == ' ') {
            spac = true;
        } else if((spac == true) && (z != '\n')) {
            spac = false;
            il++;
        }

    } while (z != '\n');

    printf("%hu", il);
    */
    //fifth
    char z;
    bool spac = true;
    do {
        z = getchar();
        if ((spac == true) && (z != ' ')){
            printf("%c", toupper(z));
            spac = false;
        } else if ((z == ' ') && (spac == false)) {
            printf("%c", z);
            spac = true;
        } else if ((z != ' ') && (spac == true)) {
            printf("%c", z);
            spac = false;
        } else if ((spac == false) && (z != ' ')) {
            printf("%c", z);
            spac = false;
        }


    } while(z != '\n');


    return 0;
}
