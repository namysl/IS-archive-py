interface Przeszukiwalne
    // do czego sluzy:
    // interfejsy pozwalaja na wielokrotne dziedziczenie
    // interfejsy maja puste metody, a klasy, ktore korzystaja z danego interfejsu musza zawierac wszystkie te metody
{
    boolean czyPasuje(String wzorzec);
}

