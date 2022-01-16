import java.io.*;

public class Macierz {
    static int m = 3;
    static int n = 3;
    int[][] macierz;

    Macierz() {
        macierz = new int[m][n];
    }

    Macierz(int[][] macierz) {
        this.macierz = macierz;
    }

    public void pokaz() {
        //Wyswietla macierz
        int licznik = 0;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(macierz[i][j] + " ");
                licznik++;

                if (licznik == 3) {
                    System.out.print("\n");
                    licznik = 0;
                }
            }
        }
    }

    public void wypelnij_podanymi(int[][] tablica) {
        //Wypelnia macierz wartosciami podanymi w tablicy
        for (int i = 0; i < m; i++) {
            if (n >= 0) System.arraycopy(tablica[i], 0, macierz[i], 0, n);
        }
    }

    public void zmien_jedna_wartosc(int wartosc, int rzad, int kolumna) {
        //Metoda pozwala na podmienienie starej wartosci
        //na nowa wartosc w wybranym rzedzie i kolumnie
        macierz[rzad][kolumna] = wartosc;
    }

    public void wypelnij_nowymi_wartosciami() {
        //Metoda pozwala na podmiane wartosci macierzy na nowe
        //poprzez input uzytkownika
        try {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    System.out.print("Podaj wartosc w " + "[" + i + "]" + "[" + j + "]: ");
                    String wartosc = br.readLine();
                    int wartosc_int = Integer.parseInt(wartosc);
                    macierz[i][j] = wartosc_int;
                }
            }
        } catch (IOException e1) {
            System.out.println("wyjatek operacji wejscia/wyjscia");
        } catch (NumberFormatException e2) {
            System.out.println("nieprawidlowy format liczby");
        }
    }

    public int[][] transpozycja() {
        //Zwraca tablice z transponowana macierza
        int[][] transponowana = new int[3][3];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                transponowana[j][i] = macierz[i][j];
            }
        }
        return transponowana;
    }

    Macierz dodawanie(Macierz obj2) {
        //Dodaje dwie macierze 3x3
        int[][] wynik = new int[3][3];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                wynik[i][j] = this.macierz[i][j] + obj2.macierz[i][j];
            }
        }
        return new Macierz(wynik);
    }

    Macierz odejmowanie(Macierz obj2) {
        //Odejmuje macierze 3x3
        int[][] wynik = new int[3][3];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                wynik[i][j] = this.macierz[i][j] - obj2.macierz[i][j];
            }
        }
        return new Macierz(wynik);
    }

    Macierz mnozenie(Macierz obj2) {
        //Mnozy dwie macierze i zwraca wynik jako nowy obiekt
        int[][] wynik = new int[3][3];
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                for (int h = 0; h < 3; h++) {
                    wynik[i][j] += this.macierz[i][h] * obj2.macierz[h][j];
                }
            }
        }
        return new Macierz(wynik);
    }

    double wyznacznik() {
        //Oblicza wyznacznik macierzy
        int x, y, z;

        x = (macierz[0][0] * (macierz[1][1] * macierz[2][2] - macierz[1][2] * macierz[2][1]));
        y = (macierz[0][1] * (macierz[1][0] * macierz[2][2] - macierz[1][2] * macierz[2][0]));
        z = (macierz[0][2] * (macierz[1][0] * macierz[2][1] - macierz[1][1] * macierz[2][0]));
        return (x - y + z);
    }
}
