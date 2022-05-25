# Q1

grade = int(input("Enter the marks: "))

if grade < 25:
    print("Your grade is: F")
elif (grade >= 25) & (grade < 45):
    print("Your grade is: E")
elif (grade >= 45) & (grade < 50):
    print("Your grade is: D")
elif (grade >= 50) & (grade < 60):
    print("Your grade is: C")
elif (grade >= 60) & (grade < 80):
    print("Your grade is: B")
elif (grade >= 80):
    print("Your grade is: A")
else:
    print("Invalid Input")
print("\n\n")



# Q2

yr = int(input("Enter the year: "))

if yr%4 == 0:
    if yr%100 == 0:
        if yr%400 == 0:
            print(str(yr) + " is a leap year")
        else:
            print(str(yr) + " is not a leap year")
    else:
        print(str(yr) + " is a leap year")
else:
    print(str(yr) + " is not a leap year")
print("\n\n")



# Q3

from random import randint

for i in range(1,11):
    n1 = randint(1,10)
    n2 = randint(1,10)
    
    print("Q" + str(i) + " is: " + str(n1) +"x"+ str(n2) + " = ")
    answer = int(input())
    if answer == n1*n2:
        print("Right!")
    else:
        print("Wrong!")
print("\n\n")



# Q4


for i in range(200):
    if i%5 == 2:
        if i%6 == 3:
            if i%7 == 2:
                print("There are " + str(i) + " candies in total")
print("\n\n")
