
class Prostokat
{
    double dlugosc;
    double szerokosc;
    Punkt wierzcholek;
    double srodek_x;
    double srodek_y;

    Prostokat(double dlugosc, double szerokosc) {
        this.dlugosc = dlugosc;
        this.szerokosc = szerokosc;
        this.wierzcholek = new Punkt(0, 0);
    }

    Prostokat(double dlugosc, double szerokosc, Punkt wierzcholek) {
        this.dlugosc = dlugosc;
        this.szerokosc = szerokosc;
        this.wierzcholek = wierzcholek;
    }

    public String toString() {
        return "[dl: " + dlugosc + ", sz: " + szerokosc + "]" + wierzcholek.toString();
    }

    double pole() {
        return dlugosc * szerokosc;
    }

    double srodek_x() {
        srodek_x = (wierzcholek.x + (wierzcholek.x + dlugosc)) / 2;

        return srodek_x;
    }

    double srodek_y() {
        srodek_y = (wierzcholek.y + (wierzcholek.y + szerokosc)) / 2;

        return srodek_y;
    }

    void przesun(double u, double v) {
        wierzcholek.przesun(u, v);
    }
}
