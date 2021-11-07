
public class Program {
    public static void main(String[] args) {
        //Dodawanie
        Dodawanie dodawanie1;
        dodawanie1 = new Dodawanie(1);
        double wynik1_dodawanie = dodawanie1.dodaj(1234);
        System.out.println(wynik1_dodawanie);

        double wynik2_dodawanie = dodawanie1.dodaj(10);
        System.out.println(wynik2_dodawanie);
        System.out.println(dodawanie1 + "\n");

        //Wiek
    /*
        try {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            System.out.println("Podaj rok urodzin: ");
            String rok_str = br.readLine();

            int rok_int = Integer.parseInt(rok_str);
            Wiek wiek1;
            wiek1 = new Wiek(rok_int);
            int wynik1_wiek = wiek1.ile_lat();
            System.out.println(wynik1_wiek);
        }
        catch(IOException e1)
        {
            System.out.println("wyjatek operacji wejscia/wyjscia");
        }

        catch(NumberFormatException e2)
        {
            System.out.println("nieprawidlowy format liczby");
        }
    */
        //Imie
    /*
        try {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            System.out.println("Podaj imie: ");
            String imie = br.readLine();
            System.out.println("Podaj nazwisko: ");
            String nazwisko = br.readLine();

            ImieNazwisko im_naz;
            im_naz = new ImieNazwisko(imie, nazwisko);
            System.out.println(im_naz.getImie());
            System.out.println(im_naz.getNazwisko());
            System.out.println(im_naz.getImieNazwisko());
            System.out.print(im_naz);
        }
        catch(IOException e1)
        {
            System.out.println("wyjatek operacji wejscia/wyjscia");
        }

        catch(NumberFormatException e2)
        {
            System.out.println("nieprawidlowy format liczby");
        }
    */
        //Liczba

        Liczba liczba1;
        liczba1 = new Liczba(4);
        String wynik1_liczba = liczba1.operacje(2);
        System.out.println(wynik1_liczba);
        System.out.println(liczba1.parzysta());
        System.out.println(liczba1.podzielna3i5());
        System.out.println(liczba1.pierwiastek());
        System.out.println(liczba1.trojkat_prostokatny(3, 5));

    }
}
