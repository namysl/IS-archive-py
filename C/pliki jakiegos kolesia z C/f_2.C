#include <stdio.h>
#include <stdlib.h>
int main(){
    char *string;
    int i = 0;
    int rozmiar = 16;
    string = (char*)malloc(16);
    
    do{
        if (i == rozmiar){
            string = (char*)realloc(string, rozmiar+16);
            rozmiar += 16;
        }
        string[i] = getchar();
        i++;
    } while (string[i-1] != '\n');
    string[i] = 0;
    printf("%s", string);
}
