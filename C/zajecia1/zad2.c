#include <stdio.h>

unsigned ilosc_mnozen = 0;
unsigned char x = 1;

// program, który wylicza pojemnoœæ unsigned char

void main() {
	while (x != 0) {
		x = x * 2;
		ilosc_mnozen++;
	}

	printf("zakres: 2^%hhu", ilosc_mnozen);
}
