from math import sqrt


# 15. Find the biggest prime number lower than a given n from the Keyboard

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

def FindBigPrime(n):
    n -= 1
    while (not CheckPrime(n) and n > 1): n -= 1

    if n == 1 : return -1
    else : return n


if __name__ == '__main__':
    print("15. For a given n, find the biggest n1, such that n1 < n and n1 is prime")
    n = int(input("n = "))
    result = FindBigPrime(n)
    if result == -1:
        print("There is no prime number smaller than your input")
    else:
        print("The searched n1 is : ", result)