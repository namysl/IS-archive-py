import java.awt.*;
import java.awt.geom.*;

class Kulka extends Ellipse2D.Float
{
    Plansza p;
    int dx,dy;

    Kulka(Plansza p,int x,int y,int dx,int dy)
    {
        this.x=x;
        this.y=y;
        this.width=10;
        this.height=10;

        this.p=p;
        this.dx=dx;
        this.dy=dy;
    }

    void nextKrok()
    {
        x+=dx;
        y+=dy;

        if(getMinX()<0)  dx=Math.abs(dx);
        if(getMaxX()>p.getWidth())  dx=-Math.abs(dx);
        if(getMaxY()>345){
            //System.out.println("lose");
            dy=0;
            dx=0;
        }
        if(getMinY()<0) dy=Math.abs(dy);

        p.repaint();
        Toolkit.getDefaultToolkit().sync();
    }
}