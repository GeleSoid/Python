from operator import mod
from random import random
from math import acos

class Calculator:
    def __init__(self):
        pass

    def abs(self,first):
        return abs(first)

    def fac(self,first):
        a = 0
        for i in range(first+1):
            a += i
        return a

    def rand(self):
        return int(random() * 100 // 1)

    def acos(self,first):
        return round(acos(first),6)

    def mainloop(self):
        while True:
            first = input()
            if first == 'random':
                print(Calc.rand)
                break
            first = int(first)
            oper = str(input())
            if oper == '+':
                second = int(input())
                print(first+second)
                break
            elif oper == '-':
                second = int(input())
                print(first-second)
                break
            elif oper == '*':
                second = int(input())
                print(first*second)
                break
            elif oper == '/':
                second = int(input())
                print(first/second)
                break
            elif oper == 'pow':
                second = int(input())
                print(pow(first,second))
                break
            elif oper == 'mod':
                print(Calc.abs(first))
                break
            elif oper == 'fac':
                print(Calc.fac(first))
                break
            elif oper == 'acos':
                print(Calc.acos(first))
                break

print('Для операций используются команды +,-,/,*,pow,mod,random,fac,arccos')
#WARNING! Незлья закрывать скобки до того, как введёте содержимое, иначе Python не распознает аргумент

Calc = Calculator()

Calc.mainloop()
