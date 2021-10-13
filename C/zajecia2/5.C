
#include <stdio.h>

int main(){

unsigned licznik=0;
bool czy_spacja = true;
char znak;

do {
    znak = getchar();

    if (znak == ' '){
        if (!czy_spacja){
            putchar(' ');
        }
        czy_spacja = true;
    }
    else if (czy_spacja) {
        if (znak <= 'z' && znak >= 'a'){
            znak += 'A' - 'a';
        }

        czy_spacja = false;
        putchar(znak);
        licznik++;
    }
    else {
        putchar(znak);
    }

}
while (znak != '\n');

//printf("licznik: %i\n", licznik);
    return 0;
}
