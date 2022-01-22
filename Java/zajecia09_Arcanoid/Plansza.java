import javax.swing.*;
import java.awt.event.*;
import java.awt.*;

class Plansza extends JPanel implements MouseMotionListener
{
    Belka b;
    Kulka a;
    Cegielka[][] cegielki;
    SilnikKulki s;
    int []punktacja={0};
    int []stan={0};
    long start;
    long koniec;
    long czas;

    Plansza()
    {
        super();
        addMouseMotionListener(this);

        b=new Belka(100);
        a=new Kulka(this,300,300,-1,-1);
        cegielki = new Cegielka[5][6];
        for(int i=0;i<5;i++){
            for(int j=0;j<6;j++){
                cegielki[i][j]=new Cegielka(10+i*75,10+j*20);
            }
        }

        s=new SilnikKulki(a, b, cegielki, punktacja, stan);
        start = System.currentTimeMillis();
    }

    public void paintComponent(Graphics g)
    {
        super.paintComponent(g);
        Graphics2D g2d=(Graphics2D)g;

        g2d.fill(a);
        g2d.fill(b);
        for(int i=0;i<5;i++){
            for(int j=0;j<6;j++){
                if(cegielki[i][j]==null){
                    continue;
                }
                g2d.fill(cegielki[i][j]);
            }
        }
        if(stan[0]==1){//porazka
            g2d.drawString("Porazka! \nPunkty: " + punktacja[0],300/2,370/2);
        }else if(stan[0]==2){
            if(koniec==0) {
                koniec = System.currentTimeMillis();
                czas = koniec - start;
            }
            g2d.drawString("Wygrana! \nPunkty: "+punktacja[0]+" Czas: "+czas/1000,200/2,370/2);
        }

    }

    public void mouseMoved(MouseEvent e)
    {
        b.setX(e.getX()-50);
        //b.y = e.getY();
        repaint();
    }

    public void mouseDragged(MouseEvent e)
    {

    }
}