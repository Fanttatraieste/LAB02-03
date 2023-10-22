from math import sqrt


# 13. Find the nth element of the sequence 1,2,3,2,2,5,2,2,3,3,3,7,2,2,3,3,3, ...

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

def CountPrimeDiv13(n) :
    if CheckPrime(n) : return 1;    # if n is prime, then it appears one time in the sequence

    count = 0

    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0 :
            if CheckPrime(i) :
                count += i  # if i is a prime divizor, then it appears i times in the sequence
            if n/i != i and CheckPrime((n/i)):
                count += (n/i)    # analog as for i

    return count

def FindDesired13(n,i):
    #   we are searching among n's Prime Divizors, and we return the ith one
    count = 0

    step = 2
    while count <= i :
        if (n % step == 0 and CheckPrime(step)) : count += step
        if (count >= i): return step
        step += 1

    return step

def Exercise13 (n) :
    # Ideea exercitiului este ca un numar prim se va repeta o singura data in secventa
    # Iar un numar compus de ex din i * j isi va repeta fiecare divizor i prim de i ori, j prim de j ori si tot asa

    if (n <= 3) : return n

    count = 3       # count va numara elementele din secventa
    step = 4        # step va parcurge numerele naturale

    while count <= n :
        #  In acest while vreau sa parcurg practic sirul format
        #  Count retine cate elemente am socotit deja
        #  nrEl calculeaza cate elemente urmeaza sa fie adaugate in sir, pt urm nr natural din secventa
        nrEl = CountPrimeDiv13(step)    #   nrEl calculeaza cate elemente urmeaza sa fie adaugate in sir conform urmatorului nr natural, fie el prim sau compus
        if count + nrEl >= n :          # Daca nr de elemente deja socotite, plus nr de el care urm sa fie adaugate depaseste n ( pozitia pe care o caut ), inseamna ca numarul dorit de returnat, se afla printre divizorii urmatorului nr natural, adica step
            return FindDesired13(step, n - count)    # returnez al i-lea divizor al lui step, i = n - count
        count += nrEl            # daca am ajuns aici, inseamna ca mai am de parcurs elemente, deci nrEl le contabilizez la el socotite
        step += 1                # trec la urmatorul nr natural

    return -1                       # in mod normal se face return in while, daca am ajuns aici, cv e gresit


if __name__ == '__main__':
    print("13. For a given n, we return the nth number of the sequence from ex 13")
    n = int(input("n = "))
    print("The resulult is : ", Exercise13(n))