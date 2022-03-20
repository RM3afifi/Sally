#! /usr/bin/python3.9
#! python3 sally.py

from datetime import date

def Add(x,y):
	return (x+y)

def Subtract(x,y):
	return (x-y)
	
def Multiply(x,y):
	return (x*y)
	
def Divide(x,y):
	return (x/y)
	
def Age(Year, Month, Day):
	Today = date.today()
	daysLeft = Today - date(Year, Month, Day)

	years = ((daysLeft.total_seconds())/(365.242*24*3600))
	yearsInt=int(years)

	months=(years-yearsInt)*12
	monthsInt=int(months)

	days=(months-monthsInt)*(365.242/12)
	daysInt=int(days)
	
	return (yearsInt, monthsInt, daysInt)
	
print('        Sally')
print('Made by Rokaya Muhammad')

print('What is your name?')
Name = input()
print("Hello, %s!" % Name)

print("What is the year you was born in, %s?" % Name)
Year = int(input("Year: "))

print("And, what is the month you was born in, %s?" % Name)
Month = int(input("Month: "))

print("And, what is the day you was born in, %s?" % Name)
Day = int(input("Day: "))

print("So, you Where born in",Day,"/",Month,"/",Year,"!")
print("So, your name is",Name,"and you are %s years old, %s months, and %s days!" % Age(Year, Month, Day))
print("Nice to know you %s!" % Name)
print('Oh yeah I was about to forget ;0. My name is Sally.')
print('I am a calculator bot')
print('Now you knew me and I knew you let us start')
print('First of all these are the operators that you can use: ÷,×,+,-,and / for ÷ and * for ×!')
running = True
while running:

	choice=input('Enter your operator: ')
	#check the choice
	if choice in('+','-','÷','×','/','*'):
		
		num1=float(input("Enter the first number: "))
		
		num2=float(input("Enter the second number: "))
	else:
		running = False	
	if choice=='+':
		print(num1,'+',num2,'=',Add(num1,num2))
		
	if choice=='-':
	        if num2== num1:
	            print(num1,'-',num2,'=',0)
	        else:    
	            print(num1,'-',num2,'=',Subtract(num1,num2))
	        
	        
	if choice=='×':
	        print(num1,'×',num2,'=',Multiply(num1,num2))
	        
	if choice=='÷':
	        
	        if num2== 0:
	        	print("Error, I cannot divide by zero, Try again!")
	        if num2 > num1:
	        	q = input("Are you sure?, it is going to be a fraction(y for yes n for no): ")
	        	if q in ('Y','y'):
	        		
	        		print(num1,'÷',num2,'=',Divide(num1,num2))	
	        	else:
	        		print(num1,'÷',num2,'=',Divide(num1,num2))
	        	
	        	
	if choice=='*':
	        print(num1,'×',num2,'=',Multiply(num1,num2))
	        
	if choice=='/':
	        
	        if num2== 0:
	        	print("Error, I cannot divide by zero, Try again!")
	        if num2 > num1:
	        	q = input("Are you sure?, it is going to be a fraction(y for yes n for no): ")
	        	if q in ('Y','y'):
	        		
	        		print(num1,'÷',num2,'=',Divide(num1,num2))	
	        	else:
	        		print(num1,'÷',num2,'=',Divide(num1,num2))
	        			 


else:
	print('there is no that operator, there is ÷,×,+,-,and / for ÷ and * for ×!')
	print('Good Bye!')
	print('See you soon!')
	print("Don\'t forget me I wiil miss you %s!" % Name)
	print('Bye!')
