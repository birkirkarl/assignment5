Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 3 > 2
True
>>> 3<2
False
>>> 3==2
False
>>> 3==3
True
>>> 3!=2
True
>>> a=2+5
>>> a
7
>>> a==7
True
>>> 
============ RESTART: /Users/Birkir/Downloads/Forritun 1/test2.py ============
Input a number: 2
Not zero
>>> 1
1
>>> 
============ RESTART: /Users/Birkir/Downloads/Forritun 1/test2.py ============
Input a number: 9
Not zero
>>> some_int=40
>>> another_int=20
>>> if some_int > another_int:
	print ("Some is bigger!")
	else:
		
SyntaxError: invalid syntax
>>> if some_int > another_int:
	print ("Some is bigger!")
	else:print("Another is bigger!")
	
SyntaxError: invalid syntax
>>> 
============ RESTART: /Users/Birkir/Downloads/Forritun 1/test3.py ============
0
>>> int ('4')==4
True
>>> user='Admin'
>>> logged_in=False
>>> if user=='Admin' and logged_in:
	print('Admin page')
	else:
		
SyntaxError: invalid syntax
>>> else: print('Bad credentials')
SyntaxError: invalid syntax
>>> user = 'Admin'
logged_in = False

if user == 'Admin' and logged_in:
    print('Admin page')
else:
    print('Bad credentials')


SyntaxError: multiple statements found while compiling a single statement
>>> 
============ RESTART: /Users/Birkir/Downloads/Forritun 1/test4.py ============
Bad credentials
>>> x=2
>>> y=(x<7) or (x>7)
>>> print(x,y)
2 True
>>> x=10
>>> y=12
>>> result=(x>y) and (y<10) or (x>7)
>>> print(result)
True
>>> a_int=3
>>> b_int=2
>>> b_int=a_int
>>> a_int=b_int
>>> print(a_int,b_int)
3 3
>>> percent_float=float(input("What is your percentage? "))
What is your percentage? 
========== RESTART: /Users/Birkir/Downloads/Forritun 1/22.08.19.py ==========
What is your percentage? 
