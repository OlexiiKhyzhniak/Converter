# read animals.txt
# and write animals_new.txt
file, file_new = open('animals.txt', 'r'), open('animals_new.txt', 'w')
list_1 = list()

for x in file:
    b = x.rstrip('\n') + ' '
    file_new.write(b)

file.close()
file_new.close()
