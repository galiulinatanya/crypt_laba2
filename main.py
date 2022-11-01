from nis import match
import random   
import math
def checkPrimeNum(num):
    res = 1
    i = 2
    while i <= num ** 0.5 and res:
        if num % i == 0:
            res = 0
        i += 1
    return res

def fastPow(num, pow, div):
    res = 1
    while pow:
        if pow & 1 == 1:
            res = (res * num) % div
        num = (num * num) % div
        pow >>= 1
    return res

def checkPrimeRoot(num1, num2):
    i = 2
    primeNum = []
    n = num2 - 1
    res = 1
    while i * i <= n:
        while n % i == 0:
            primeNum.append(i)
            n = n // i
        i = i + 1
    if n > 1:
        primeNum.append(n)
    for el in primeNum:
        if fastPow(num1, num2 // el, num2) == 1:
            res = 0
    return res

def mutuallyPrimeNum(x, y):
    while x != y:
        if x > y:
            x -= y
        else:
            y -= x
    return x

print("Select a menu item")
print("1. Key generator")
print("2. Text encryption")
print("3. Text decryption")

item = int(input())
p, g = map(int, input('p, g: ').split())

if not checkPrimeNum(p):
    print("p isn't prime")
    exit()

if not checkPrimeRoot(g, p):
    print("g isn't primitive root p")
    exit()

random.seed()

match item:
    case 1:
        x = random.randint(2, p - 2)
        y = fastPow(g, x, p)
        print("privat key(x): ", x)
        print("public key(y): ", y)
    case 2:
        y = int(input("public key(y): "))
        m = int(input("messege(m): "))
        if m >= p:
            print("m must be less than p")
            exit()
        while True:
            k = random.randint(2, p - 2)
            if mutuallyPrimeNum(k, p - 1) == 1:
                break
        a = fastPow(g, k, p)
        b = (fastPow(y, k, p) * (m % p)) % p
        print("(a, b): (", a, ", ", b, ")", sep = '')
    case 3:
        x = int(input("privat key(x): "))
        a, b = map(int, input("(a, b): ").split())
        m = ((b % p) * fastPow(a, p - 1 - x, p)) % p
        print("messege(m): ", m)
    case _:
        print("There is no such item in the menu")
