#include <stdio.h>
#include <stdlib.h>
int main() {
    int x;
    int n;
    scanf("%d", &n);
    int string[n];
    int y;
    char *str;
    str = (char*)malloc(10);
    printf("%p, %p, %p", &x, &y, &str);
}
