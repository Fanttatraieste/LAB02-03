from math import sqrt

# 5. Find the first twin numbers p1 and p2 after a given n

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


def FindTwins (n) :
    n += 1
    while(not (CheckPrime(n) and CheckPrime(n + 2))) :
        n += 1

    return (n, n + 2)

if __name__ == '__main__':
    print("5. We are going to find p1, p2 prime numbers such that p1 = p2 - 2 and n < p1 < p2")
    n = int (input ("n : "))
    pair = FindTwins(n)
    print("The numbers are %d and %d" % (pair[0], pair[1]))