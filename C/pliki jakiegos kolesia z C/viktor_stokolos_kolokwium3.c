#include <stdio.h>
#include <string.h>
#include <stdarg.h>
#include <stdlib.h>

int scalaj(const char *lancuh, ...){
    int s = 200;
    char* l_lancuh = (char*)malloc(s*sizeof(char));
    int counter=0;
    va_list arg;
    va_start(arg, lancuh); 

    while (lancuh){
        strcpy(l_lancuh+counter, lancuh);
        if (counter +strlen(lancuh)){
            s += 200;
            realloc(l_lancuh, s*sizeof(char));
        }

        counter += strlen(lancuh);
        lancuh = va_arg(arg, const char *);
    } 
    free(l_lancuh);
    va_end(arg);

    return counter;
}

int dr(const char* lancuh, int f, int l){
    int* ind = &f;
    int* ind2 = &l;

    char const digit[] = "0123456789";

    char* max=0;
    char* el;

    (*ind) = strcspn(lancuh, "1234567890");

    for (int i = 0; i < 10; i++){
       el = strrchr(lancuh, digit[i]); 
       if (el > max){
           max = el;
       }
    }
    if (max != 0){
        (*ind2) = (max-lancuh);
    }
    if ((*ind) == strlen(lancuh) && ((*ind2) == 0)){
        return 0;
    }
    printf("%d, %d", *ind, *ind2);
}

void tre(char * lan) {
    char c;
    char new_lan[256];
    int j = 0;
    for (int i =0; i<strlen(lan);i++) {
        c = lan[i];

        if (isalpha(c) || c == ' ') {
            new_lan[j] = c;
            j++;
        }
    }
    new_lan[j+1]=0;
    printf("%s", new_lan);
}


int main(){
    printf("%d \n", scalaj("kek", "ne kek", "sowsem ne kek", NULL));
    int a = 0;
    int b = 0;
    dr("aa1bb2cc", a, b);
    printf("%d, %d", a, b);
    tre("asfd1qwer2wqe");
    
}
