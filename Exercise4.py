from math import sqrt

# 4. Goldbach Conjecture. Given a integer n, find prime number p1 and p2 such as n = p1 + p2

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

def FindPrimeTuplet (n) :
    for i in range (n // 2) :
        if (CheckPrime(i)) :
            if (CheckPrime(n - i)) :
                return (i, n - i)

    return (-1, -1)

if __name__ == '__main__':
    print ("4. We are going to find p1, p2 prime numbers such that p1 + p2 = n for your given n")
    n = int(input("Please give an even n : "))
    pair = FindPrimeTuplet(n)
    print("The to numbers are %d and %d" % ( pair[0] , pair[1]))