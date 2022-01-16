import javax.swing.*;
import java.awt.event.*;
import java.awt.*;
import java.io.*;
import java.math.*;
import java.util.Arrays;


public class Kalk implements ActionListener, KeyListener
{
    JTextField t1;

    JButton b1, b2, b3, b4, b5, b6, b7, b8, b9, b0;
    JButton bplus, brow, bminus, bmult, bdiv, bdot;
    JButton bproc, broot, bpower, bmemrc, bmemplus, bmemminus, bdelete;

    JButton back;
    double[] zapis = new double[] {};

    double x, buf;
    char bufZnak;
    double memory;
    boolean memory_exists = false;

    static char znak;

    public void keyTyped(KeyEvent e) {
        System.out.println(e + "KEY TYPED: ");
    }

    public void keyPressed(KeyEvent e) {
        System.out.println(e + "KEY PRESSED: ");
    }

    public void keyReleased(KeyEvent e) {
        System.out.println(e + "KEY RELEASED: ");
    }

    public void do_pliku(String dane){
        try
        {
            PrintWriter plik1=new PrintWriter(new BufferedWriter(new FileWriter("plik.txt",true)));
            plik1.print(dane);
            plik1.close();
        }
        catch (FileNotFoundException e){System.out.println("Plik nie istnieje");}
        catch(Exception e){System.out.println(e);}
    }

    public void actionPerformed(ActionEvent e)
    {
        Object target = e.getSource();

        if(target==b1)
        {
            t1.setText(t1.getText()+((JButton)target).getText());
            t1.requestFocus();
        }

        else if(target==b2)
        {
            t1.setText(t1.getText()+((JButton)target).getText());
            t1.requestFocus();
        }

        else if(target==b3)
        {
            t1.setText(t1.getText()+((JButton)target).getText());
            t1.requestFocus();
        }

        else if(target==b4)
        {
            t1.setText(t1.getText()+((JButton)target).getText());
            t1.requestFocus();
        }

        else if(target==b5)
        {
            t1.setText(t1.getText()+((JButton)target).getText());
            t1.requestFocus();
        }

        else if(target==b6)
        {
            t1.setText(t1.getText()+((JButton)target).getText());
            t1.requestFocus();
        }

        else if(target==b7)
        {
            t1.setText(t1.getText()+((JButton)target).getText());
            t1.requestFocus();
        }

        else if(target==b8)
        {
            t1.setText(t1.getText()+((JButton)target).getText());
            t1.requestFocus();
        }

        else if(target==b9)
        {
            t1.setText(t1.getText()+((JButton)target).getText());
            t1.requestFocus();
        }

        else if(target==b0)
        {
            t1.setText(t1.getText()+((JButton)target).getText());
            t1.requestFocus();
        }

        else if(target==back){
            if(zapis.length > 1){
                zapis = Arrays.copyOf(zapis, zapis.length-1);
                double ostatni = zapis[zapis.length-1];
                t1.setText(Double.toString(ostatni));
                t1.requestFocus();
            }
            else if(zapis.length == 1){
                zapis = Arrays.copyOf(zapis, zapis.length-1);
                t1.setText("");
                t1.requestFocus();
            }
            else{
                t1.setText("");
                t1.requestFocus();
            }
        }

        else if(target==bdot)
        {
            if(t1.getText().indexOf('.')==-1) {
                if(t1.getText().equals("-")) {
                    t1.setText(t1.getText() + "0");
                }
                    t1.setText(t1.getText() + ((JButton) target).getText());
                    t1.requestFocus();
            }
        }

        else if(target==bdelete)
        {
            buf=0;
            t1.setText("");
            t1.requestFocus();
        }

        else if(target==bplus)
        {
            if(!t1.getText().equals("") && !t1.getText().equals(".") && !t1.getText().equals("-")) {
                buf = Double.parseDouble(t1.getText());
                bufZnak = '+';
                t1.setText("");
                t1.requestFocus();
            }
        }

        else if(target==bminus)
        {
                if (t1.getText().equals("") && !t1.getText().equals("-")) {
                    t1.setText(t1.getText() + ((JButton) target).getText());
                    t1.requestFocus();
                } else if(!t1.getText().equals(".") && !t1.getText().equals("-")){
                    buf = Double.parseDouble(t1.getText());
                    bufZnak = '-';
                    t1.setText("");
                    t1.requestFocus();
                }
        }

        else if(target==bmult)
        {
            if(!t1.getText().equals("") && !t1.getText().equals(".") && !t1.getText().equals("-")) {
                buf = Double.parseDouble(t1.getText());
                bufZnak = '*';
                t1.setText("");
                t1.requestFocus();
            }
        }

        else if(target==bdiv)
        {
            if(!t1.getText().equals("") && !t1.getText().equals(".") && !t1.getText().equals("-")) {
                buf = Double.parseDouble(t1.getText());
                bufZnak = '/';
                t1.setText("");
                t1.requestFocus();
            }
        }

        else if(target==broot) {
            if(!t1.getText().equals("") && !t1.getText().equals(".") && !t1.getText().equals("-")) {
                x = Double.parseDouble(t1.getText());

                String pars = "√"+ x;
                do_pliku(pars);

                x = Math.sqrt(x);
                do_pliku(" = "+x+"\n");
                t1.setText(Double.toString(x));
                t1.requestFocus();
            }
        }

        else if(target==bpower)
        {
            if(!t1.getText().equals("") && !t1.getText().equals(".") && !t1.getText().equals("-")) {
                buf = Double.parseDouble(t1.getText());
                bufZnak = '^';
                t1.setText("");
                t1.requestFocus();
            }
        }

        else if(target==brow||target==t1)
        {
            if(!t1.getText().equals("") && !t1.getText().equals(".") && !t1.getText().equals("-")) {
                x = Double.parseDouble(t1.getText());

                String pars = buf + " " + bufZnak + " " + x;
                do_pliku(pars);

                if (bufZnak == '+') {
                    x = buf + x;
                } else if (bufZnak == '-') {
                    x = buf - x;
                } else if (bufZnak == '*') {
                    x = buf * x;
                } else if (bufZnak == '/') {
                    x = buf / x;
                } else if (bufZnak == '^') {
                    x = Math.pow(buf, x);
                }

                do_pliku(" = " + x + "\n");
                zapis = Arrays.copyOf(zapis, zapis.length+1);
                zapis[zapis.length-1] = x;

//                for(int x=0; x<zapis.length; x++){
//                    System.out.print(zapis[x] + " ");
//                }
//                System.out.print("\n");

                t1.setText(Double.toString(x));
                t1.requestFocus();
            }
        }
        else if(target==bproc)
        {
            if(!t1.getText().equals("") && !t1.getText().equals(".") && !t1.getText().equals("-")) {
                x = Double.parseDouble(t1.getText());

                String pars = buf + " " + bufZnak + " " + x + "%";
                do_pliku(pars);

                if (bufZnak == '+') {
                    x = buf + buf * x / 100;
                } else if (bufZnak == '-') {
                    x = buf - buf * x / 100;
                } else if (bufZnak == '*') {
                    x = buf * x / 100;
                } else if (bufZnak == '/') {
                    x = buf / x * 100;
                }
                do_pliku(" = " + x + "\n");
                t1.setText(Double.toString(x));
                t1.requestFocus();
            }
        }

        else if(target==bmemrc){ //ładuje
            if (memory_exists){
                t1.setText(Double.toString(memory));
            }
        }

        else if(target==bmemplus){ //dodaje
            if(!t1.getText().equals("") && !t1.getText().equals(".") && !t1.getText().equals("-")) {
                memory = Double.parseDouble(t1.getText());
                memory_exists = true;
            }
        }

        else if(target==bmemminus){//usuwa
            memory = 0;
            memory_exists = false;
        }
    }

    void init()
    {
        //try
        //{
        //UIManager.setLookAndFeel(UIManager.getSystemLookAndFeelClassName());
        //}
        //catch(Exception e){}

        JFrame f=new JFrame();
        Container c=f.getContentPane();

        GridBagLayout gbl=new GridBagLayout();
        GridBagConstraints gbc=new GridBagConstraints();
        gbc.fill=GridBagConstraints.HORIZONTAL;
        c.setLayout(gbl);

        t1=new JTextField(15);

        t1.addKeyListener(new KeyAdapter() {
            public void keyTyped(KeyEvent e) {
                znak = e.getKeyChar();

                if (znak >= '0' && znak <= '9'){
                    System.out.println(znak);
                    t1.setText(t1.getText() + znak);
                }
                else if (znak == '+' || znak == '-' || znak == '*' || znak == '/' || znak == ',' || znak == '.'){
                    System.out.println(c);
                    //t1.setText(t1.getText() + znak);

                    if(znak=='+')
                    {
                        if(!t1.getText().equals("") && !t1.getText().equals(".") && !t1.getText().equals("-")) {
                            buf = Double.parseDouble(t1.getText());
                            bufZnak = '+';
                            t1.setText("");
                            t1.requestFocus();
                        }
                    }

                    else if(znak=='-')
                    {
                        if (t1.getText().equals("") && !t1.getText().equals("-")) {
                            t1.setText(t1.getText() + znak);
                            t1.requestFocus();
                        } else if(!t1.getText().equals(".") && !t1.getText().equals("-")){
                            buf = Double.parseDouble(t1.getText());
                            bufZnak = '-';
                            t1.setText("");
                            t1.requestFocus();
                        }
                    }

                    else if(znak=='*')
                    {
                        if(!t1.getText().equals("") && !t1.getText().equals(".") && !t1.getText().equals("-")) {
                            buf = Double.parseDouble(t1.getText());
                            bufZnak = '*';
                            t1.setText("");
                            t1.requestFocus();
                        }
                    }

                    else if(znak=='/')
                    {
                        if(!t1.getText().equals("") && !t1.getText().equals(".") && !t1.getText().equals("-")) {
                            buf = Double.parseDouble(t1.getText());
                            bufZnak = '/';
                            t1.setText("");
                            t1.requestFocus();
                        }
                    }
                    else if(znak == ',' || znak == '.')
                    {
                        if(t1.getText().indexOf('.')==-1) {
                            if(t1.getText().equals("-")) {
                                t1.setText(t1.getText() + "0");
                            }
                            t1.setText(t1.getText() + '.');
                            t1.requestFocus();
                        }
                    }
                    else{
                        int znak_int = e.getKeyCode();

                        if(znak_int == 10){
                            System.out.println("Enter");

                            if(!t1.getText().equals("") && !t1.getText().equals(".") && !t1.getText().equals("-")) {
                                x = Double.parseDouble(t1.getText());
                                if (bufZnak == '+') {
                                    x = buf + x;
                                } else if (bufZnak == '-') {
                                    x = buf - x;
                                } else if (bufZnak == '*') {
                                    x = buf * x;
                                } else if (bufZnak == '/') {
                                    x = buf / x;
                                } else if (bufZnak == '^') {
                                    x = Math.pow(buf, x);
                                }
                                t1.setText(Double.toString(x));
                                t1.requestFocus();
                            }
                        }
                    }
                }
            }
        });

        t1.setEditable(false);

        t1.addActionListener(this);
        t1.setHorizontalAlignment(JTextField.RIGHT);
        gbc.gridx=0;
        gbc.gridy=0;
        gbc.gridwidth=5;
        gbc.ipadx=0;
        gbc.ipady=5;
        gbc.insets=new Insets(5,5,0,0);
        gbl.setConstraints(t1,gbc);
        c.add(t1);



        b1=new JButton("1");
        b1.addActionListener(this);
        b1.setFocusable(false);
        gbc.gridx=0;
        gbc.gridy=1;
        gbc.gridwidth=1;
        gbc.ipadx=0;
        gbc.ipady=0;
        gbc.insets=new Insets(5,5,0,0);
        gbl.setConstraints(b1,gbc);
        c.add(b1);

        b2=new JButton("2");
        b2.addActionListener(this);
        b2.setFocusable(false);
        gbc.gridx=1;
        gbc.gridy=1;
        gbc.gridwidth=1;
        gbc.ipadx=0;
        gbc.ipady=0;
        gbc.insets=new Insets(5,5,0,0);
        gbl.setConstraints(b2, gbc);
        c.add(b2);


        b3=new JButton("3");
        b3.addActionListener(this);
        b3.setFocusable(false);
        gbc.gridx=2;
        gbc.gridy=1;
        gbc.gridwidth=1;
        gbc.ipadx=0;
        gbc.ipady=0;
        gbc.insets=new Insets(5,5,0,0);
        gbl.setConstraints(b3, gbc);
        c.add(b3);

        b4=new JButton("4");
        b4.addActionListener(this);
        b4.setFocusable(false);
        gbc.gridx=0;
        gbc.gridy=2;
        gbc.gridwidth=1;
        gbc.ipadx=0;
        gbc.ipady=0;
        gbc.insets=new Insets(5,5,0,0);
        gbl.setConstraints(b4,gbc);
        c.add(b4);

        b5=new JButton("5");
        b5.addActionListener(this);
        b5.setFocusable(false);
        gbc.gridx=1;
        gbc.gridy=2;
        gbc.gridwidth=1;
        gbc.ipadx=0;
        gbc.ipady=0;
        gbc.insets=new Insets(5,5,0,0);
        gbl.setConstraints(b5, gbc);
        c.add(b5);


        b6=new JButton("6");
        b6.addActionListener(this);
        b6.setFocusable(false);
        gbc.gridx=2;
        gbc.gridy=2;
        gbc.gridwidth=1;
        gbc.ipadx=0;
        gbc.ipady=0;
        gbc.insets=new Insets(5,5,0,0);
        gbl.setConstraints(b6, gbc);
        c.add(b6);

        b7=new JButton("7");
        b7.addActionListener(this);
        b7.setFocusable(false);
        gbc.gridx=0;
        gbc.gridy=3;
        gbc.gridwidth=1;
        gbc.ipadx=0;
        gbc.ipady=0;
        gbc.insets=new Insets(5,5,0,0);
        gbl.setConstraints(b7,gbc);
        c.add(b7);

        b8=new JButton("8");
        b8.addActionListener(this);
        b8.setFocusable(false);
        gbc.gridx=1;
        gbc.gridy=3;
        gbc.gridwidth=1;
        gbc.ipadx=0;
        gbc.ipady=0;
        gbc.insets=new Insets(5,5,0,0);
        gbl.setConstraints(b8, gbc);
        c.add(b8);


        b9=new JButton("9");
        b9.addActionListener(this);
        b9.setFocusable(false);
        gbc.gridx=2;
        gbc.gridy=3;
        gbc.gridwidth=1;
        gbc.ipadx=0;
        gbc.ipady=0;
        gbc.insets=new Insets(5,5,0,0);
        gbl.setConstraints(b9, gbc);
        c.add(b9);


        b0=new JButton("0");
        b0.addActionListener(this);
        b0.setFocusable(false);
        gbc.gridx=0;
        gbc.gridy=4;
        gbc.gridwidth=1;
        gbc.ipadx=0;
        gbc.ipady=0;
        gbc.insets=new Insets(5,5,0,0);
        gbl.setConstraints(b0, gbc);
        c.add(b0);

        bplus=new JButton("+");
        bplus.addActionListener(this);
        bplus.setFocusable(false);
        bplus.setToolTipText("dodawanie");
        gbc.gridx=3;
        gbc.gridy=1;
        gbc.gridwidth=2;
        gbc.ipadx=30;
        gbc.ipady=0;
        gbc.insets=new Insets(5,5,0,0);
        gbl.setConstraints(bplus,gbc);
        c.add(bplus);


        bdot=new JButton(".");
        bdot.addActionListener(this);
        bdot.setFocusable(false);
        bdot.setToolTipText("kropka dziesiętna");
        gbc.gridx=1;
        gbc.gridy=4;
        gbc.gridwidth=1;
        gbc.ipadx=0;
        gbc.ipady=0;
        gbc.insets=new Insets(5,5,0,0);
        gbl.setConstraints(bdot, gbc);
        c.add(bdot);


        brow=new JButton("=");
        brow.addActionListener(this);
        brow.setFocusable(false);
        brow.setToolTipText("wykonaj działanie");
        gbc.gridx=3;
        gbc.gridy=5;
        gbc.gridwidth=2;
        gbc.ipadx=0;
        gbc.ipady=0;
        gbc.insets=new Insets(5,5,0,0);
        gbl.setConstraints(brow, gbc);
        c.add(brow);


        back=new JButton("←");
        back.addActionListener(this);
        back.setFocusable(false);
        back.setToolTipText("cofnij");
        gbc.gridx=2;
        gbc.gridy=5;
        gbc.gridwidth=2;
        gbc.ipadx=0;
        gbc.ipady=0;
        gbc.insets=new Insets(5,5,0,0);
        gbl.setConstraints(back, gbc);
        c.add(back);

//bminus, bmult, bdiv

        bminus=new JButton("-");
        bminus.addActionListener(this);
        bminus.setFocusable(false);
        bminus.setToolTipText("odejmowanie");
        gbc.gridx=3;
        gbc.gridy=2;
        gbc.gridwidth=2;
        gbc.ipadx=30;
        gbc.ipady=0;
        gbc.insets=new Insets(5,5,0,0);
        gbl.setConstraints(bminus,gbc);
        c.add(bminus);

        bmult=new JButton("*");
        bmult.addActionListener(this);
        bmult.setFocusable(false);
        bmult.setToolTipText("mnożenie");
        gbc.gridx=3;
        gbc.gridy=3;
        gbc.gridwidth=2;
        gbc.ipadx=30;
        gbc.ipady=0;
        gbc.insets=new Insets(5,5,0,0);
        gbl.setConstraints(bmult,gbc);
        c.add(bmult);

        bdiv=new JButton("/");
        bdiv.addActionListener(this);
        bdiv.setFocusable(false);
        bdiv.setToolTipText("dzielenie");
        gbc.gridx=3;
        gbc.gridy=4;
        gbc.gridwidth=2;
        gbc.ipadx=30;
        gbc.ipady=0;
        gbc.insets=new Insets(5,5,0,0);
        gbl.setConstraints(bdiv,gbc);
        c.add(bdiv);

        // JButton bproc, broot, bpower,

        bproc=new JButton("%");
        bproc.addActionListener(this);
        bproc.setFocusable(false);
        bproc.setToolTipText("dzielenie");
        gbc.gridx=2;
        gbc.gridy=4;
        gbc.gridwidth=1;
        gbc.ipadx=0;
        gbc.ipady=0;
        gbc.insets=new Insets(5,5,0,0);
        gbl.setConstraints(bproc,gbc);
        c.add(bproc);

        broot=new JButton("√");
        broot.addActionListener(this);
        broot.setFocusable(false);
        broot.setToolTipText("pierwiastkowanie");
        gbc.gridx=0;
        gbc.gridy=5;
        gbc.gridwidth=1;
        gbc.ipadx=0;
        gbc.ipady=0;
        gbc.insets=new Insets(5,5,0,0);
        gbl.setConstraints(broot, gbc);
        c.add(broot);

        bpower=new JButton("^");
        bpower.addActionListener(this);
        bpower.setFocusable(false);
        bpower.setToolTipText("potegowanie");
        gbc.gridx=1;
        gbc.gridy=5;
        gbc.gridwidth=1;
        gbc.ipadx=0;
        gbc.ipady=0;
        gbc.insets=new Insets(5,5,0,0);
        gbl.setConstraints(bpower, gbc);
        c.add(bpower);

        // bmemrc, bmemplus, bmemminus;


        bmemrc=new JButton("M");
        bmemrc.addActionListener(this);
        bmemrc.setFocusable(false);
        bmemrc.setToolTipText("z pamięci");
        gbc.gridx=0;
        gbc.gridy=6;
        gbc.gridwidth=1;
        gbc.ipadx=0;
        gbc.ipady=0;
        gbc.insets=new Insets(5,5,0,0);
        gbl.setConstraints(bmemrc, gbc);
        c.add(bmemrc);

        bmemplus=new JButton("M+");
        bmemplus.addActionListener(this);
        bmemplus.setFocusable(false);
        bmemplus.setToolTipText("dodaj do pamięci");
        gbc.gridx=1;
        gbc.gridy=6;
        gbc.gridwidth=1;
        gbc.ipadx=0;
        gbc.ipady=0;
        gbc.insets=new Insets(5,5,0,0);
        gbl.setConstraints(bmemplus, gbc);
        c.add(bmemplus);

        bmemminus=new JButton("M-");
        bmemminus.addActionListener(this);
        bmemminus.setFocusable(false);
        bmemminus.setToolTipText("usuń z pamięci");
        gbc.gridx=2;
        gbc.gridy=6;
        gbc.gridwidth=1;
        gbc.ipadx=0;
        gbc.ipady=0;
        gbc.insets=new Insets(5,5,0,0);
        gbl.setConstraints(bmemminus, gbc);
        c.add(bmemminus);

        bdelete=new JButton("C");
        bdelete.addActionListener(this);
        bdelete.setFocusable(false);
        bdelete.setToolTipText("usuń działanie");
        gbc.gridx=3;
        gbc.gridy=6;
        gbc.gridwidth=2;
        gbc.ipadx=0;
        gbc.ipady=0;
        gbc.insets=new Insets(5,5,0,0);
        gbl.setConstraints(bdelete, gbc);
        c.add(bdelete);


        f.pack();
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        f.setTitle("Kalk");
        f.setVisible(true);
    }

    public static void main(String[] args)
    {
        //do wersji 1.4
        //new Kalk().init();

        //od wersji 1.5
        SwingUtilities.invokeLater(new Runnable()
        {
            public void run()
            {
                new Kalk().init();
            }
        });
    }
}