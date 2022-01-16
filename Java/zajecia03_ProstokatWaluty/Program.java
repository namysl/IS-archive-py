public class Program
{
    public static void main(String[] args)
    {
        //prostokat
        Prostokat obj2;
        obj2=new Prostokat(1,2);
        double p=obj2.pole();

        obj2.save("plikkk");

        obj2.load("plikkk");

    }
}