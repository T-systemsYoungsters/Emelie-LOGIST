Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> height=("Please enter the height of the trapezoid:")
>>> height=input("Please enter the height of the trapezoid:")
Please enter the height of the trapezoid:5
>>> bottom_base=input("Please enter the length of the bottom base:")
Please enter the length of the bottom base:10
>>> top_base=("Please enter the length of the top base:")
>>> top_base=input("Please enter the length of the top base:")
Please enter the length of the top base:7
>>> height=float(height)
>>> bottom_base=float(bottom_base)
>>> top_base=float(top_base)
>>> area=1/2 * (bottom_base + top_base) * height
>>> print(area)
42.5
>>> 