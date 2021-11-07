public class Liczba {
    double liczba;

    Liczba(double liczba){
        this.liczba = liczba;
    }

    public String operacje(double liczba2){
        double suma = liczba + liczba2;
        double roznica = liczba - liczba2;
        double iloczyn = liczba * liczba2;
        double iloraz = liczba / liczba2;

        return "suma: " + suma + ", roznica: " + roznica + ", iloczyn: " + iloczyn + ", iloraz: " + iloraz;
    }

    public boolean parzysta(){
        return liczba % 2 == 0;
    }

    public boolean podzielna3i5(){
        return (liczba % 3 == 0) && (liczba % 5 == 0);
    }

    public double do3Potegi(){
        return Math.pow(liczba, 3);
    }

    public double pierwiastek(){
        return Math.sqrt(liczba);
    }

    public boolean trojkat_prostokatny(double a, double b){
        double c;
        if (liczba > a && liczba > b){
            c = liczba;
        }
        else{
            if (a > b){
                c = a;
                a = liczba;
            }
            else{
                c = b;
                b = liczba;
            }
        }

        return Math.pow(a, 2) + Math.pow(b, 2) == Math.pow(c, 2);
    }
}
