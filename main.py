import datetime
from math import sqrt
from datetime import date

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

# 2. Given a birth date, calculate the age of a person in days

def CalculateAgeDays (BirthDate) :
    current = date.today()
    return (current - BirthDate).days

# 3. Calculate a date (year, month, day) after you are given a year and the ith day in that year
def CalculateDate (year, days) :
    first = date(year, 1, 1)
    return first + datetime.timedelta(days=days)

# 4. Goldbach Conjecture. Given a integer n, find prime number p1 and p2 such as n = p1 + p2
def FindPrimeTuplet (n) :
    for i in range (n // 2) :
        if (CheckPrime(i)) :
            if (CheckPrime(n - i)) :
                return (i, n - i)

    return (-1, -1)

# 5. Find the first twin numbers p1 and p2 after a given n
def FindTwins (n) :
    n += 1
    while(not (CheckPrime(n) and CheckPrime(n + 2))) :
        n += 1

    return (n, n + 2)

# 6. Find the smallest m number from the Fibonacci sequence, where m > n (a given n)
def FindSmallestFibo (n) :
    f1 = 1
    f2 = 1
    f3 = f1 + f2
    while (f3 <= n) :
        f1 = f2
        f2 = f3
        f3 = f1 + f2

    return f3

# 7. Calculate the product of n's divisors (except for n itself)
def CalculateDivProd (n) :
    prod = 1
    i = 2
    while (i * i < n) :
        if (n % i == 0) :
            prod *= i
            prod *= (n // i)
        i+=1

    if (i * i == n):
        prod *= i

    return prod

# 8. For a given n, find the maximum m formed from the same digits as n
def CalculateMaxDigits (n) :
    nStr = str(n)
    digits = list(nStr)
    digits = [int(digit) for digit in digits]
    digits.sort(reverse=True)

    nr = 0
    for digit in digits:
        nr = nr * 10 + digit
    return nr

# 9. For a given n, calculate its palindrom
def Palindrom(n) :
    pal = 0

    while(n != 0) :
        cif = n % 10
        n //= 10
        pal = pal * 10 + cif


    return pal

# 10. For a given n, calculate the minimum m, formed from the same digits
def CalculateMinDigits(n) :
    # we will use a hashmap
    digitMap = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
    while (n > 0):
        cif = n % 10
        n //= 10
        digitMap[str(cif)] = digitMap.get(str(cif)) + 1

    mini = 10
    # print(digitMap)
    for key in digitMap :
        if (key != '0' and digitMap[key] != 0) :
            mini = int(key)
            digitMap[key] = digitMap.get(key) - 1
            break
    # print(digitMap)


    for key in digitMap :
        while(digitMap[key] > 0) :
            mini = mini * 10 + int(key)
            digitMap[key] = digitMap.get(key) - 1

    return mini

# 11. Check if two given numbers are composed from the same digits
def CheckDigits(a,b):
    mapA = {}
    mapB = {}
    for i in range(9):
        mapA[i] = 0
        mapB[i] = 0

    while a > 0 and b > 0:
        cifa = a % 10
        cifb = b % 10
        a //= 10
        b //= 10
        print(b)
        mapA[cifa] += 1
        mapB[cifb] += 1

    if a > 0 : return False
    if b > 0 : return False

    for i in range(9) :
        if mapA[i] != mapB[i]:
            return False

    return True

if __name__ == '__main__':
    # n1 = int(input("1. We return the first prime number greater then n \n n = "))
    # print("The requested prime number is : ", FindFirstPrime(n1))
    #
    # print("2. We are going to calculate how many days have passed since your birthday. Please enter it : ")
    # year = int(input("year : "))
    # month = int(input("month : "))
    # day = int(input("day: "))
    # print("The number of days that have passed is : ", CalculateAgeDays(date(year, month, day)))
    #
    # print ("3. We are going to calculate a date, after you give us a year, and the ith day of that year")
    # year = int(input("year : "))
    # day = int(input("ith day : "))
    # print("The date is : ", CalculateDate(year, day))
    #
    # print ("4. We are going to find p1, p2 prime numbers such that p1 + p2 = n for your given n")
    # n = int(input("Please give an even n : "))
    # pair = FindPrimeTuplet(n)
    # print("The to numbers are %d and %d" % ( pair[0] , pair[1]))
    #
    # print("5. We are going to find p1, p2 prime numbers such that p1 = p2 - 2 and n < p1 < p2")
    # n = int (input ("n : "))
    # pair = FindTwins(n)
    # print("The numbers are %d and %d" % (pair[0], pair[1]))
    #
    # print("6. Find the smallest m, where m belongs to the fibonacci sequence and m > n")
    # n = int(input("n : "))
    # print("The smallest m is ", FindSmallestFibo(n))

    # print("7. Calculate the product of n's divisors, except for n itself")
    # n = int(input("n : "))
    # print("The product is : ", CalculateDivProd(n))

    # print("8. For a given n, calculate the maximum m, formed from the same digits")
    # n = int(input("n : "))
    # print("m = ", CalculateMaxDigits(n))

    # print("9. For a given n, calculate its palindrom")
    # n = int(input("n : "))
    # print("Palindrom : ", Palindrom(n))

    # print("10. For a given n, calculate the minimum numbers formed from the same digits")
    # n = int(input("n : "))
    # print("Minimum is : ", CalculateMinDigits(n))

    # print("11. For two given a and b, check if they are composed from the same digits")
    # a = int(input("a = "))
    # b = int(input("b = "))
    # print("The result is : ", CheckDigits(a,b))
