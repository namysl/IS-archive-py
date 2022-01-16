#include <stdio.h>
#include <string.h>

int main(){

    char zdanie[200];

    char array[126]; // wyzerowac
    for (int x=0; x <126; x++){
        array[x] = 0;
    }

    printf("Podaj zdanie: ");
    scanf("%[^\n]s", zdanie);

    size_t len = strlen(zdanie);


    int i = 0;
    do {
        //printf("%c %i\n", zdanie[i], zdanie[i]);
        array[(int)zdanie[i]] += 1;
        i++;

    } while (i < len);

    /*
    printf("Tablica 126: \n");
    for (int x=0; x <126; x++){
        printf("%i ", array[x]);
    }
    */

    printf("Len wprowadzonego stringa: %d\n", len);
    for (int x=32; x<126; x++){
        float procent = (100 * array[x])/len;
        printf("WARTOSC: %d SYMBOL: %c ILE RAZY: %d PROCENT: %f %%\n", x, x, array[x], procent);
    }

    return 0;
}
