public class Wektor {
    double x, y, z;

    Wektor(double x, double y, double z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }

    public String toString() { return "["+x+" "+y+" " +z+ "]";}

    Wektor plus(Wektor obj){
        return new Wektor(x + obj.x, y + obj.y, z + obj.z);
    }

    Wektor minus(Wektor obj){
        return new Wektor(x - obj.x, y - obj.y, z - obj.z);
    }

    Wektor iloczynWektorowy(Wektor obj){
        return new Wektor( (y*obj.z)-(z*obj.y), (z*obj.x)-(x*obj.z), (x*obj.y)-(y*obj.x));
    }

    double iloczynSkalarny(Wektor obj){
        return (double) (x * obj.x + y * obj.y + z * obj.z);
    }
}
