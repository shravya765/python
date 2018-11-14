year = int(input("enter a year:"))

if year % 4 != 0:
    print("Not a Leap year")
else:
    if year % 100 != 0 or year % 400 == 0:
        print("Leap year")