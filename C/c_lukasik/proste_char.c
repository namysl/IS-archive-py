#include <stdio.h>

int main(){

    int rok;
    printf("Podaj rok narodzin:\n");
    scanf("%i", &rok);

    char imie[50], nazwisko[50];

    printf("Podaj swoje imie:\n");
    scanf("%s", imie);

    printf("Podaj swoje nazwisko:\n");
    scanf("%s", nazwisko);

    printf("Twoje imie i nazwisko: %s %s. Masz %i lat.\n", imie, nazwisko, 2021-rok);

    char miasto[50];
    printf("Podaj swoje miasto: ");
    scanf("%s", miasto);

    char plec;
    printf("k/m? ");
    scanf(" %c", &plec);

    printf("miasto: %s, plec: %c\n", miasto, plec);

return 0;
}
