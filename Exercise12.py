from math import sqrt


# 12.
def CheckPrime(x):
    #   we check if x is prime
    if (x < 2 or (x % 2 == 0 and x != 2)): return False
    for i in range(3, int(sqrt(x)) + 1, 2) :
        if x % i == 0 : return False

    return True
def CountPrimeDiv(x):
    #     We return the num of prime div of x
    if (CheckPrime(x)) : return 1
    count = 0
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0 :
            if CheckPrime(i) :
                count += 1
            if x/i != i and CheckPrime((x/i)):
                count += 1

    # if (int(sqrt(x)) * int(sqrt(x)) == x and CheckPrime(int(sqrt(x)))) : return count + 1
    return count
def FindDesired(n,i):
    #   we are searching among n's Prime Divizors, and we return the ith one
    count = 0
    if (n % 2 == 0) : count = 1
    if (i == 1 and count == 1): return 2
    step = 3
    while count <= i :
        if (n % step == 0 and CheckPrime(step)) : count += 1
        if (count == i): return step
        step += 2

    return step

def FindNthElement(n) :
    if (n <= 3) : return n

    count = 3
    step = 4

    while count <= n :
        nrDiv = CountPrimeDiv(step)
        if (count + nrDiv >= n) :
            return FindDesired(step, n - count)
        count += nrDiv
        step += 1

    return -1


if __name__ == '__main__':
    print("12. For a given n, we return the nth number of the sequence from ex 12")
    n = int(input("n = "))
    print("the result is : ", FindNthElement(n))