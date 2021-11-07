public class Wiek {
    int rok_narodzin;
    static int obecny_rok = 2021;

    Wiek(int rok_narodzin){
        this.rok_narodzin = rok_narodzin;
    }

    public int ile_lat(){
        return obecny_rok - rok_narodzin;

    }
}
