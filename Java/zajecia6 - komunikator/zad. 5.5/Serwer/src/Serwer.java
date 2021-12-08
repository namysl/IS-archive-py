import java.io.*;
import java.net.*;

class Odbior extends Thread
{
    Socket sockZ;  //odbiera
    Socket sockD;  //wysyla
    BufferedReader sockReaderZ;
    PrintWriter sockWriterD;

    public Odbior(Socket sockZ, Socket sockD) throws IOException
    {
        this.sockZ=sockZ;
        this.sockD=sockD;
        this.sockReaderZ=new BufferedReader(new InputStreamReader(sockZ.getInputStream()));
        this.sockWriterD=new PrintWriter(sockD.getOutputStream());
    }

    public void run()
    {
        String str;
        try{
            while(true){
                str = sockReaderZ.readLine();
                sockWriterD.println(str);
                sockWriterD.flush();
                if (str.equals("koniec") || str.equals("KONIEC")) {
                    System.out.println("Koniec polaczenia");
                    break;
                }
            }
            sockZ.close();
            sockD.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

public class Serwer
{
    public static final int PORT=50007;

    public static void main(String[] args) throws IOException
    {
        //tworzenie gniazda serwerowego
        ServerSocket serv;
        serv=new ServerSocket(PORT);

        //oczekiwanie na polaczenie i tworzenie gniazda sieciowego
        System.out.println("Nasluchuje: "+serv);
        Socket sock1;
        sock1=serv.accept();
        Socket sock2;
        sock2=serv.accept();
        System.out.println("Jest polaczenie: "+sock1+" "+sock2);

        //tworzenie watka odbierajacego i wysylajacego
        new Odbior(sock1,sock2).start();
        new Odbior(sock2,sock1).start();

    }
}