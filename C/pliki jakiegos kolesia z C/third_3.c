#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <ctype.h>
#include <math.h>

int main()
{
    int x = 1;
    int y = 0;
    printf("  x | f(x) \n");
    while (x < 11) {
        y = 2*pow(x,2) - 30*x + 10;
        printf("%3d | %4d \n", x, y);
        x += 1;
    }



}
