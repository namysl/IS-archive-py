#include <stdio.h>

#define wiekszaz3(x, y, z) ((x)<(y)) ? ((y)<(z) ? (z) : (y)) : ((x) < (z) ? (z) : (x))

#define wiekszaz3v2(x, y, z)\
    {\
    int m = x;\
    if(m<y) m = y;\
    if(m<z) m = z;\
    printf("Wieksza z 3 liczb to %d", m);\
    }

int main(){
    int k, m, n;
    printf("Podaj 3 liczby calkowite: ");
    scanf(" %d %d %d", &k, &m, &n);
    printf("Wieksza z 3 liczb to (v1): %d\n", wiekszaz3(k, m, n));
    wiekszaz3v2(k, m, n);

    return 0;
}