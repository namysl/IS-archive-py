class Dodawanie {
    // dodaje do liczby
    double liczba;

    Dodawanie(int liczba){
        this.liczba = liczba;
    }

    public String toString(){
        return "liczba: " + liczba + " ";
    }

    public double dodaj(double liczba2){
        this.liczba = this.liczba + liczba2;
        return this.liczba;
    }

}
