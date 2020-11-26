Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #EXERCISE-1
>>> 
>>> #Add an item in to the list (using function)
>>> A=[12,43,33,96,87,78,29,70]
>>> A.append(25)
>>> print(A)
[12, 43, 33, 96, 87, 78, 29, 70, 25]
>>> 
>>> #Delete (using function)
>>> A.remove(96)
>>> print(A)
[12, 43, 33, 87, 78, 29, 70, 25]
>>> 
>>> #The largest number from the list
>>> A.sort()
>>> print("Largest element is ",A[-1])
Largest element is  87
>>> 
>>> #The Smallest number from the list
>>> print("Smallest element is",A[0])
Smallest element is 12
>>> 
>>> 
>>> #EXERCISE-2
>>> B=(5,10,15,20,30,40,50,60,70,80,90,99)
>>> C=reversed(B)
>>> print(tuple(C))
(99, 90, 80, 70, 60, 50, 40, 30, 20, 15, 10, 5)
>>> 
>>> 
>>> #EXERCISE-3
>>> A= ("RED","BLUE","YELLOW","GREEN","BLACK")
>>> B= list(A)
>>> print(B)
['RED', 'BLUE', 'YELLOW', 'GREEN', 'BLACK']
>>> 