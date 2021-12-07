#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdarg.h>

char* intdochar(int n){
    static char tekst[12];
    char czyujemna=0;

    if(n<0){
        czyujemna = 1;
        n-=n;
    }

    tekst[11]=0;
    int i=10;

    do{
        tekst[i]='0'+(n%10);
        n/=10;
        i--;
    }while(n!=0);
    
    if(czyujemna){
        tekst[i]='-';
    }
    else{
        i++;
    }
    return (tekst+i);
}

void print(char* lancuch,...){
    va_list argumenty;
    va_start(argumenty, lancuch);
    char c;
    while(1){
        c=lancuch[0];
        if(c==0){
            break;
        }
        if(c!='%'){
            putchar(c);
        }
        else{
            lancuch++;
            switch(lancuch[0]){
                case '%': 
                    putchar('%');
                    break;
                case 'c': 
                    c = va_arg(argumenty, int);
                    putchar(c);
                    break;
                case 's':{
                    char* wsk = va_arg(argumenty, char*);
                    while(*wsk != 0){
                        putchar(*wsk);
                        wsk++;
                    }
                    break;}
                case 'd':{
                    int n = va_arg(argumenty, int);
                    char* wsk = intdochar(n);
                    while(*wsk != 0){
                        putchar(*wsk);
                        wsk++;
                    }
                    break;}
            } //koniec switch
        } //koniec else
    
    lancuch++;    
    } //koniec while
va_end(argumenty);
} //koniec print

int main()
{
    print("123 asd\n"); //123 asd
    print("aaa %d\n",123); //aaa 123
    print("bbb %c\n",'p'); //bbb p
    print("ccc %s\n","tekst"); //ccc tekst
}
