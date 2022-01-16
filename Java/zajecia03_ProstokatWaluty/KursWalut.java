import java.io.*;
//S1.14 - 9 listopada kolos

public class KursWalut
{
    static double KURS_dolar = 3.95;
    static double KURS_euro = 4.6;
    static double KURS_jen = 0.034;
    static double KURS_rubel = 0.0564;


    public static void main(String[] args)
    {
        try
        {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

            System.out.print("Z jakiej waluty: ");
            String waluta = br.readLine();

            System.out.print("Ilosc waluty: ");
            String pieniadze = br.readLine();

            double x = Double.parseDouble(pieniadze);

            if (waluta.equals("dolar")){
                System.out.println("PLN: " +  x * KURS_dolar);
            }
            else if (waluta.equals("euro")){
                System.out.println("PLN: " +  x * KURS_euro);
            }
            else if (waluta.equals("jen")){
                System.out.println("PLN: " +  x * KURS_jen);
            }
            else if (waluta.equals("rubel")){
                System.out.println("PLN: " +  x * KURS_rubel);
            }
            else {
                System.out.println("Nieobslugiwana waluta");
            }
        }

        catch(IOException e1)
        {
            System.out.println("wyjatek operacji wejscia/wyjscia");
        }

        catch(NumberFormatException e2)
        {
            System.out.println("nieprawidlowy format liczby");
        }
    }
}