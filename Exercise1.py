from math import sqrt

# 1. Find the first prime number greater then a given number

def CheckPrime (n) :
    if (n == 2):
        return True
    if (n < 2):
        return False
    if (n % 2 == 0):
        return False

    for i in range (3, int(sqrt(n)) + 1, 2):
        if (n % i == 0):
            return False

    return True

def FindFirstPrime (n) :
    n += 1
    while CheckPrime(n) == False :
        n += 1

    return n

if __name__ == '__main__':
    n1 = int(input("1. We return the first prime number greater then n \n n = "))
    print("The requested prime number is : ", FindFirstPrime(n1))