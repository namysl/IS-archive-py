myProgram: main.o employee.o address.o employee.h address.h
	g++ -o myProgram main.o employee.o address.o

main.o: main.cpp address.h employee.h
	g++ -c main.cpp

employee.o: employee.cpp address.h
	g++ -c employee.cpp

address.o: address.cpp  
	g++ -c address.cpp




