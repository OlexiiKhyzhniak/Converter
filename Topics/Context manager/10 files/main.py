for i in range(1, 11):
    str_x = 'file' + str(i) + '.txt'
    with open(str_x, 'at') as f1:
        f1.write(str(i))
