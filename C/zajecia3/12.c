#include <stdio.h>

int main(){
    int x;

    for(x=1; x<=10; x++){
        printf("| %6d |\n", y(x));
    }
    return 0;
}


int y(x){
    return 2*x*x - 30*x + 10;
}
