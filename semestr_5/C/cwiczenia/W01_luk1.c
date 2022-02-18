#include <stdio.h>

int main() {
    char znak;

    puts("Wpisz zdanie:\n");

    do {
        znak = getchar();
        putchar(znak);
    } while(znak != '\n');
    return 0;
}
