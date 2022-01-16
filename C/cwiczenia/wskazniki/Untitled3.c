 #include <stdio.h>

 int main (void)
 {
   int liczba = 80;
   int *wskaznik = &liczba;   // wskaznik przechowuje adres, ktory pobieramy od zmiennej liczba

   printf("Wartosc zmiennej: %d, jej adres: %p.\n", liczba, &liczba);
   printf("Adres przechowywany we wskazniku: %p, wskazywana wartosc: %d.\n",
          wskaznik, *wskaznik);

   *wskaznik = 42;   // zapisanie liczby 42 do obiektu, na który wskazuje wskaznik
   printf("Wartosc zmiennej: %d, wartosc wskazywana przez wskaznik: %d\n",
          liczba, *wskaznik);

   liczba = 0x42;  // liczba podana w systemie szesnastkowym, podana po prefiksie 0x
   printf("Wartosc zmiennej: %d, wartosc wskazywana przez wskaznik: %d\n",
          liczba, *wskaznik);

   return 0;
 }
