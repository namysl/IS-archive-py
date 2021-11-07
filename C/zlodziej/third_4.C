#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <ctype.h>
int main()
{
    char z;
    double a;
    double b;
    double result = 0;

    scanf(" %c", &z);
    scanf(" %lf", &a);
    scanf(" %lf", &b);

    switch(z) {
    case '+':
        result = a+b;
        break;
    case '-':
        result = a-b;
        break;
    case '*':
        result = a*b;
        break;
    case '/':
        if (b == 0) {
            printf("NOOOO \n");
        }
        else {
            result = a/b;
        }
        break;
    default:
        printf("NOT VALID \n");
    }
    printf("%5.5lf", result);


}
