#include <stdio.h>
#include <stdlib.h>

int main(){

    unsigned rozmiar_bufora = 0;
    unsigned znakow_w_buforze = 0;
    char *bufor = 0;
    char znak;

    //user podaje zdanie
    //wczytujemy go znak po znaku
    do{
        znak = getchar();
        if (znak=='\n'){
            znak = 0;
        }
        //sprawdzic czy bufor jest wystarczajaco duzy,
        //jak nie, to relokowac pamiec
        if (znakow_w_buforze < rozmiar_bufora){
            bufor[znakow_w_buforze] = znak;
            znakow_w_buforze++;
        }
        else{
            printf("realokacja\n");
            if (bufor){
                char *tmp = (char*)realloc(bufor, rozmiar_bufora+16);

                ///////
                if (tmp){
                    bufor = tmp;
                    rozmiar_bufora += 16;
                    bufor[znakow_w_buforze] = znak;
                    znakow_w_buforze++;
                }
                else{
                    printf("za malo pamieci");
                    break;
                }
                ///////
            }
            else{
                bufor = (char*)malloc(16);
                if (bufor){
                    //cos podobnego do wyzej
                    rozmiar_bufora += 16;
                    bufor[znakow_w_buforze] = znak;
                    znakow_w_buforze++;
                }
                else{
                    printf("?");
                    break;
                }
            }
        }

    } while(znak != 0);

    return 0;
}
