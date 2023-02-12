import math


def choose(answer):
    if answer == "Y":
        b = True
        return b
    elif answer == "N":
        print("Program just stopped")
        b = False
        return b
    else:
        print('You can choose between "Y" - Yes and "N" - No. Relax and try again')
        return answer


def Discriminant(first, second, third):
    d = (second * second) - 4 * first * third
    try:
        math.sqrt(d)
    except ValueError:
        print("Discriminant < 0, try again")
        main()
    return math.sqrt(d)


def Arguments_of_quadratic_equation(pervoe, vtoroe, tretye):
    dis = Discriminant(pervoe, vtoroe, tretye)
    x1 = ((-1) * vtoroe - dis) / (2 * pervoe)
    x2 = ((-1) * vtoroe + dis) / (2 * pervoe)
    return print(x1, x2)


def main():
    b: bool = True
    while b:
        a = int(input('Enter "a" value: '))
        b = int(input('Enter "b" value: '))
        c = int(input('Enter "c" value: '))
        Arguments_of_quadratic_equation(a, b, c)
        ask = input('You wanna try again? Enter "Y" if Yes and "N" if No: ')
        b = choose(ask)


main()
