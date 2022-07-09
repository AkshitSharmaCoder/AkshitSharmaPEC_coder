# INPUT ASSIGNMENT 6   AKSHIT SHARMA 21107018


# q1

def perfect(a):
    tempsum=0
    for i in range(1,a+1):
        if a%i == 0:
            tempsum = tempsum+i
            
    if a == tempsum/2:
        print(a, "is a perfect no")
    else:
        print("   not perfect")

x = int(input("enter no"))
perfect(x)
print("\n")


#q2
def checkpal(st):
# python mai fn defination mai typecasting mai type defining ki lod nhi hoti
    # tempsstr = st[::-1]
    # tempsstr = st.replace(" ","")
    tempsstr = st.replace(" ","")
    tempsstr = tempsstr[::-1]
    x = st.replace(" ","")
    if tempsstr == x:
        print(st, "is a palindrome")
    else:
        print("no")

t=input(" string enter ")
t = t.lower()
checkpal(t)
print("\n")


# q3


from math import factorial

n=5
for i in range(n):
    for j in range(n-1-i):
        print(" ", end="")
    for k in range (i+1):
        print(factorial(i) // (factorial(i-k)*factorial(k)) , end=" ") # nCr = n! / ((n-r)! * r!)
    print()
print("\n")

# q4


def palgram(str):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in str:
            return False
    return True

user_string=str(input("Enter a sentence: "))
if palgram(user_string)==False:
    print("entered sentence is not a palgram")
else:
    print("entered sentence is palgram")
print("\n")


#q5
str = input("string dalo")
def hyp():
    list=[]
    list = str.split("-")
    list.sort()
    empt = ""
    # empty string created
    for i in list:
        empt += i
        empt += "-"
    print(empt)
hyp()
print("\n")



# q6


def student_data(student_name , student_branch, student_id):
    print("student name: ",student_name)
    print("student branch: ",student_branch)
    print("student id: ",student_id)

student_data("Aayush","Civil",21102050)
print("\n")



# q7


class Student:
    pass 
class Marks:
    pass 
student1 = Student()
marks1 = Marks()
print(isinstance(student1, Student))
print(isinstance(marks1, Student))
print(isinstance(marks1, Marks)) 
print(isinstance(student1, Marks))
print("Check whether the said classes are subclasses of the built-in object class or not.")
print(issubclass(Student, object))
print(issubclass(Marks, object))
print()
print("\n")


#8

def findTriplets(arr, n):
  
    found = False
    for i in range(0, n-2):
      
        for j in range(i+1, n-1):
          
            for k in range(j+1, n):
              
                if (arr[i] + arr[j] + arr[k] == 0):
                    print(arr[i], arr[j], arr[k])
                    found = True
      
    if (found == False):
        print(" not exist ")
  
arr = [-25, -10, -7, -3, 2, 4, 8, 10]
n = len(arr)
findTriplets(arr, n)
print("\n")
print("\n")



# q9


class parantheses:
    def find(str):
        a= ['()', '{}', '[]'] 
        while any(i in str for i in a):
            for j in a:
                str = str.replace(j, '') 
        return not str 

s = input("Enter the sequence of parantheses : ")
if parantheses.find(s):
    print(s,"-","is balanced")
else:
    print(s,"-","is unbalanced")
print("\n")

