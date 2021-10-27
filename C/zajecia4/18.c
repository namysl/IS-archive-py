#include <stdio.h>
#include <stdlib.h>
#include <time.h>


int main(){
    int m = 1;
    int n = 6;

    int array[9];
    //osobno parzyste, osobno nieparzyste
    //5, 3, 1
    //6, 4, 2


    do {

        srand(time(0));
        int liczba = m + (rand() % (n+1-m));

        printf("Wylosowano: %i\n", liczba);

        char user_input[10];
        printf("k+enter to end\n");
        scanf("%c", user_input);

        if (user_input[0] == 'k'){
            break;
        }

    } while (1);

    int arr[6] = {218, 191, 192, 217, 196, 179};

    for (int x=0; x<6; x++) {
        printf("%c ", arr[x]);
    }

    return 0;
}


//          *           *           * *         * *      * *
//  *                    *                       *       * *
//            *           *         * *         * *      * *
