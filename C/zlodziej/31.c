#include <stdio.h>
#include <stdlib.h>
typedef struct date {
   unsigned short rok:7;
   unsigned short miesiac:4;
   unsigned short dzien:5;
   unsigned short minuta:6;
   unsigned short sekunda:6;
   unsigned short godzina:5;
} date;
int main(){
    printf("%lu", sizeof(date));
    return 0;
}
