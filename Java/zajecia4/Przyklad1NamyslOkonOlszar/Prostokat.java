import java.awt.*;

class Prostokat extends Rectangle {
    int dlugosc;
    int szerokosc;

    Prostokat(int a, int b)
    {
        super(a, b);
        /* defaultowo dziedziczone sa metody, ale nie konstruktory,
           super w wywolaniu konstruktora podklasy pozwala
           uzyc metod klasy nadrzednej
         */
    }

    Prostokat(Point wierzcholek, int dlugosc, int szerokosc) {
        super(wierzcholek, new Dimension(dlugosc, szerokosc));
        this.dlugosc = dlugosc;
        this.szerokosc = szerokosc;
    }

    boolean przylega(Prostokat obj){
        int []LG = {this.x, this.y};
        int []LD = {this.x, this.y - this.szerokosc};
        int []PG = {this.x + this.dlugosc, this.y};
        int []PD = {this.x + this.dlugosc, this.y - this.szerokosc};

        int []objLG = {obj.x, obj.y};
        int []objLD = {obj.x, obj.y - obj.szerokosc};
        int []objPG = {obj.x + obj.dlugosc, obj.y};
        int []objPD = {obj.x + obj.dlugosc, obj.y - obj.szerokosc};

        if ( (objLD[1] == LG[1]) && ((objLD[0] < PG[0]) && (objLD[0]+ obj.dlugosc > LG[0])) ) {
            System.out.println("obj na gorze");
            return true;
        }
        else if ( (objLG[1] == LD[1]) && ((objLG[0] < PD[0]) && (objLG[0] + obj.dlugosc > LD[0])) ) {
            System.out.println("obj na dole");
            return true;
        }
        else if ( (objPG[0] == LG[0]) && ((objLG[1] > LD[1]) && (objLG[1] - obj.szerokosc < LG[1])) ) {
            System.out.println("obj po lewej");
            return true;
        }
        else if ( (objLG[0] == PG[0]) && ((objLG[1] > PD[1]) && (objLG[1] - obj.szerokosc < LG[1])) ) {
            System.out.println("obj po prawej");
            return true;
        }
        else {
            return false;
        }
    }

    void info()
    {
        System.out.println(this);
    }
}