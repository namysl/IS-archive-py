#include <stdio.h>

union {
    unsigned int integer;
    unsigned char byte[4];
} bar;

int main(){
    bar.integer = 256;
    printf("%u %u %u %u\n", bar.byte[3], bar.byte[2], bar.byte[1], bar.byte[0]);
    return 0;
}
