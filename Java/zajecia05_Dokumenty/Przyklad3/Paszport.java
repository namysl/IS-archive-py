class Paszport extends Dokument
{
    Osoba wlasciciel;
    String typ;

    public boolean czyPasuje(String wzorzec)
    {
        return wzorzec.equalsIgnoreCase(this.wlasciciel.nazwisko);
    }

    public Paszport(Osoba w){
        this.typ = "Paszport";
        this.wlasciciel = w;
    }

    public String toString()
    {
        return this.typ + " " + this.wlasciciel.toString();
    }
}