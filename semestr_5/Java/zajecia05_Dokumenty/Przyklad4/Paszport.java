import java.io.*;

class Paszport implements Serializable
{
    Osoba posiadacz;
    String numer;

    Paszport(BufferedReader br)
    {
        try
        {
            this.posiadacz=new Osoba(br);

            System.out.print("numer paszportu: ");
            this.numer=br.readLine();
        }
        catch(IOException e){}
    }

    public String toString()
    {
        return "<do:> "+posiadacz.toString()+" "+this.numer;
    }

    void info()
    {
        System.out.println(this);
    }
}
