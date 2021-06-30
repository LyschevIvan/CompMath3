import matplotlib.pyplot as plt
import numpy as np


class Equation:
    def __init__(self):
        self.x1 = 0
        self.x2 = 0
        self.x3 = 0
        self.c = 0
        self.a = 0
        self.b = 1
        self.fault = 0.001


    def f_back(self, x):
        return self.x3 * pow(x, 4)/4 + self.x2 * pow(x, 3) / 3 + self.x1 * pow(x, 2) /2 + self.c * x

    def f(self, x):
        return self.x3 * pow(x, 3) + self.x2 * pow(x, 2) + self.x1 * x + self.c

    def f1(self, x):
        return 3 * self.x3 * pow(x, 2) + 2 * self.x2 * x + self.x1

    def f2(self, x):
        return 6 * self.x3 * x + 2 * self.x2

    def to_string(self):
        print("Equation{" +
              "x3=" + str(self.x3) +
              ", x2=" + str(self.x2) +
              ", x1=" + str(self.x1) +
              ", c=" + str(self.c) +
              ", a=" + str(self.a) +
              ", b=" + str(self.b) +
              ", fault=" + str(self.fault) +
              '}')





def printGraph(equation):
    fig, ax = plt.subplots()
    x = np.linspace(equation.a, equation.b, 1000)
    y = equation.f(x)
    ax.plot(x, y)
    plt.show()


def whiler(func, equation, k):
    I0 = func(equation, k)[1]
    k *= 2
    result, I1 = func(equation, k)
    print(result)
    while abs(I1 - I0) > equation.fault:
        I0 = I1
        k*=2
        result , I1 = func(equation, k)
        print(result)

    return result


def left_rect(equation, n):
    h = (equation.b - equation.a) / n
    x = equation.a
    k = 1
    summ = 0
    result = ""
    for i in range(n):
        summ += equation.f(x) * h
        # result += "{}. x = {}   f(x) = {}   summ = {} \n".format(k, x, equation.f(x), summ)
        k += 1
        x += h

    result += "S = {} n = {} \n".format(summ, n)

    return result, summ

def right_rect(equation, n):
    h = (equation.b - equation.a) / n
    x = equation.a + h
    k = 1
    summ = 0
    result = ""
    for i in range(n):
        summ += equation.f(x) * h
        # result += "{}. x = {}   f(x) = {}   summ = {} \n".format(k, x, equation.f(x), summ)
        k += 1
        x += h

    result += "S = {} n = {} \n".format(summ, n)
    return result, summ

def middle_rect(equation, n):
    h = (equation.b - equation.a) / n
    x = equation.a + h/2
    k = 1
    summ = 0
    result = ""
    for i in range(n):
        summ += equation.f(x) * h
        # result += "{}. x = {}   f(x) = {}   summ = {} \n".format(k, x, equation.f(x), summ)
        k += 1
        x += h

    result += "S = {} n = {} \n".format(summ, n)
    return result, summ


def trapeze(equation, n):
    h = (equation.b - equation.a) / n
    x =equation.a + h
    k = 1
    summ = equation.f(equation.a) * h / 2
    result = ""
    for i in range(n-1):
        summ += equation.f(x) * h
        # result += "{}. x = {}   f(x) = {}   summ = {} \n".format(k, x, equation.f(x), summ)
        k += 1

        x += h
    summ += equation.f(equation.b) * h / 2
    # result += "{}. x = {}   f(x) = {}   summ = {} \n".format(k, x, equation.f(x), summ)
    result += "S = {} n = {} \n".format(summ, n)
    return result, summ


def simpson(equation, n):
    h = (equation.b - equation.a) / n
    x = equation.a
    k = 1
    summ = equation.f(x) * h / 3
    result = ""
    x += h
    for i in range(n - 1):
        if i % 2 == 0:
            summ += equation.f(x) * h * 4 / 3
        else:
            summ += equation.f(x) * h * 2 / 3
        # result += "{}. x = {}   f(x) = {}   summ = {} \n".format(k, x, equation.f(x), summ)
        k += 1
        x += h
    summ += equation.f(x) * h / 3
    # result += "{}. x = {}   f(x) = {}   summ = {} \n".format(k, x, equation.f(x), summ)
    result += "S = {} n = {} \n".format(summ, n)
    return result, summ



if __name__ == '__main__':
    n = 10
    print("Ввести файлы из файла( или из консоли) (y/n)?")
    inp = input().lower()
    equation = Equation()
    if inp == 'y':
        with open("./input.txt", 'r') as file:
            equation.x3, equation.x2, equation.x1, equation.c = map(float, file.readline().split())
            equation.a, equation.b = map(float, file.readline().split())
            equation.fault = float(file.readline())

    else:
        print("Для отделения дробной части используйте .")
        print("Введите коэффициент при x³: ")
        equation.x3 = float(input())
        print("Введите коэффициент при x²: ")
        equation.x2 = float(input())
        print("Введите коэффициент при x: ")
        equation.x1 = float(input())
        print("Введите свободный член: ")
        equation.c = float(input())
        print("Введите левую границу: ")
        equation.a = float(input())
        print("Введите правую границу: ")
        equation.b = float(input())
        print("Введите n: ")
        equation.fault = float(input())

    equation.to_string()
    while True:
        result = ""
        print("Выберите метод:\n" +
              "•0 Прямое вычисление\n" +
              "•1 Метод прямоугольников левый\n" +
              "•2 Метод прямоугольников правый\n" +
              "•3 Метод прямоугольников \n" +
              "•4 Метод трапеций\n" +
              "•5 Метод Симпсона\n" +
              "exit – выход")

        inp = input().lower()
        if inp == "0":
            result = "S = F(b) - F(a) = {}".format(equation.f_back(equation.b) - equation.f_back(equation.a))

        elif inp == "1":
            result = whiler(left_rect, equation, 2)

        elif inp == "2":
            result = whiler(right_rect, equation, 2)

        elif inp == "3":
            result = whiler(middle_rect, equation, 2)

        elif inp == "4":
            result = whiler(trapeze, equation, 2)

        elif inp == "5":
            result = whiler(simpson, equation, 4)

        elif inp == "exit":
            break

