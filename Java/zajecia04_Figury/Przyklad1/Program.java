import java.awt.*;

public class Program
{
    public static void main(String[] args)
    {

        Prostokat a=new Prostokat(3,4); //tworzenie obiektu
        a.info();

        Prostokat b=new Prostokat(2,2); //tworzenie obiektu
        b.info();

        /*
           intersects - zwraca prawde lub falsz w zaleznosci
           od tego czy prostokaty maja czesc wspolna

           translate - przesuwa prostokat o wektor

         */

        if(a.intersects(b)) //metoda dziedziczona z Rectangle
        {
            System.out.println("-- przecinaja sie --\n");
        }
        else
        {
            System.out.println("-- NIE przecinaja sie --\n");
        }


        a.translate(5,3); //metoda dziedziczona z Rectangle
        a.info(); // metoda klasy Prostokat

        if(a.intersects(b)) //metoda dziedziczona z Rectangle
        {
            System.out.println("-- przecinaja sie --\n");
        }
        else
        {
            System.out.println("-- NIE przecinaja sie --\n");
        }

        Prostokat test = new Prostokat(new Point(3, 13), 12, 6);
        test.info();

        System.out.println("Testowanie prostokatow przylegajacych do prostokata test:");
        Prostokat top = new Prostokat(new Point(4, 15), 6, 2);
        Prostokat bot = new Prostokat(new Point(6, 7), 2, 2);
        Prostokat left = new Prostokat(new Point(1, 16), 2, 6);
        Prostokat right = new Prostokat(new Point(15, 15), 2, 3);

        System.out.println("Na gorze przylegajacy: " + test.przylega(top) + "\n");
        System.out.println("Na dole przylegajacy: " + test.przylega(bot) + "\n");
        System.out.println("Po lewej przylegajacy: " + test.przylega(left) + "\n");
        System.out.println("Po prawej przylegajacy: " + test.przylega(right) + "\n");

        System.out.println("Testowanie prostokatow nieprzylegajacych do prostokata test:");
        Prostokat top_oddalony = new Prostokat(new Point(4, 15), 6, 1);
        Prostokat bot_oddalony = new Prostokat(new Point(6, 6), 2, 2);
        Prostokat left_oddalony = new Prostokat(new Point(1, 16), 1, 4);
        Prostokat right_oddalony = new Prostokat(new Point(15, 15), 2, 2);

        System.out.println("Gorny oddalony: " + test.przylega(top_oddalony));
        System.out.println("Dolny oddalony: " + test.przylega(bot_oddalony));
        System.out.println("Po prawej oddalony: " + test.przylega(right_oddalony));
        System.out.println("Po lewej oddalony: " + test.przylega(left_oddalony));

    }
}