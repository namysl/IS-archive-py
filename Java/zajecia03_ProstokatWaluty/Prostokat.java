import java.io.*;

public class Prostokat
{
    double dlugosc;
    double szerokosc;

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    Prostokat(double dlugosc,double szerokosc)
    {
        this.dlugosc=dlugosc;
        this.szerokosc=szerokosc;
    }

    public String toString()
    {
        return "[dl: "+dlugosc+", sz: "+szerokosc+"]".toString();
    }

    double pole()
    {
        return dlugosc*szerokosc;
    }

    double obwod()
    {
        return 2*dlugosc+2*szerokosc;
    }


    void save(String plik) {
        try {
            PrintWriter plik1 = new PrintWriter(new BufferedWriter(new FileWriter(plik, true)));
            plik1.println("dlugosc: " + dlugosc + " szerokosc: " + szerokosc);

            plik1.close();
        }
        catch (Exception e) {
            System.out.println(e);
        }
    }

    void load(String plik) {

        System.out.println("\n-- z pliku --");

        try
        {
            BufferedReader plik2=new BufferedReader(new FileReader(plik));
            String str;

            while(plik2.ready())
            {
                str=plik2.readLine();
                System.out.println(str);
            }

            plik2.close();
        }
        catch(Exception e){System.out.println(e);}
    }
}
