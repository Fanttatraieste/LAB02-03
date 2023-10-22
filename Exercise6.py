from math import sqrt

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

if __name__ == '__main__':

    print("6. Find the smallest m, where m belongs to the fibonacci sequence and m > n")
    n = int(input("n : "))
    print("The smallest m is ", FindSmallestFibo(n))