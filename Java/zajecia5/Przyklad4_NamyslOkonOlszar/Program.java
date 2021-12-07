import java.io.*;

public class Program
{
    public static void main(String[] args)
    {
        System.out.println("-- do zapisu --");
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));

        DowodOsobisty z=new DowodOsobisty(br);
        z.info();

        Paszport p = new Paszport(br);
        p.info();

        try
        {
            ObjectOutputStream outp=new ObjectOutputStream(new FileOutputStream("plik.dat"));
            outp.writeObject(z);
            outp.writeObject(p);
            outp.close();
        }
        catch (FileNotFoundException e){System.out.println("Plik nie istnieje");}
        catch(Exception e){System.out.println(e);}


        System.out.println("\n-- z pliku --");
        ObjectInputStream inp;

        try
        {
            inp=new ObjectInputStream(new FileInputStream("plik.dat"));
            Object o=inp.readObject();
            Object o2=inp.readObject();

            DowodOsobisty x=(DowodOsobisty)o;
            Paszport y=(Paszport)o2;

            inp.close();
            x.info();
            y.info();
        }
        catch (FileNotFoundException e){System.out.println("Plik nie istnieje");}
        catch(Exception e){System.out.println(e);}

    }
}