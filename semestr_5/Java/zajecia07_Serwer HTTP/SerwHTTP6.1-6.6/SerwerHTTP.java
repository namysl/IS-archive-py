import java.io.*;
import java.net.*;

public class SerwerHTTP
{
    public static void main(String[] args) throws IOException
    {
        ServerSocket serv=new ServerSocket(8080);

        while(true)
        {
            //przyjecie polaczenia
            System.out.println("Oczekiwanie na polaczenie...");
            Socket sock=serv.accept();

            //strumienie danych
            InputStream is=sock.getInputStream();
            OutputStream os=sock.getOutputStream();
            BufferedReader inp=new BufferedReader(new InputStreamReader(is));
            DataOutputStream outp=new DataOutputStream(os);



            //przyjecie zadania (request)
            String request=inp.readLine();
            System.out.println(request);

            if(request != null) {
                //wyslanie odpowiedzi (response)
                String[] splitit = request.split("\\s");
                if (splitit.length > 2) {
                    System.out.println("get strona: " + splitit[splitit.length - 2].substring(1));
                }
                if (request.startsWith("GET")) {
                    //response header
                    String nazwaPliku = "/home/student/IdeaProjects/przyklad6/src/jakisplik.txt";  //linux path
                    FileInputStream fis = new FileInputStream(nazwaPliku);
                    //6.6
                    int iloscbajtow = fis.available();
                    //System.out.println(iloscbajtow);

                    outp.writeBytes("HTTP/1.0 200 OK\r\n");
                    if(nazwaPliku.endsWith(".html") || nazwaPliku.endsWith(".htm")){
                        outp.writeBytes("Content-Type: text/html\r\n");
                    }else {
                        outp.writeBytes("Content-Type: \r\n");
                    }
                    outp.writeBytes("Content-Length: <"+iloscbajtow+">\r\n");
                    outp.writeBytes("\r\n");

                    //response body
                    outp.writeBytes("<html>\r\n");
                    outp.writeBytes("<H1>Strona testowa</H1>\r\n");
                    outp.writeBytes("</html>\r\n");

                    //6.5

                    byte[] bufor;
                    bufor=new byte[1024];
                    int n=0;

                    while ((n = fis.read(bufor)) != -1 )
                    {
                        outp.write(bufor, 0, n);
                    }
                } else {
                    System.out.println("strona:" + splitit[splitit.length - 2].substring(1));
                    try {
                        BufferedReader br = new BufferedReader(new FileReader("~//IdeaProjects//przyklad6//src//" + splitit[splitit.length - 2].substring(1)));  //linux path
                        String line;
                        while ((line = br.readLine()) != null) {
                            outp.writeBytes(line);
                        }
                    } catch (Exception ex) {
                        outp.writeBytes("HTTP/1.0 404 nie znaleziono");
                        System.out.println("brak");
                    }
                }
            }
            else{
                outp.writeBytes("HTTP/1.1 501 Not supported.\r\n");
            }

            //zamykanie strumieni
            inp.close();
            outp.close();
            sock.close();
        }
    }
}

