class DowodOsobisty extends Dokument
{
    Osoba wlasciciel;
    String typ;

    public DowodOsobisty(Osoba w){
        this.typ = "Dowod Osobisty";
        this.wlasciciel = w;
    }

    public boolean czyPasuje(String wzorzec)
    {
        return wzorzec.equalsIgnoreCase(this.wlasciciel.nazwisko);
    }

    public String toString()
    {
        return this.typ + " " + this.wlasciciel.toString();
    }
}