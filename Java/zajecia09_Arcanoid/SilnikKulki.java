class SilnikKulki extends Thread
{
    Kulka a;
    Belka b;
    Cegielka[][] c;
    int []punktacja;
    int []stan;
    SilnikKulki(Kulka a, Belka b, Cegielka[][] c, int []punktacja, int []stan)
    {
        this.a=a;
        this.b=b;
        this.c=c;
        this.punktacja=punktacja;
        this.stan=stan;
        start();
    }

    public void run()
    {
        try
        {
            while(true)
            {
                //detekcja kulka-belka
                if(b.intersects(a.getBounds2D())){
                    if(b.x-a.x>b.y-a.y){//lewo
                        a.dx = -Math.abs(a.dx);
                    }else if(a.x+a.width-(b.x+b.width)>b.y-a.y){//prawo
                        a.dx = Math.abs(a.dx);
                    }else{//gora
                        a.dy = -Math.abs(a.dy);
                    }
                }
                //detekcja cegielka-kulka
                for(int i=0;i<5;i++){
                    for(int j=0;j<6;j++){
                        if(c[i][j]==null){
                            continue;
                        }
                       if(c[i][j].intersects(a.getBounds2D())){
                           if(c[i][j].x-a.x>c[i][j].y-a.y){//lewo
                               a.dx = -Math.abs(a.dx);
                           }else if(a.x+a.width-(c[i][j].x+c[i][j].width)>b.y-a.y){//prawo
                               a.dx = Math.abs(a.dx);
                           }else if(c[i][j].y>a.y){//gora
                               a.dy = -Math.abs(a.dy);
                           }else{//dol
                               a.dy = Math.abs(a.dy);
                           }
                           punktacja[0]++;
                           c[i][j]=null;
                           if(punktacja[0]==6*5){
                               stan[0]=2;//wygrana
                               a.dy=0;
                               a.dx=0;
                           }
                       }
                    }
                }
                //koniec gry?
                if(a.dy==0){
                    if(stan[0]==0){
                        stan[0]=1;//porazka
                    }
                }
                //kulka
                a.nextKrok();
                sleep(5);
            }
        }
        catch(InterruptedException e){}
    }
}