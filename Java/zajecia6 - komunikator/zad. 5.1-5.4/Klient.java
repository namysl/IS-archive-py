import java.io.*;
import java.net.*;

public class Klient {

    public static final int PORT = 50007;
    public static final String HOST = "127.0.0.1";

    public static void main(String[] args) throws IOException {
        //nawiazanie polaczenia z serwerem
        Socket sock;
        try {
            sock = new Socket(HOST, PORT);
            System.out.println("Nawiazalem polaczenie: " + sock);

            //tworzenie strumieni danych pobieranych z klawiatury i dostarczanych do socketu
            BufferedReader klaw;
            klaw = new BufferedReader(new InputStreamReader(System.in));

            PrintWriter outp = new PrintWriter(sock.getOutputStream());
            BufferedReader inp = new BufferedReader(new InputStreamReader(sock.getInputStream()));


            //komunikacja - czytanie danych z klawiatury i przekazywanie ich do strumienia
            String str;
            while (true) {
                System.out.print("<Wysylamy:> ");
                str = klaw.readLine();
                outp.println(str);
                outp.flush();
                if (str.equals("koniec") || str.equals("KONIEC")) {
                    System.out.println("Koniec polaczenia");
                    break;
                }

            }

            //zamykanie polaczenia
            klaw.close();
            outp.close();
            sock.close();
        } catch (ConnectException e) {
            System.out.println("Błąd w połączeniu z serwerem");
        } catch (SocketException e) {
            System.out.println("Połączenie zerwane przez serwera");
        }
    }
}

