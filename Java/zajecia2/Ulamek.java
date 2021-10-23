public class Ulamek {
    int licznik;
    int mianownik;

    Ulamek(int licznik, int mianownik){
        this.licznik = licznik;
        this.mianownik = mianownik;
    }

    Ulamek plus(Ulamek obj){
        return new Ulamek(licznik*obj.mianownik+obj.licznik*mianownik, mianownik*obj.mianownik);
    }

    public String toString() { return "["+licznik+"/"+mianownik+"]";}

    Ulamek minus(Ulamek obj){
        return new Ulamek(licznik*obj.mianownik-obj.licznik*mianownik, mianownik*obj.mianownik);
    }

    Ulamek razy(Ulamek obj){
        return new Ulamek(licznik*obj.licznik, mianownik*obj.mianownik);
    }

    void odwroc(){
        int temp = this.licznik;
        this.licznik = this.mianownik;
        this.mianownik = temp;
    }

    void skroc() {
        int a = licznik;
        int b = mianownik;

        int nwd = a % b;

        while (nwd != 0) {
            nwd = a % b;
            a = b;
            b = nwd;
        }

        this.licznik /= a;
        this.mianownik /= a;
    }

    double rozwDziesietne(){
        return (double) licznik/mianownik;
    }
}
