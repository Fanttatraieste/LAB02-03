from math import sqrt


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
    print("11. For two given a and b, check if they are composed from the same digits")
    a = int(input("a = "))
    b = int(input("b = "))
    print("The result is : ", CheckDigits(a, b))