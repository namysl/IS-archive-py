import java.io.*;
import java.net.*;
import java.util.Calendar;
import java.text.SimpleDateFormat;

// zrobic schemat blokowy!

class ObslugaZadania extends Thread {
    Socket client;
    InputStream in;
    OutputStream out;
    BufferedReader Receiver;
    DataOutputStream Sender;

    ObslugaZadania(Socket clientSocket) throws IOException {
        this.client = clientSocket;
        //tworzenie strumienia
        this.in = this.client.getInputStream();
        this.out = this.client.getOutputStream();
        this.Receiver = new BufferedReader(new InputStreamReader(in));
        this.Sender = new DataOutputStream(out);
    }

    public void run() {
        try {
            //get request
            String request = this.Receiver.readLine();
            //zsynchronizowany dostęp do pliku dziennika
            //synchronizacja w javie to możliwość kontrolowania dostępu wielu wątków do dowolnego
            //udostępnionego zasobu

            synchronized (SerwerHTTP.LogWriter) {
                String timeStamp = new SimpleDateFormat("yyyy.MM.dd HH:mm:ss").format(
                        Calendar.getInstance().getTime());
                SerwerHTTP.LogWriter.printf("[%s] %s %s\n", timeStamp, request, this.client.getRemoteSocketAddress().toString());
                SerwerHTTP.LogWriter.flush();
            }
            //parse filename
            String[] splited = request.split("\\s+");
            String fn = splited[1].replace("/", "");
            //System.out.println("111111111" + fn);

            //if root requested -> return index.html
            if (fn.equals("")) {
                this.get_file("index.html");
            } else { //return requested file if exists
                this.get_file(fn);
            }
        } catch (IOException e) {
            System.out.println(e);
        }
    }

    static String getExtension(String fn) {
        //parse file extension
        int dotIdx = fn.lastIndexOf(".");
        String extension = "";
        if (dotIdx > 0) {
            extension = fn.substring(dotIdx + 1);
        }
        //System.out.println("2222222222" + extension);
        return extension;
    }

    void httpHeader(String type, String length) throws IOException {
        //naglowek odpowiedzi
        this.Sender.writeBytes("HTTP/1.0 200 OK\r\n");
        this.Sender.writeBytes("Content-Type: " + type + "\r\n");
        this.Sender.writeBytes("Content-Length: " + length + "\r\n");
        this.Sender.writeBytes("\r\n");
    }

    void get_file(String fn) throws IOException {
        FileInputStream file;

        try {
            //create file stream
            file = new FileInputStream(fn);

            //define content lenght
            int contentLenght = file.available();

            //define content type
            String extension = getExtension(fn);
            String contentType = "";
            if (extension.equals("html") || extension.equals("htm")) {
                contentType = "text/html";
            }

            if (extension.equals("png")) {
                contentType = "image/png";
            }
            //response header
            httpHeader(contentType, Integer.toString(contentLenght));
            //send requested file
            byte[] buffer = new byte[1024];
            int n = 0;
            while ((n = file.read(buffer)) != -1) {
                this.Sender.write(buffer, 0, n);
            }
            file.close();
        } catch (FileNotFoundException e) {
            this.Sender.writeBytes("HTTP/1.1 404 Not Found.\r\n");
        }
    }
}

public class SerwerHTTP {
    //server log file
    public static String Log = "log.txt";
    public static PrintWriter LogWriter;

    //static initializer
    static {
        try {
            LogWriter = new PrintWriter(new BufferedWriter(new FileWriter(Log, true)));
        } catch (IOException e) {
            System.out.println(e);
        }
    }

    public static void main(String[] args) throws IOException
    {
        int port;
        boolean accepted = false;
        BufferedReader keyboard = new BufferedReader(new InputStreamReader(System.in));
        ServerSocket serv = null;
        Socket clientSocket;
        //check argument availability

        if (args.length==0){
            System.out.println("Specify port number");
            System.out.print("PORT: ");
        }
        else{
            //parse port number
            try{
                port = Integer.parseInt(args[0]);
                serv = new ServerSocket(port);
                System.out.println("Server started: "+serv);
                accepted = true;
            }catch(BindException e){
                System.out.println("Port is already in use");
                System.out.print("PORT: ");
            }
        }

        //ask for free port
        while(!accepted){
            if(keyboard.ready()){
                try{
                    port = Integer.parseInt(keyboard.readLine());
                    serv = new ServerSocket(port);
                    System.out.println("Server started: " + serv);
                    accepted = true;
                }catch(BindException e){
                    System.out.println("Port is already in use");
                    System.out.print("PORT: ");
                }
            }
        }
        while(true)
        {
            //accept connections from clients
            System.out.println("Oczekiwanie na polaczenie...");
            clientSocket = serv.accept();
            //tworzenie watku obslugi tego polaczenia
            new ObslugaZadania(clientSocket).start();
        }
    }
}