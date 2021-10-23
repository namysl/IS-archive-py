public class LiczbaZespolona {
    double re;
    double im;

    LiczbaZespolona(double re, double im){
        this.re = re;
        this.im = im;
    }

    public String toString() { return "["+re+" + "+im+"i]";}

    LiczbaZespolona plus(LiczbaZespolona obj){
        return new LiczbaZespolona(re+obj.re, im+obj.im);
    }

    LiczbaZespolona minus(LiczbaZespolona obj){
        return new LiczbaZespolona(re-obj.re, im-obj.im);
    }

    LiczbaZespolona razy(LiczbaZespolona obj){
        return new LiczbaZespolona(re*obj.re-im*obj.im, re*obj.im+im*obj.re);
    }


}
