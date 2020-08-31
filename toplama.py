# num1 = int(input('num1: '))
# num2 = int(input('num2: '))


def top(num1, *args):
    toplam = sum(args)
    return num1 + toplam


def top(num1, num2):
    return num1 + num2


# print(top(5, 5, 7, 8, 9))
print(top(1, 2))
