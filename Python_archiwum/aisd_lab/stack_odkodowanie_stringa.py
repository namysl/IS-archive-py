class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            self.items.pop()
        else:
            return Exception('pusty stos')

    def peak(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return Exception('pusty stos')

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


def odkoduj(tekst):
    liczby = Stack()
    litery = Stack()
    string = ''

    for znak in tekst:
        if znak.isdigit():
            liczby.push(int(znak))

        elif znak == ']':
            temp = ''
            liczba = 0

            if not liczby.is_empty():
                liczba = liczby.peak()
                liczby.pop()

            while not litery.is_empty() and litery.peak() != '[':
                temp = litery.peak() + temp
                litery.pop()

            if not litery.is_empty() and litery.peak() == '[':
                litery.pop()

            for _ in range(liczba):
                string = string + temp
                #print(string)

            for i in range(len(string)):
                litery.push(string[i])
                #print(litery.items)

            string = ''

        elif znak == '[':
            litery.push(znak)

        else:  # litery
            litery.push(znak)

    while not litery.is_empty():
        string = litery.peak() + string
        litery.pop()

    return string


#print(odkoduj('3[a]2[bc]'))
print(odkoduj('3[a2[c]]'))
#print(odkoduj('2[abc]3[cd]ef'))
