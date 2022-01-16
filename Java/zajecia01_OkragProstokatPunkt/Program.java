public class Program
{
    public static void main(String[] args)
    {
        //punkt
        Punkt obj1;
        obj1=new Punkt(-1,1);
        System.out.println("punkt: "+obj1);
        obj1.przesun(-1,3);
        System.out.println("punkt po przesunieciu: "+obj1);

        //prostokat
        Punkt obj;
        obj = new Punkt(0,0);

        Prostokat obj2;
        obj2=new Prostokat(3,4, obj);
        System.out.println(obj2);

        obj2.przesun(7,-3);
        System.out.println(obj2);

        double p=obj2.pole();
        System.out.println("pole: "+p);

        //Test: Punkt zawiera się w prostokącie
        Punkt p1 = new Punkt(8,-4.5);
        Punkt p2 = new Punkt(6,-0.5);

        System.out.println("punkt 1: "+obj2.zawiera(p1));
        System.out.println("punkt 2: "+obj2.zawiera(p2));

        //okrag
        Punkt obj3;
        obj3 = new Punkt(0,0);
        Okrag obj4;
        obj4 = new Okrag(1, obj3);
        System.out.println("obwod: "+obj4.obwod());
        System.out.println("pole: "+obj4.pole());

        //Test: Punkt zawiera się w okręgu
        Punkt obj5 = new Punkt(0.7,0.7);
        Punkt obj6 = new Punkt(0.71,0.71);
        System.out.println("punkt 0.7: "+obj4.zawiera(obj5));
        System.out.println("punkt 0.71: "+obj4.zawiera(obj6));
    }
}