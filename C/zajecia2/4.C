#include <stdio.h>

int main(){

//    char slowa[10];
//    scanf("&s", slowa);

//    printf("%s\n", slowa);


unsigned licznik=0;
bool czy_spacja = true;
char znak;

do {
    znak = getchar();
    //printf("%c\n", znak);

    if (znak == ' '){
        czy_spacja=true;
    }
    else if (czy_spacja) {
        czy_spacja=false;
        licznik++;
    }
}
while (znak != '\n');


printf("licznik: %i\n", licznik);
    return 0;
}
