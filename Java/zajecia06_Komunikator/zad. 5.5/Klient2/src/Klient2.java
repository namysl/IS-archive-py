import java.io.*;
import java.net.*;

class Odbior extends Thread {
    Socket sock;
    BufferedReader sockReader;

    public Odbior(Socket sock) throws IOException {
        this.sock = sock;
        this.sockReader = new BufferedReader(new InputStreamReader(sock.getInputStream()));
    }

    public void run() {
        String str;
        try {
            while (true) {
                str = sockReader.readLine();
                System.out.println("<Odebrano:> " + str);
                if (str.equals("koniec") || str.equals("KONIEC")) {
                    System.out.println("Koniec polaczenia");
                    break;
                }
            }
            sock.close();
        } catch (IOException e) {
            System.out.println("Rozlaczono z serwerem");
        }
    }
}

class Wyslij extends Thread {
    Socket sock;
    PrintWriter sockWriter;
    BufferedReader kla;

    public Wyslij(Socket sock) throws IOException {
        this.sock = sock;
        this.sockWriter = new PrintWriter(sock.getOutputStream());
        this.kla = new BufferedReader(new InputStreamReader(System.in));
    }

    public void run() {
        String str;
        try{
            while (true) {
                System.out.println("<Wyslij:> ");
                str = kla.readLine();
                sockWriter.println(str);
                sockWriter.flush();
                if (str.equals("koniec") || str.equals("KONIEC")) {
                    System.out.println("Koniec polaczenia");
                    break;
                }
            }
            sock.close();
        } catch (IOException e) {
            System.out.println("Error");
        }
    }
}

public class Klient2 {
    public static final int PORT = 50007;
    public static final String HOST = "127.0.0.1";

    public static void main(String[] args) throws IOException {
        //nawiazanie polaczenia z serwerem
        Socket sock;
        sock = new Socket(HOST, PORT);
        System.out.println("Nawiazalem polaczenie: " + sock);

        //tworzenie watka odbierajacego i wysylajacego
        new Odbior(sock).start();
        new Wyslij(sock).start();
    }
}