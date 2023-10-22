from math import sqrt


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


if __name__ == '__main__':
    print("7. Calculate the product of n's divisors, except for n itself")
    n = int(input("n : "))
    print("The product is : ", CalculateDivProd(n))