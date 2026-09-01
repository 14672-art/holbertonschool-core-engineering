#!/usr/bin/env python3
number = __import__('random').randint(-10, 10)
if number >0:
     print (f"{number} is Positive") 
elif number  ==0:
     print (f"{number} is Zero") 
else:  
     print (f"{number} is Negative")

