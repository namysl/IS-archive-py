
class Prostokat
{
    double dlugosc;
    double szerokosc;
    Punkt wierzcholek;

    Prostokat(double dlugosc,double szerokosc)
    {
        this.dlugosc=dlugosc;
        this.szerokosc=szerokosc;
        this.wierzcholek=new Punkt(0,0);
    }

    Prostokat(double dlugosc,double szerokosc, Punkt wierzcholek)
    {
        this.dlugosc=dlugosc;
        this.szerokosc=szerokosc;
        this.wierzcholek=wierzcholek;
    }

    public String toString()
    {
        return "[dl: "+dlugosc+", sz: "+szerokosc+"]" + wierzcholek.toString();
    }
    /*Ćwiczenie 1.4
    * Metoda public String tostring() odpowiada pythonowemu __repr__
    * Dzieki przysłonieciu tej metody printując obiekt możemy uzyskać sformatowane przez nas informacje w postaci tekstu*/
    double pole()
    {
        return dlugosc*szerokosc;
    }

    double obwod()
    {
        return 2*dlugosc+2*szerokosc;
    }

    /* Zadanie 1.6 */
    void przesun(double u,double v){ //Przesunięcie wierzchołka prostokątu o wektor (dx,dy)
        wierzcholek.przesun(u,v);
    }

    boolean zawiera(Punkt obj){ //Metoda zwraca True/False w zalezności czy podany punkt znajduje się w prostokącie
        return (obj.x<=wierzcholek.x+dlugosc/2 && obj.x>=wierzcholek.x-dlugosc/2 && obj.y<=wierzcholek.y+szerokosc/2 && obj.y>=wierzcholek.y-szerokosc/2);
    }
}