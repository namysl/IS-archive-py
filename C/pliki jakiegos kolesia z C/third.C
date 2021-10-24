#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
int main()
{
char c;
int i;
c = getchar();
while (c != EOF){
    i+= 1;
    putchar(c);
    c = getchar();
    if (i == 8) {
        putchar('\n');
        i = 0;
    }
}




}
