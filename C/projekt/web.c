#include <stdio.h>
#include <stdlib.h>

int main()
{
	char adres = "www.google.pl/maps/dir/Plonia,+47-253/Skalmierzyce,+63-460/";
	char cmd[256];

    sprintf(cmd, "START %s", adres);
    system(cmd);

    return 0;
}
