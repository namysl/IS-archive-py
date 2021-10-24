#include <stdlib.h>
#include <string.h>

int main(){
    int n = 128;
    char *first = (int*) malloc(n);
    char *second = (int*) malloc(n);
    int k = 0;
    memset(first, 0, n);
    scanf("%128s", first);
    char *c = strrchr(first, '.');
    if (c != 0){
        k = c - first;
    } else {
        k = strlen(first);
    }
    printf("%d \n", k);
    strncpy(second, first, n);
    memset(second, 0, n);
    printf("%s \n", second);
    printf("%d \n", strlen(second));


}
