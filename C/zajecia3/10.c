#include <stdio.h>
#include <string.h>

int main(){

/*
    char znak;
    printf("Podaj zdanie: ")
    do {
        znak = getchar();
        for (int i=0; i<8; i++){
            putchar(znak);
        }
        printf("\n");
    } while (znak != '\n');

    return 0;
}

*/

    char zdanie[200];

    printf("Podaj zdanie: ");
    scanf("%[^\n]s", zdanie);

    size_t len = strlen(zdanie);
    int i = 0;
    int licznik = 0;

    do{
        printf("%c ", zdanie[i]);
        i++;
        licznik++;

        if (licznik==8){
            licznik = 0;
            printf("\n");
        }

    } while (i < len);

    return 0;
}
