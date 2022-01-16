#include <stdio.h>

int main(){
    char znak;
    char zdanie[128];

    printf("Podaj znak: ");
    scanf(" %c", &znak);
    fflush(stdin);
    printf("Podaj zdanie: ");
    scanf("%[^\n]s", zdanie);

    int licznik = 0;
    size_t len = strlen(zdanie);
    //printf("%d", len);

    for (int i=0; i <= len; i++){
        if (zdanie[i] == znak){
            licznik++;
        }
        else if (zdanie[i] == znak+32) {
            licznik++;
        }
    }

    printf("Ile znakow %c w zdaniu: %i\n", znak, licznik);
    return 0;
}
