public class ImieNazwisko {
    String imie;
    String nazwisko;

    ImieNazwisko(String imie, String nazwisko){
        this.imie = imie;
        this.nazwisko = nazwisko;
    }
    public String getImie(){
        return "Imie: " + this.imie;
    }

    public String getNazwisko(){
        return this.nazwisko;
    }

    public String getImieNazwisko(){
        return "Twoje imie: " + this.imie + " Twoje nazwisko: " + this.nazwisko;
    }

    public String toString(){
        return "tutaj jest println dla obiektu";
    }
}
