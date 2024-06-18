#Name
#Date
#Description

#Setup
#Create a variable called score is dataype decimal and intial value is 0
#Create a string variable called grade, inital value ""


#Input
#Ask the user to enter a numerical score

#Processing
#If score greater than or equal to  92 grade is A
#else if score is greater than or equal to 82 grade is B
#else if score is greater than or equal to 72 grade is C
#else if score is greater than or equal to 62 grade is D
#else if score is less than or equal to 61 grade is F

#Output
#print letter grade

score = 0.0
Grade = ""
score = float(input("Please enter a numeric grade: "))
if score >= 92:
    print('A')
elif score >= 82:
    print('B')
elif score >= 72:
    print('C')
elif score >= 62:
    print('D')
else:
    print('F')
