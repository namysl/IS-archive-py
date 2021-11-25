#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

main() {
    char alph[30] = {'a', 'b', 'c', 'd', 'e', 'f',
	 	     'g', 'k', 'l', 'm', 'n', 'o', 'p',
     		     'r', 's', 't', 'y', 'z', 'x', 'i',
		     'w', 'v', 'q', 'h', 'u', 'j', '.',
		     ',', '\t'};

    char numb[10] = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'};

    char c;
    bool ye, already_space, i_need_to_print_space;
    double removed_spaces, removed_numbers, removed_others, amount_of_chars;
    double per_sp, per_nb, per_ch;

    per_sp = 0;
    per_ch = 0;
    per_nb = 0;

    ye = false;
    already_space = true;
    removed_spaces = 0;
    removed_numbers = 0;
    removed_others = -1;
    amount_of_chars = -1;

    printf("Prosze podac tekst: \n");

    do {
	c = getchar();
	if ((c == ' ') && (already_space == false)) {
	     i_need_to_print_space = true;
	     already_space = true;
	} else if ((c == ' ') && (already_space == true)) {
	     removed_spaces += 1;
	     amount_of_chars += 1;
	} else {
	    for (int i=0; i < 30; i++){
		if (tolower(c) == alph[i]){
		    ye = true;
		}
	    }
	    if (ye == true) {
		if (i_need_to_print_space == true) {
		    putchar(' ');
		}
	        putchar(toupper(c));
	    	already_space = false;
	    } else {
		for (int i=0; i < 10; i++) {
		    if (c == numb[i]) {
		        ye = true;
		    }
		}
		if (ye == true) {
		    removed_numbers+= 1;
	            amount_of_chars += 1;
		} else {
		    removed_others += 1;
		    amount_of_chars += 1;
		}
	    }
	}

	ye = false;
    } while (c != '\n');

    if (amount_of_chars != 0) {
	    per_sp = removed_spaces / amount_of_chars;
	    printf("\n Usuniete spacji: %lf.% \n", per_sp*100);
	    per_nb = removed_numbers / amount_of_chars;
	    printf("Usuniete liczby: %lf.% \n", per_nb*100);
	    per_ch = removed_others / amount_of_chars;
	    printf("Usuniete inne: %lf.% \n", per_ch*100);
    } else {
	    printf("\n Nie ma usuniętych symboli");
    }
}
