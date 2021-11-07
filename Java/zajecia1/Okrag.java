/* Zadanie 1.7 */
public class Okrag {
    double promien;
    Punkt srodek;

    Okrag(double promien)
    {
        this.promien=promien;
        this.srodek=new Punkt(0,0);
    }

    Okrag(double promien, Punkt srodek)
    {
        this.promien=promien;
        this.srodek=srodek;
    }

    double pole()
    {
        return promien*promien*Math.PI;
    }

    double obwod()
    {
        return 2*promien*Math.PI;
    }

    boolean zawiera(Punkt obj){ //Metoda zwraca True/False w zalezności czy znajduje się w okręgu
        return (Math.sqrt((obj.x-srodek.x)*(obj.x-srodek.x)+(obj.y-srodek.y)*(obj.y-srodek.y))<=promien);
    }
}
