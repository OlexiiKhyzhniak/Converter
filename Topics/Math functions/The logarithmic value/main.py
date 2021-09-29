import math

number, base = abs(int(input())), int(input())
if base > 1:
    answer = math.log(number, base)
    print(round(answer, 2))
elif base <= 1:
    answer = math.log(number)
    print(round(answer, 2))
