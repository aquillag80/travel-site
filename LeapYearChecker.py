year = 0

year = int(input('Enter a year: '))



condition1 = year%4 == 0
condition2 = year%100 == 0
condition3 = year%400 == 0


if condition1: 
    if condition2:
        if condition3:
            print("Leap Year")
        else:
            print("Not a Leap Year")
    else:
        print("Leap Year")
else:
    print("Not a Leap Year")
