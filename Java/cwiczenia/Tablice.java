public class Tablice {
    public static void main(String[] args) {

        String [] tablica_stringow = new String[] {"aa", "bb", "cc", "dd", "ee"};
        System.out.println("adres tablicy STRINGOW: " + tablica_stringow);

        for (int i=0; i<tablica_stringow.length; i++){
            System.out.print(tablica_stringow[i] + " ");
        }
        System.out.println("\n");

        for (String s : tablica_stringow) {
            System.out.println(s + " ");
        }

        System.out.println("\nCHAR:\n");
        char [] tablica_char = new char[] {41, 42, 43};

        for (int i=0; i<tablica_char.length; i++){
            System.out.println(tablica_char[i]);
        }

        int [] tablica_int = new int[] {10, 11, 12, 13, 14, 15};

        for (int i=tablica_int.length-1; i>=0; i--){
            System.out.print(tablica_int[i] + " ");
        }


        System.out.println("\n");
        int [] tablica = new int[10];

        for (int i=0; i<10; i++){
            tablica[i] = i;
        }
        for(int i=0; i<10; i++){
            System.out.println(tablica[i]);
        }
    }
}
