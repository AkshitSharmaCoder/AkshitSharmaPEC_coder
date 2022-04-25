# QUESTION 1
print("enter first number: ")
num1 = int(input())
print("enter second number: ")
num2 = int(input())
print("enter third number: ")
num3 = int(input())
avg= (num1+num2+num3)/3
print("the average of three numbers: \n", avg)
print("\n\n")

#QUESTION 2
print("enter your gross income: ")
gross_income= int(input())
print("enter your dependants: ")
dependants= int(input())
taxable_income= gross_income-10000-(3000*dependants)
print("Your taxable income will be: \n", taxable_income)
print("your tax is: ", taxable_income*20/100, "\t(taxable income: ", taxable_income, ")")
print("\n\n")

# QUESTION NO.3
print ("This program ask's the user for thenumber of seconds and prints out how many minutes and seconds that is equal to")
print("Enter the number of seconds you want to convert:")
var1=int(input())
print("This is equal to :")
print(var1//60, "Minutes", var1%60," Seconds")
print("\n\n")

# QUESTION NO.4
print(str( 25 + int('25') + int(25.0) ))
print("\n\n")

#QUESTION 5
import math as mt
for angle in range(0,360, 15):
    rad = mt.radians(angle)     
    print(angle, '---', round(mt.sin(rad),4), round(mt.cos(rad),4))  

    
