# hash, insert, find, remove

class BED:
    def __init__(self, bucket):
        self.bucket = bucket
        self.hashtable = [[] for _ in range(bucket)]

    def __repr__(self):
        return 'instancja klasy' + __class__.__name__

    def __str__(self):
        return str(self.hashtable)

    def parser(self):
        empty_list = []
        filepath = 'bed.txt'
        with open(filepath, 'r') as f:
            for line in f:
                if 'chr7' in line:
                    no_whitespace_text = line.replace('    ', ', ')
                    no_slash_n_text = no_whitespace_text.replace('\n', '')
                    empty_list.append(no_slash_n_text)
        del empty_list[0]
        return empty_list

    def hash(self):
        hash_list = []
        for string in self.parser():
            sum_of_all = 0
            for char in string:
                sum_of_all += ord(char)
            key = sum_of_all % self.bucket
            hash_list.append(key)
        return hash_list

    def insert(self):
        list_of_hash = self.hash()
        list_of_values = self.parser()

        for i in range(len(list_of_hash)):
            self.hashtable[list_of_hash[i]].append(list_of_values[i])

    def find(self, data):
        pass

    def remove(self, data):
        pass


bazaBED = BED(10)
print(bazaBED)
print(bazaBED.parser())
print(bazaBED.hash())
bazaBED.insert()
print(bazaBED)
print(bazaBED.find('127471196'))
