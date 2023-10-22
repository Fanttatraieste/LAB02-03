import datetime
from datetime import date

# 3. Calculate a date (year, month, day) after you are given a year and the ith day in that year
def CalculateDate (year, days) :
    first = date(year, 1, 1)
    return first + datetime.timedelta(days=days)

if __name__ == '__main__':
    print("3. We are going to calculate a date, after you give us a year, and the ith day of that year")
    year = int(input("year : "))
    day = int(input("ith day : "))
    print("The date is : ", CalculateDate(year, day))