from math import sqrt


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


if __name__ == '__main__':
    print("10. For a given n, calculate the minimum numbers formed from the same digits")
    n = int(input("n : "))
    print("Minimum is : ", CalculateMinDigits(n))