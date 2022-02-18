abstract class Dokument implements Przeszukiwalne
    //klasa abstrakcyjna to klasa, ktora moze zawierac metody abstrakcyjne,
    //takiej klasy nie mozna inicjalizowac, ale sluzy do dziedziczenia

    //w klasie abstrakcyjnej moga istniec metody abstrakcyjne, jak i nieabstrakcyjne
    //(w przeciwienstwie do interfejsow, gdzie sa tylko abstrakcyjne)
{
    Osoba wlasciciel;
    String typ;

    public abstract boolean czyPasuje(String wzorzec);

    public String toString()
    {
        return this.typ + " " + this.wlasciciel.toString();
    }

}