#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <ctype.h>
#include <time.h>
int main()
{
    char c;
    int r;
    //printf("+---------+\n");
    //printf("|  *      |\n");
    //printf("|    *    |\n");
    //printf("|      *  |\n"); 
    //printf("+---------+\n");

    srand(time(0));
    printf("Print symbol to get a random number\n");
    do {
        r = (rand() % 6) + 1;
        printf("+---------+\n");
        switch(r){
        case 1:
            printf("|         |\n");
            printf("|    *    |\n");
            printf("|         |\n");
            break;
        case 2:
            printf("|  *      |\n");
            printf("|         |\n");
            printf("|      *  |\n");
            break;
        case 3:
            printf("|  *      |\n");
            printf("|    *    |\n");
            printf("|      *  |\n");
            break;
        case 4:
            printf("|  *   *  |\n");
            printf("|         |\n");
            printf("|  *   *  |\n");
            break;
        case 5:
            printf("|  *   *  |\n");
            printf("|    *    |\n");
            printf("|  *   *  |\n");
            break;
        case 6:
            printf("|  *   *  |\n");
            printf("|  *   *  |\n");
            printf("|  *   *  |\n");
            break;
        }
        printf("+---------+\n");
        scanf(" %c", &c);
    } while (c != 'k');

}
