from datetime import date

# 2. Given a birth date, calculate the age of a person in days

def CalculateAgeDays (BirthDate) :
    current = date.today()
    return (current - BirthDate).days

if __name__ == '__main__':
    print("2. We are going to calculate how many days have passed since your birthday. Please enter it : ")
    year = int(input("year : "))
    month = int(input("month : "))
    day = int(input("day: "))
    print("The number of days that have passed is : ", CalculateAgeDays(date(year, month, day)))