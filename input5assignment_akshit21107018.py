#Q1
print("\nQ1 Program to reverse the string.")
string = input("Enter the string: ")
string = string[::-1]
print("The reversed string is: ", string)





#Q2
print("\nQ2 Python Program to Print all Numbers in a Range Divisible by a Given Number. (user inputs the range and the number)")
n1 = int(input("Enter the upper range: "))
n1 += 1
n2 = int(input("Enter the lower range: "))
n3 = int(input("Enter the number to divide by:- "))

for i in range(n2,n1):
    if (i%n3==0):
        print(i)




#Q3
print("\nQ3 Program to calculate the area of a triangle using heron’s formula. (check condition if the combination of sides is possible).")
s1 = int(input("Enter side 1: "))
s2 = int(input("Enter side 2: "))
s3 = int(input("Enter side 3: "))
condition = (((s1+s2)>s3)and((s1+s3)>s2)and((s2+s3)>s1))
if condition == True:
    s = (s1+s2+s3)/2
    area = ((s*(s-s1)*(s-s2)*(s-s3))**0.5)
    print("The area of the triangle is: ", area)
else:
    print("Invalid Input: Sides not possible.")




#Q4
print("\nQ4 Write a Python program to construct the following pattern, using a nested for loop.")
n = 5
for i in range(n):
    for j in range(i):
        print("*",end="")
    print("")
for i in range(n,0,-1):
    for j in range(i):
        print("*",end="")
    print("")




#Q5
print("\nQ5 Write a python program to print a triangular pattern of the alphabet (user input the number of rows).")
x = int(input("Enter the number of rows: "))
z = 65
for i in range(0,x+1):
    for j in range(i):
        print(chr(z), end="") 
        z += 1   
        if (z-64)%26 == 0:
            z = 65
    print("")




        
#Q6 
print("\nQ6 Write a python program to print the prime numbers for a user input range.")
lower = int(input ("Enter the Lowest Range Value: "))  
upper = int(input ("Enter the Upper Range Value: "))  

if upper>0 and lower>0:
    if upper>lower:
        print ("The Prime Numbers in the range are: ")  
        for number in range (lower, upper + 1):  
            if number > 1:  
                for i in range (2, number):  
                    if (number % i) == 0:  
                        break  
                else:  
                    print (number)  
    else:
        print("Invalid inputs: Upper range should be larger than lower range.")
else:
    print("Invalid inputs: Ranges should be positive.")




#Q7
print("\nQ7 Write a python program to find the numbers which are multiple of 7 and divisible by 11 in the range 1-500.")
for z in range(1,500):
    if z%77 == 0:
        print(z)




#Q8
print('''\nQ8 Input 10 integer values from the user. Write a python program to find and print the following:

a. positive numbers
b. negative numbers
c. odd numbers
d. even numbers
e. Number of times each number occurs in the List''')
list = []
for i in range(10):
    z = int(input("Enter the number: "))
    list.append(z)
print("The negative numbers are: ")
for j in list:
    if j < 0:
        print(j)
print("The positive numbers are: ")
for j in list:
    if j > 0:
        print(j)
print("The odd numbers are: ")
for j in list:
    if j%2!=0:
        print(j)
print("The even numbers are: ")
for j in list:
    if j%2==0:
        print(j)
print("\n")
for j in list:
    count = list.count(j)
    print(j, "occurs", count, "times")
    

    
#Q9
print("\nQ9 Write a program to count the number of occurrences of each word in the list(List entered by the user).")
list_new = []
n = int(input("Enter the range of words in list: "))
for i in range(n):
    z = input("Enter the word to be added in list: ")
    list_new.append(z)
word = input("Enter the word to be counted: ")
count_list = list_new.count(word)
print(word,"occurs",count_list,"times")
