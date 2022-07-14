#Question 1
from tkinter import *

def findGst() :

	org_cost= int(org_priceField.get())
	N_price = int(net_priceField.get())
	gst_rate = ((N_price - org_cost) * 100) / org_cost;

	gst_rateField.insert(10, str(gst_rate) + " % ")

def clearAll():

	org_priceField.delete(0, END)
	net_priceField.delete(0, END)
	gst_rateField.delete(0, END)

if __name__ == "__main__" :
	gui = Tk()
	gui.configure(background = "light green")
	gui.title("GST Rate Finder")
	gui.geometry("300x300")
	org_price = Label(gui, text = "Original Price",
					bg = "blue")
	net_price = Label(gui, text = "Net Price",
					bg = "blue")
	find = Button(gui, text = "Find", fg = "Black",
				bg = "Red",
				command = findGst)
	gst_rate = Label(gui, text = "Gst Rate", bg = "blue")
	clear = Button(gui, text = "Clear", fg = "Black",
				bg = "Red",
				command = clearAll)

	org_price.grid(row = 1, column = 1,padx = 10,pady = 10)

	net_price.grid(row = 2, column = 1, padx = 10, pady = 10)

	find.grid(row = 3, column = 2,padx = 10,pady = 10)

	gst_rate.grid(row = 4, column = 1,padx = 10, pady = 10)

	clear.grid(row = 5, column = 2, padx = 10, pady = 10)
	org_priceField = Entry(gui)

	net_priceField = Entry(gui)

	gst_rateField = Entry(gui)

	org_priceField.grid(row = 1, column = 2 ,padx = 10,pady = 10)

	net_priceField.grid(row = 2, column = 2, padx = 10,pady = 10)

	gst_rateField.grid(row = 4, column = 2, padx = 10,pady = 10)

	gui.mainloop()



#Question 2
from tkinter import *
import calendar

def showCal() :
	new_gui = Tk()
	new_gui.config(background = "white")
	new_gui.title("CALENDAR")
	new_gui.geometry("550x600")
	fetch_year = int(year_field.get())
	cal_content = calendar.calendar(fetch_year)

	cal_year = Label(new_gui, text = cal_content, font = "Consolas 10 bold")

	cal_year.grid(row = 5, column = 1, padx = 20)

	new_gui.mainloop()


if __name__ == "__main__" :

	gui = Tk()

	gui.config(background = "white")

	gui.title("CALENDAR")

	gui.geometry("250x140")

	cal = Label(gui, text = "CALENDAR", bg = "dark gray",
							font = ("times", 28, 'bold'))

	year = Label(gui, text = "Enter Year", bg = "light green")

	year_field = Entry(gui)

	Show = Button(gui, text = "Show Calendar", fg = "Black",
							bg = "Red", command = showCal)

	Exit = Button(gui, text = "Exit", fg = "Black", bg = "Red", command = exit)

	cal.grid(row = 1, column = 1)

	year.grid(row = 2, column = 1)

	year_field.grid(row = 3, column = 1)

	Show.grid(row = 4, column = 1)

	Exit.grid(row = 6, column = 1)

	gui.mainloop()


	


#Question 3
from tkinter import *

expression = ""
def press(num):
	global expression
	expression = expression + str(num)
	equation.set(expression)

def equalpress():

	try:

		global expression
		total = str(eval(expression))

		equation.set(total)
		expression = ""
	except:

		equation.set(" error ")
		expression = ""
def clear():
	global expression
	expression = ""
	equation.set("")

if __name__ == "__main__":
	gui = Tk()
	gui.configure(background="light green")
	gui.title("Simple Calculator")
	gui.geometry("270x150")
	equation = StringVar()
	expression_field = Entry(gui, textvariable=equation)
	expression_field.grid(columnspan=4, ipadx=70)
	button1 = Button(gui, text=' 1 ', fg='black', bg='red',
					command=lambda: press(1), height=1, width=7)
	button1.grid(row=2, column=0)

	button2 = Button(gui, text=' 2 ', fg='black', bg='red',
					command=lambda: press(2), height=1, width=7)
	button2.grid(row=2, column=1)

	button3 = Button(gui, text=' 3 ', fg='black', bg='red',
					command=lambda: press(3), height=1, width=7)
	button3.grid(row=2, column=2)

	button4 = Button(gui, text=' 4 ', fg='black', bg='red',
					command=lambda: press(4), height=1, width=7)
	button4.grid(row=3, column=0)

	button5 = Button(gui, text=' 5 ', fg='black', bg='red',
					command=lambda: press(5), height=1, width=7)
	button5.grid(row=3, column=1)

	button6 = Button(gui, text=' 6 ', fg='black', bg='red',
					command=lambda: press(6), height=1, width=7)
	button6.grid(row=3, column=2)

	button7 = Button(gui, text=' 7 ', fg='black', bg='red',
					command=lambda: press(7), height=1, width=7)
	button7.grid(row=4, column=0)

	button8 = Button(gui, text=' 8 ', fg='black', bg='red',
					command=lambda: press(8), height=1, width=7)
	button8.grid(row=4, column=1)

	button9 = Button(gui, text=' 9 ', fg='black', bg='red',
					command=lambda: press(9), height=1, width=7)
	button9.grid(row=4, column=2)

	button0 = Button(gui, text=' 0 ', fg='black', bg='red',
					command=lambda: press(0), height=1, width=7)
	button0.grid(row=5, column=0)

	plus = Button(gui, text=' + ', fg='black', bg='red',
				command=lambda: press("+"), height=1, width=7)
	plus.grid(row=2, column=3)

	minus = Button(gui, text=' - ', fg='black', bg='red',
				command=lambda: press("-"), height=1, width=7)
	minus.grid(row=3, column=3)

	multiply = Button(gui, text=' * ', fg='black', bg='red',
					command=lambda: press("*"), height=1, width=7)
	multiply.grid(row=4, column=3)

	divide = Button(gui, text=' / ', fg='black', bg='red',
					command=lambda: press("/"), height=1, width=7)
	divide.grid(row=5, column=3)

	equal = Button(gui, text=' = ', fg='black', bg='red',
				command=equalpress, height=1, width=7)
	equal.grid(row=5, column=2)

	clear = Button(gui, text='Clear', fg='black', bg='red',
				command=clear, height=1, width=7)
	clear.grid(row=5, column='1')

	Decimal= Button(gui, text='.', fg='black', bg='red',
					command=lambda: press('.'), height=1, width=7)
	Decimal.grid(row=6, column=0)
	# start the GUI
	gui.mainloop()




# question 4
print("Q4")

# MergeSort in Python


def mergeSort(array):
    if len(array) > 1:

        #  r is the point where the array is divided into two subarrays
        r = len(array)//2
        L = array[:r]
        M = array[r:]

        # Sort the two halves
        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1


# Print the array
def printList(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()


# Driver program

if __name__ == '__main__':
    array = eval(input("Enter a list of comma separated marks in [] brackets:"))
    mergeSort(array)

    print("Sorted array is: ")
    printList(array)



# question 5
print("Q5")
#5a

def partition(l, r, nums):
    # Last element will be the pivot and the first element the pointer
    pivot, ptr = nums[r], l
    for i in range(l, r):
        if nums[i] <= pivot:
            # Swapping values smaller than the pivot to the front
            nums[i], nums[ptr] = nums[ptr], nums[i]
            ptr += 1
    # Finally swapping the last element with the pointer indexed number
    nums[ptr], nums[r] = nums[r], nums[ptr]
    return ptr
 
# With quicksort() function, we will be utilizing the above code to obtain the pointer
# at which the left values are all smaller than the number at pointer index and vice versa
# for the right values.
 
 
def quicksort(l, r, nums):
    if len(nums) == 1:  # Terminating Condition for recursion. VERY IMPORTANT!
        return nums
    if l < r:
        pi = partition(l, r, nums)
        quicksort(l, pi-1, nums)  # Recursively sorting the left values
        quicksort(pi+1, r, nums)  # Recursively sorting the right values
    return nums

n = eval(input("Enter a list in [] brackets:"))

print(quicksort(0,len(n)-1,n))

#5b
def binary_search(list1, x):  
    low = 0  
    high = len(list1) - 1  
    mid = 0  
  
    while low <= high:  
        # for get integer result   
        mid = (high + low) // 2  
  
        # Check if n is present at mid   
        if list1[mid] < x:  
            low = mid + 1  
  
        # If n is greater, compare to the right of mid   
        elif list1[mid] > x:  
            high = mid - 1  
  
        # If n is smaller, compared to the left of mid  
        else:  
            return mid  
  
            # element was not present in the list, return -1  
    return -1  
  
  
# Initial list1    
x = int(input("Enter the element you want to search :"))
  
# Function call   
result = binary_search(n, x)  
  
if result != -1:  
    print("Element is present at index", n.index(x))  
else:  
    print("Element is not present in list1")  

#5c
count = 0
for i in n:
    if i == x:
        count += 1
print(f'Number of occurences of element {x} is: {count}')




# question 6
print("Q6")

def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list

list1 = eval(input("Enter a list of numbers containing duplicates inside []:"))
list2 = Remove(list1)
print(list2)

def bubbleSort(array):
    
  # loop to access each array element
  for i in range(len(array)):

    # loop to compare array elements
    for j in range(0, len(array) - i - 1):

      # compare two adjacent elements
      # change > to < to sort in descending order
      if array[j] > array[j + 1]:

        # swapping elements if elements
        # are not in the intended order
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp


bubbleSort(list2)

print('Sorted List in Ascending Order by Bubble sort:')
print(list2)

def selectionSort(array, size):
   
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
            if array[i] < array[min_idx]:
                min_idx = i
         
        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])


list3 = Remove(list1)
size = len(list3)
selectionSort(list3, size)
print('Sorted Array in Ascending Order by Selection sort:')
print(list3)

