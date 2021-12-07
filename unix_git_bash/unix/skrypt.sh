#!/bin/bash

echo Siema swiecie!!!
zmienna="No siema, tu zmienna globalna"

function bash {
	local zmienna="A tu zmienna lokalna"
	echo $zmienna
}

echo $zmienna
bash

# tutaj jest komentarz

echo
echo

# jak masz predefiniowane zmienne,
# to musisz wywolac skrypt razem z wartosciami dla tych zmiennych
# na przyklad: ./skrypt.sh bash to kurwa

echo 'no to przejdzmy do wywolywania skryptu z jakimis argumentami'
echo $zmienna1 $zmienna2 $zmienna3 ' -> echo $zmienna1 $zmienna2 $zmienna3'

# argumenty mozna trzymac tez w takiej dziwnej tablicy:
args=("$@")

#echo argumentow w shell
echo ${args[0]} ${args[1]} ${args[2]} ' -> args=("$@"); echo ${args[0]} ${args[1]} ${args[2]}'

#jak zrobisz $@, to wyprintujesz wszystkie argumenty
echo $@ ' -> echo $@'

# a $# zwroci ile argumentow przekazalas przy wywolywaniu skryptu
echo Ile podano argumentow: $# ' -> echo Ile podano argumentow: $#'

echo
echo

echo 'jak wykonywac komendy z poziomu skryptu?'
echo 'robisz tak: echo `ls ~`'

echo `ls ~`

echo
echo

echo czytanie inputow
echo "Wpisz jedno slowo"
read slowo
echo "Wpisane slowo: $slowo"
echo
echo -e "Wpisz dwa slowa"
read slowo1 slowo2
echo "Wpisane slowa: \"$slowo1\", $slowo2"
echo
echo "Wpisuj cokolwiek do $ REPLY"
read
echo "Wpisano do defaultowej zmiennej $ REPLY: $REPLY"
echo
echo "Czas na read -a -> wpisuje kazde slowo oddzielone spacja do array"
read -a cokolwiek
echo "Tutaj sa dwa pierwsze slowa: ${cokolwiek[0]}, ${cokolwiek[1]}"


echo KONIEC
