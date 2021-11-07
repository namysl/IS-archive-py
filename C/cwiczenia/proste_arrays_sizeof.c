#include <stdio.h>

int main() {
    char x = 'l';
    printf("size of int: %lu\n", sizeof(int));
    printf("size of x variable: %lu\n\n", sizeof(x));

    int array[] = {1, 2, 3, 4, 5, 6};

    printf("number of elements in the array: %lu\n", sizeof(array)/sizeof(array[0]));
    printf("first element: %lu\nand second: %lu\n", sizeof(array[0]), sizeof(array[1]));
    printf("size of the array: %lu\n\n", sizeof(array));

    double double_array[] = {1.0, 2.0, 3.0};
    printf("double array: %lu\n", sizeof(double_array)/sizeof(double_array[0]));
    printf("first element: %lu\nand array: %lu\n\n", sizeof(double_array[0]), sizeof(double_array));

    char char_array[] = {'a', 'b', 'c', '\0'};
    printf("char array: %lu\n", sizeof(char_array)/sizeof(char_array[0]));
    printf("first element: %lu\nand array: %lu\n\n", sizeof(char_array[0]), sizeof(char_array));
    printf("char_array: %s\n", char_array); // %s!!!!!!!!!!!!!!!!

    char inna_tablica[] = "no siema";
    printf("inna_tablica: %s\n", inna_tablica);

    char podwojna[4][7] = {"cos", "cos2", "cos3", "cosik5"};  //[7] = len najwiekszego stringa + 1

    for (int i=0; i<4; i++){
        printf("podwojna: %s Adres pamieci unsigned int: %u Adres pamieci hex: %p\n", podwojna+i, podwojna+i, podwojna+i);
    }

    printf("ile elementow w 2d array: %lu\n", sizeof(podwojna)/sizeof(podwojna[0]));
    printf("pierwszy: %lu, tablica: %lu\n\n", sizeof(podwojna[0]), sizeof(podwojna));


    char iks = 'x';
    printf("rozmiar iks: %lu\n", sizeof(iks));

    char es = 's';
    printf("liczba pod s -> %%i: %i, %%d: %d\n", es, es);

    int liczba = 16;
    printf("%i, %o, %x", liczba, liczba, liczba);
    return 0;

}

