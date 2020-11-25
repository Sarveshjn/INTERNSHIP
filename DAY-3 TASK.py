Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #DAY3 TASK-3
>>> 
>>> #EXERCISE-1
>>> dic_1={"KARNATAKA":"CHENNAI","DELHI":"UTTARPRADESH"}
>>> dic_2={"KARWAR":"TAMILNADU","CHANDANICHOK":"RAJGAD"}
>>> dic_1.update(dic_2)
>>> print(dic_1)
{'KARNATAKA': 'CHENNAI', 'DELHI': 'UTTARPRADESH', 'KARWAR': 'TAMILNADU', 'CHANDANICHOK': 'RAJGAD'}
>>> 
>>> 
>>> #EXERCISE-2
>>> dic ={"RAHUL":"SARVESH","KARAN":"VIGNESH"}
>>> del dic["KARAN"]
>>> print(dic)
{'RAHUL': 'SARVESH'}
>>> 
>>> 
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> #EXERCISE-3
>>> keys= ["NAME","AGE","PLACE"]
>>> values= ["SARVESH", 19,"KARWAR"]
>>> z = dict(zip(keys, values))
>>> print(z)
{'NAME': 'SARVESH', 'AGE': 19, 'PLACE': 'KARWAR'}
>>> 
>>> 
>>> #EXERCISE-4
>>> set={"CHENNAI","BANGALORE","MUMBAI","DELHI","KARWAR","GOA","HYDRABAD"}
>>> print(len(set))
7
>>> 
>>> 
>>>  #EXERCISE-5
>>> s1={10,20,30,40,60,80}
>>> s2={5,15,25,35,45,55}
>>> x=s1-s2
>>> print(x)
{40, 10, 80, 20, 60, 30}
>>> 