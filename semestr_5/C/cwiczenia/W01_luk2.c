#include <stdio.h>
int main() {
    char napis[16];
    puts ("Wpisz zdanie:\n");
    fgets(napis, 16, stdin);
    printf("%s\n", napis);

    fflush(stdin);

    fgets(napis, 16, stdin);
    printf("%s\n", napis);

    return 0;
}
