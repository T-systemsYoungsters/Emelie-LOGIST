Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> pi=3.14
>>> radius=input("Please enter your radius of the circle:")
Please enter your radius of the circle:3
>>> area=pi*radius**2
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    area=pi*radius**2
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
>>> area=pi * (radius* radius)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    area=pi * (radius* radius)
TypeError: can't multiply sequence by non-int of type 'str'
>>> radius=float(radius)
>>> area=pi * (radius*radius)
>>> print(area)
28.26
>>> 