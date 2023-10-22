from math import sqrt


# 16. Find the biggest perfect n lower than a given n from the keyboard

def CheckPerfect(n) :
    sum = 1
    for i in range(2, int(sqrt(n)) + 1):
        if (n % i == 0) :
            sum += (i + n/i)
        if (sum > n) :
            return False

    if (int(sqrt(n)) * int(sqrt(n)) == n) :
        sum += int(sqrt(n))

    return n == sum

def FindBigPerfectN(n) :
    n -= 1
    while (n > 1 and not CheckPerfect(n)) : n -= 1

    if (n == 1) : return -1
    return n

if __name__ == '__main__':
    print("16. For a given n, find the biggest n1, such that n1 < n and n1 is perfect")
    n = int(input("n = "))
    result = FindBigPerfectN(n)
    if result == -1:
        print("There is no prime number smaller than your input")
    else:
        print("The searched n1 is : ", result)