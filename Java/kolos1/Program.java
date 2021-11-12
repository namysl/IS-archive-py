public class Program {
    public static void main(String[] args){
        int [][]przykladowa_tablica = { {1, 2, 3}, {4, 5, 6}, {7, 8, 9} };

        Macierz obj1;
        obj1 = new Macierz(przykladowa_tablica);
        System.out.println("Utworzona tablica:");
        obj1.pokaz();

        System.out.println("Zmiana wybranej wartosci:");
        obj1.zmien_jedna_wartosc(100, 2,2);
        obj1.pokaz();

        obj1.zmien_jedna_wartosc(9, 2, 2);

        System.out.println("Macierz transponowana:");
        Macierz obj2;
        obj2 = new Macierz(obj1.transpozycja());
        obj2.pokaz();

        System.out.println("Wypelnianie nowej:");
        Macierz obj3;
        obj3 = new Macierz();
        int [][]inna_tablica = { {1, 2, 3}, {1, 2, 3}, {1, 2, 3} };
        obj3.wypelnij_podanymi(inna_tablica);
        obj3.pokaz();

        System.out.println("Dodawanie dwoch macierzy:");
        Macierz wynik_dod = obj1.dodawanie(obj3);
        wynik_dod.pokaz();

        System.out.println("Odejmowanie dwoch macierzy:");
        Macierz wynik_ode = obj1.odejmowanie(obj3);
        wynik_ode.pokaz();

        System.out.println("Mnozenie dwoch macierzy:");
        Macierz wynik_mno = obj1.mnozenie(obj3);
        wynik_mno.pokaz();

        System.out.println("Wyznacznik macierzy:");
        System.out.println(obj1.wyznacznik());
    }
}
