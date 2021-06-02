from math import prod
from time import time

def pnum(n):
    pnum = []
    for i in range(2,n):
        if isprime(i):
            pnum.append(i)
    yield pnum
    

def isprime (n):
    divisivel = 0

    for i in range(1,(n+1)):
        if n % i == 0:
            divisivel += 1
        if divisivel == 3:
            return False

    if divisivel == 2:
        return True
    else:
        return False


def fatorar(n):
    num = abs(round(n))
    numround = round(num/2)

    for p in pnum(numround):
        for n in p:
            if num % n == 0:
                num = num/n
                return n
        else:
            return num


def main(n):
    num = abs(n)
    fatores = []
    while prod(fatores) != n:
        fator = fatorar(num)
        fatores.append(fator)
        num = num/fator
    return fatores


def teste(teste = 101_127_319):
    t0 = time()
    print(f"O produto de {main(teste)} é {prod(main(teste))}")
    t = time()
    dt = t-t0
    print(f'Demorou {dt:.2f} s')

teste()
