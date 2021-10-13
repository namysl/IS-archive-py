#include <stdio.h>

// program, który wyświetla rzutowanie typu rzeczywistego (double) na całkowity (int), a następnie wyświetla część po przecinku tej liczby rzeczywistej
// jeżeli liczba wykracza poza zakres int, to należy wyœwietlić wartość maksymalną dla int, analogicznie dla wartości minimalnej

//double x = 1234.22;
int y;
float reszta;

void main() {
	printf("Podaj double x:\n");
	double x;
	scanf("%lf", &x);

	y = x;
	reszta = x - y;

	if (y > 2147483647) {
		printf("max: +2147483647\n");
	}

	else if (y < (-2147483648)) {
		printf("min: -2147483648\n");
	}

	else {
		printf("int y: %d\nfloat reszta: %f\n", y, reszta);
	}
}
