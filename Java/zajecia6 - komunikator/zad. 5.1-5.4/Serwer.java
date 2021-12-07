import java.io.*;
import java.net.*;

public class Serwer {

    public static final int PORT=50007;
    static ServerSocket serv;

    public static void main(String args[]) throws IOException
    {
        //tworzenie gniazda serwerowego
        serv=new ServerSocket(PORT);

        //oczekiwanie na polaczenie i tworzenie gniazda sieciowego
        System.out.println("Nasluchuje: "+serv);
        Socket sock;
        sock=serv.accept();
        System.out.println("Jest polaczenie: "+sock);

        //tworzenie strumienia danych pobieranych z gniazda sieciowego
        BufferedReader inp;
        inp=new BufferedReader(new InputStreamReader(sock.getInputStream()));
        PrintWriter outp;
        outp=new PrintWriter(sock.getOutputStream());

        //komunikacja - czytanie danych ze strumienia
        String str;
        while(true) {
            str = inp.readLine();
            System.out.println("<Nadeszlo:> " + str);
            if(str.equals("koniec")){
                System.out.println("Koniec polaczenia");
                break;
            }
            outp.println("ECHO"+str);
            outp.flush();
        }
        //zamykanie polaczenia
        inp.close();
        sock.close();
        serv.close();
    }
}

