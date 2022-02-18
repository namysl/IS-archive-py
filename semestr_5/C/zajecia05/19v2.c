#include <stdio.h>
#include <stdlib.h>

unsigned rozmiar_bufora = 0;
unsigned znakow_w_buforze = 0;
char *bufor = 0;
char znak;


int main(){
    printf("Zdanie: ");
    do{
        znak = getchar();
        if (znak == '\n'){
            znak = 0;
        }
        if (znakow_w_buforze >= rozmiar_bufora){
            char *tmp = (char*) realloc(bufor, rozmiar_bufora+16);
            if (tmp){
                bufor = tmp;
                rozmiar_bufora += 16;
            }
            else{
                printf("za malo pamieci");
                znakow_w_buforze = 0;
                break;
            }
        }
        bufor[znakow_w_buforze] = znak;
        znakow_w_buforze++;
    } while(znak!=0);

    if (znakow_w_buforze > 0){
        printf("%s", bufor);
    }

    free(bufor);
    return 0;
}
