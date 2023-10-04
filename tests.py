#Create a pytest to check the following:
#1. if the grade is passed (greater than or equal to 50) 
#2. if the conversion of the temperature from celcius to fahrenheit is correct
#3. if the area of the square is correct
#f = c x (9/5) +32

import math

def test_grade():
    grade = 45
    assert grade>=50

def test_conversion():
    c = 20
    f = c*1.8+32
    assert f == 68

def test_area():
    side = 3
    assert side**2 == 9

