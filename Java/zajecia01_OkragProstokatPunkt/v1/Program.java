public class Program
{
    public static void main(String[] args)
    {
        Punkt obj1;
        obj1 = new Punkt(-1, 1);
        System.out.println("punkt: " + obj1);

        Prostokat obj2;
        obj2 = new Prostokat(3, 4, obj1);
        System.out.println("prostokat: " + obj2);

        double p = obj2.pole();
        System.out.println("pole: " + p);

        double sr_x = obj2.srodek_x();
        double sr_y = obj2.srodek_y();
        System.out.println("\nPRZYKLAD 2: srodek");
        System.out.println("srodek_x: " + sr_x + " srodek_y: " + sr_y);

        System.out.println("\nCWICZENIE 1.5:");
        Punkt obj;
        obj = new Punkt(0, 0);
        System.out.println(obj);

        obj.przesun(-1, 3);
        System.out.println(obj);

        obj.przesun(-2, -3);
        System.out.println(obj);

        System.out.println("\nCWICZENIE 1.6:");
        Punkt obj11;
        obj11 = new Punkt(0, 0);

        Prostokat obj22;
        obj22 = new Prostokat(3, 4, obj11);
        System.out.println(obj22);

        obj22.przesun(7,-3);
        System.out.println(obj22);

        System.out.println("\nCWICZENIE 1.7:");
        Punkt srodek_okregu;
        srodek_okregu = new Punkt(0, 0);

        Okrag okrag1;
        okrag1 = new Okrag(4, srodek_okregu);
        System.out.println(okrag1);
    }
}
