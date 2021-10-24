#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <ctype.h>
int main()
{
char c;
char myc;
int i = 0;
int k = 0;
printf("Give me what you want to find: ");
myc = getchar();
printf("Give where you want to find: ");
c = getchar();
c = getchar();
while ((c != EOF) && (c != '\n')){
    if (c == myc) {
        i += 1;
    }

    if (tolower(c) == tolower(myc)) {
        k += 1;
    }

    c = getchar();

}
printf("%d \n", i);
printf("Insensetive: %d", k);
}
