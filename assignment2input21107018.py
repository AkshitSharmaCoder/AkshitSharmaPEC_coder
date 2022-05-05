#QUESTION 1 
string="Python is a case sensitive language"
length=len(string)
print("a.  length of the input string is ",length)
x=string[::-1]
print("b.  reverse order of the input string  --> ",x)
x=string[10:26]
print("c.  New string =",x)
x=string.replace("a case sensitive" , "object oriented")
print("d. ",x)
x=string.find("a")
print("e.  index of substring a in input string  --> ",x)
x=string.replace(" " , "")
print("f. ",x)

print("\n\n")

#QUESTION 2
_name=str(input("enter your name: "))
_SID=int(input("enter your SID: "))
_branch=str(input("enter your department: "))
_CGPA=float(input("enter your CGPA: "))
print("Hey, ",_name," here!")
print("My SID is ",_SID,)
print("I am from ",_branch," department and my CGPA is ",_CGPA)

print("\n\n")

#QUESTION 3
a=56
b=10
print("a.  a&b  -->  ",a&b)
print("b.  a|b  -->  ",a|b)
print("c.  a^b  -->  ",a^b)
print("d. left shift a with 2 bits (a<<2)  -->  ",a<<2)
print("   left shift b with 2 bits (b<<2)  -->  ",b<<2)
print("e. right shift a with 2 bits (a>>2)  -->  ",a>>2)
print("   right shift b with 4 bits (b>>4)  -->  ",b>>4)

print("\n\n")

#Question 4:
input_string=input("Enter the string: ")
check_name=input_string.find("name")
if(check_name==-1):
    print("NO")
else:
    print("YES")
print("\n\n")

#Question 5:
side_1=int(input("Enter the side 1: "))
side_2=int(input("Enter the side 2: "))
side_3=int(input("Enter the side 3: "))

a=side_1 + side_2
b=side_2 + side_3
c=side_3 + side_1

x= (side_1 < b)
y= (side_2 < c)
z= (side_3 < a)

answer = str(x & y & z)
answer = answer.replace("True", "Yes")
answer = answer.replace("False", "No")

print(answer)
print("\n\n")

#Question 6:
a= int(input("enter the number a: "))
b= int(input("enter the number b: "))

c= (a^b)
d= bin(c)

count= 0
for i in d[2:]:
    if i == "1":
        count+= 1

print(count)
