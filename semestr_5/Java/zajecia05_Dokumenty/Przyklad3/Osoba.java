class Osoba {
    String imie;
    String nazwisko;
    int rokUrodzenia;

    Osoba(String imie, String nazwisko, int rokUrodzenia)
    {
        this.imie=imie;
        this.nazwisko=nazwisko;
        this.rokUrodzenia=rokUrodzenia;
    }

    public String toString()
    {
        return this.imie + " " + this.nazwisko + " " + this.rokUrodzenia;
    }
}
