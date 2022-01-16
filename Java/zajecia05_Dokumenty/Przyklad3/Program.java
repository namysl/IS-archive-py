public class Program
{
    public static void main(String[] args)
    {

        Osoba o1 = new Osoba("Anna", "Kowalska", 1990);
        Osoba o2 = new Osoba("Maria", "Wojciechowska", 1991);
        Osoba o3 = new Osoba("Katarzyna", "KOWALska", 1992);

        Dokument[] bazaDanych={new Paszport(o1), new DowodOsobisty(o2), new Paszport(o3)};

        Dokument z;
        String wzorzec="kowalska";

        for(int i=0;i<bazaDanych.length;i++)
        {
            z=bazaDanych[i];
            if(z.czyPasuje(wzorzec))System.out.println("znaleziono: "+z);
        }
    }
}