from math import sqrt


# 9. For a given n, calculate its palindrom
def Palindrom(n) :
    pal = 0

    while(n != 0) :
        cif = n % 10
        n //= 10
        pal = pal * 10 + cif


    return pal


if __name__ == '__main__':
    print("9. For a given n, calculate its palindrom")
    n = int(input("n : "))
    print("Palindrom : ", Palindrom(n))