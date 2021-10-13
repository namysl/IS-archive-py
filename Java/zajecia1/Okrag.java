class Okrag {
    double promien;
    Punkt srodek;

    Okrag (double promien) {
        this.promien = promien;
        this.srodek = new Punkt(0, 0);
    }

    Okrag(double promien, Punkt srodek) {
        this.promien = promien;
        this.srodek = srodek;
    }

    double obwod() {
        return 2 * 3.14 * promien;
    }

    double pole() {
        return 3.14 * (promien * promien);
    }

    public String toString() {
        return "r: " + promien + " srodek: " + srodek + " obwod: " + obwod() + " pole: " + pole();
    }
}