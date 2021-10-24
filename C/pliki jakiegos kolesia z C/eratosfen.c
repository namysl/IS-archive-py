#include <stdio.h>

main() { 
    int n;    
    scanf("%d", &n);
    char g[n];
    int i = 2;
    int z = 1;
    int a = n;
    int r = 0;

    g[0] = 1;
    g[1] = 2;

    for (int i = 2; i < n; i++) {
        for (int k = 1+i; k < a; k++) {
            printf("%d \n", k);
            if ((k % g[i]) != 0) {
               printf("%d", k);
               g[i-1] = k;
               r += 1;
            }
            a = r;
            r = 0;
        }
    }

    for (int i = 0; i < a; i++){
        printf("%d", g[i]);
    }

}
