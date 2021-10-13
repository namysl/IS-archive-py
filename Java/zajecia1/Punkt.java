class Punkt {
    double x;
    double y;

    Punkt(double x, double y) {
        this.x = x;
        this.y = y;
    }

    public String toString() {
        return "[x: " + x + ", y: " + y + "]";
    }

    void przesun(double dx, double dy) {
        x = dx + x;
        y = dy + y;
    }
}
