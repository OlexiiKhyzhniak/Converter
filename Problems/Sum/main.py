# read sums.txt
file = open('sums.txt', 'r')
for line in file:
    num1, num2 = line.split()
    print(int(num1) + int(num2))
file.close()
