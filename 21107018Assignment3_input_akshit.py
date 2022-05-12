#Q1
num1 = int(input("Enter the number to be converted to binary: "))
print(bin(num1))

print("\n")


#Q2


n = input("Enter the expression ")
print(eval(n))

print("\n")


#Q3
import math as mt

n = int(input("Enter the number n: "))
r = int(input("Enter the number r: "))
a = int(input("Enter the angle a: "))
b = int(input("Enter the angle b: "))

x1 = int(input("Enter the number x1: "))
x2 = int(input("Enter the number x2: "))

y1 = int(input("Enter the number y1: "))
y2 = int(input("Enter the number y2: "))

print("(3+4)(5) = ", (3+4)*5)
print("n(n-1)/2 = ", (n*(n-1)/1))
print("4(pi)r^2 = ", 4*mt.pi*(r^2) )
print("sqrt(r(cosa)^2 + r(sinb)^2) = ", ((r*((mt.cos(a))**2)) + (r*((mt.sin(b))**2)))**(0.5))
if x2 == x1:
    print("Not defined")
else: 
    print("y2-y1/x2-x1 = ", (y2 - y1)/(x2 - x1))

print("\n")


#Q4

print("In the range(5)")
for i in range(5):
    print(i)

print("In the range(3, 10)")
for i in range(3, 10):
    print(i) 

print("In the range(4 ,13, 3)")
for i in range(4 ,13, 3):
    print(i) 

print("In the range(15, 5, -2)")
for i in range(15, 5, -2):
    print(i) 

print("In the range(5, 3)")
for i in range(5, 3):
    print(i) 

print("\n")


#Q5
h = int(input("Enter the number of hydrogen atoms: "))
c = int(input("Enter the number of carbon atoms: "))
o = int(input("Enter the number of oxygen atoms: "))

wt_h = h*1.00794
wt_c = c*12.0107
wt_o = o*15.99994

print(wt_h + wt_o + wt_c)
