public class WielomianKwadratowy {
    int a, b, c;

    WielomianKwadratowy(int a, int b, int c){
        this.a = a;
        this.b = b;
        this.c = c;
    }

    public String toString() { return a+"x^2 + "+ b+"x +" +c;}

    WielomianKwadratowy plus(WielomianKwadratowy obj){
        return new WielomianKwadratowy(a + obj.a, b + obj.b, c + obj.c);
    }

    WielomianKwadratowy minus(WielomianKwadratowy obj){
        return new WielomianKwadratowy(a - obj.a, b - obj.b, c - obj.c);
    }

    String razy(WielomianKwadratowy obj){
        return a*obj.a+"x^4 + "+(a*obj.b+obj.a*b)+"x^3 + "+(a*obj.c+c*obj.a+b*obj.b)+"x^2 + "+(b*obj.c+c*obj.b)+"x + "+c*obj.c;
    }

    String MiejscaZerowe(){
        double delta = b*b-4*a*c;
        if(delta<0){
            return "Brak miejsc zerowych";
        }
        else if (delta==0){
            return "x="+(-b/(2*a));
        }else{
            return "x1="+((-b-Math.sqrt(delta))/(2*a))+" x2="+((-b+Math.sqrt(delta))/(2*a));
        }
    }
}
