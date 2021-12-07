abstract class Figura //nie mozna tworzyc instancji tej klasy 
{
    abstract double pole(); //metoda abstrakcyjna
    abstract double obwod();

    void info()
    {
        System.out.println(this);
    }
}

/*

Nie mozna tworzyc obiektow z klasy abstrakcyjnej,
sluzy do dziedziczenia i jest generalizacja klas,
ktore z niej dziedzicza

 */