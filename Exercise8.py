from math import sqrt


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


if __name__ == '__main__':
    print("8. For a given n, calculate the maximum m, formed from the same digits")
    n = int(input("n : "))
    print("m = ", CalculateMaxDigits(n))