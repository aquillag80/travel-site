#SETUP - assign an integer variable for number and sum
total = 0
num = 0

#INPUT - ask the user for a series of numbers
print('Enter numbers one by one. Enter -1 to stop.')
while True:
    num = int(input('Enter a number. '))
    if num == -1:
        break
    if num >= 0:
        total += num
    
#PROCESSING - if the number is negative skip it, stop at -1
    
#OUTPUT - add the positive numbers
print('The sum of the positive numbers is: ',total)
