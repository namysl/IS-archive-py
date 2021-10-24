#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

#define BUZZ_SIZE 1024

int main(){
    char* some_string;
    scanf(" %s", some_string);
    printf("%s \n", some_string);
    if ((some_string) != "\n"){
        char buff[BUZZ_SIZE];
        FILE *f = fopen(some_string, "r");
        if (f == NULL){
            printf("NO");
            exit(1);
        }
        fgets(buff, BUZZ_SIZE, f);
        printf("String read: %s\n", buff);
        fclose(f);
    } else {
        time_t mytime = time(NULL);
        char * time_str = ctime(&mytime);
        time_str[strlen(time_str)-1] = '\0';
        printf("Current Time : %s\n", time_str);
    }
    return 0;    
}
