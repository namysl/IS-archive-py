if [ `echo $1 | sed '/.a$/p' - | wc -l` -eq 2 ]
then echo 'Ostatnia litera to "a" !!!'
else echo '"A" nie jest ostatnia litera'
fi


