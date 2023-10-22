from math import sqrt


# 14. Find n1 > n, n is a given number from the keyboard, where n1 is a perfect number, meaning n1 is the sum of its divizors

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

def FindPerfectN(n) :
    n += 1
    while (not CheckPerfect(n)) : n += 1

    return n

if __name__ == '__main__':
    print("14. For a given n, find n1 > n, such that n1 is a perfect number")
    n = int(input("n = "))
    print("The result is : ", FindPerfectN(n))