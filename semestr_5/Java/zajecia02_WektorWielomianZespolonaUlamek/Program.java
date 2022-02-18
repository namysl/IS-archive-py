import static java.lang.Math.sqrt;
public class Program
{
    public static void main(String[] args)
    {
        System.out.println("UŁAMKI:\n");

        Ulamek ul1 = new Ulamek(1,3);
        Ulamek ul2 = new Ulamek(2,3);

        System.out.println("Wynik dodawania:");
        Ulamek wynik = ul1.plus(ul2);
        System.out.println(wynik.toString());

        System.out.println("Wynik odejmowania:");
        wynik = ul1.minus(ul2);
        System.out.println(wynik.toString());

        System.out.println("Wynik mnożenia:");
        wynik = ul1.razy(ul2);
        System.out.println(wynik.toString());

        System.out.println("Wynik odwrócenia:");
        wynik = ul1;
        wynik.odwroc();
        System.out.println(wynik.toString());

        System.out.println("Wynik skrócenia:");
        wynik = new Ulamek(8745,393525);
        wynik.skroc();
        System.out.println(wynik.toString());

        System.out.println("Wynik skrócenia:");
        wynik = new Ulamek(1,2);
        wynik.skroc();
        System.out.println(wynik.toString());

        System.out.println("Rozwinięcie dziesiętne:");
        wynik = new Ulamek(1,3);
        System.out.println(wynik.rozwDziesietne());

        System.out.println("\nLICZBY ZESPOLONE:\n");

        LiczbaZespolona z1 = new LiczbaZespolona(1,3);
        LiczbaZespolona z2 = new LiczbaZespolona(2,4);

        System.out.println("Wynik dodawania:");
        LiczbaZespolona wynikZ = z1.plus(z2);
        System.out.println(wynikZ.toString());

        System.out.println("Wynik odejmowania:");
        wynikZ = z1.minus(z2);
        System.out.println(wynikZ.toString());

        System.out.println("Wynik mnożenia:");
        wynikZ = z1.razy(z2);
        System.out.println(wynikZ.toString());

        System.out.println("\nWEKTORY:\n");

        Wektor w1 = new Wektor(1,2, 3);
        Wektor w2 = new Wektor(3,2, 1);

        System.out.println("Iloczyn wektorowy:");
        Wektor wynikW = w1.iloczynWektorowy(w2);
        System.out.println(wynikW);

        System.out.println("Iloczyn skalarny:");
        double wynik_skalar = w1.iloczynSkalarny(w2);
        System.out.println(wynik_skalar);

        System.out.println("Dodawanie dwoch wektorow:");
        Wektor wynik_plus = w1.plus(w2);
        System.out.println(wynik_plus);

        System.out.println("Odejmowanie dwoch wektorow:");
        Wektor wynik_minus = w1.minus(w2);
        System.out.println(wynik_minus);

        System.out.println("\nWIELOMIAN KWADRATOWY:\n");

        WielomianKwadratowy wk1 = new WielomianKwadratowy(1,1, -6);
        WielomianKwadratowy wk2 = new WielomianKwadratowy(1,-10, 25);

        System.out.println("Dodawanie:");
        WielomianKwadratowy wynik_wk1 = wk1.plus(wk2);
        System.out.println(wynik_wk1);

        System.out.println("Odejmowanie:");
        WielomianKwadratowy wynik_wk2 = wk1.minus(wk2);
        System.out.println(wynik_wk2);

        System.out.println("Miejsce zerowe:");
        System.out.println(wk1.MiejscaZerowe());

        System.out.println("Miejsce zerowe:");
        System.out.println(wk2.MiejscaZerowe());

        System.out.println("Mnożenie");
        System.out.println(wk1.razy(wk2));
    }
}
