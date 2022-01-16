class TrojkatRownoboczny extends Figura {

    double x;
    double y;
    double a;

    TrojkatRownoboczny(double x, double y, double a){
        this.x=x;
        this.y=y;
        this.a=a;
    }

    double pole(){
        return a*a*1.732/4;
    }

    double obwod(){
        return 3*a;
    }
}
