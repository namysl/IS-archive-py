#include <stdio.h>
#include <stdlib.h>

int main(){

	char adres1[] = "www.google.pl/maps/dir/Plonia,+47-253/Skalmierzyce,+63-460/";
	char cmd[256];

    sprintf(cmd, "START %s", adres1); //Windows
    sprintf(cmd, "firefox %s", adres1); //Linux
    system(cmd);


    char adres2[256];
    printf("Podaj url: ");
    scanf(" %s", adres2);

    sprintf(cmd, "START %s", adres2);
    sprintf(cmd, "firefox %s", adres1);
    system(cmd);

    return 0;
}
