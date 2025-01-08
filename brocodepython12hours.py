# print("Hello World")
# print("I like pizza")
# print("it's really good")
# # this is my first python program
# # string
# first_name="Bro"
# food="pizza"
# email="jsharipov559@gmial.com"
# print(first_name)
# print(f"Hello {first_name}")
# print(f"You like {food}")
# print(f"You email is {email}")
# #integer
# age=25
# quantity=3
# num_students=30
# print(f"Yor are {age} years old")
# print(f"You are buying {quantity} items")
# print(f"Your class has {num_students} students")
# #float
# price=10.99
# gpa=4.4
# distance=5.5
# print(f"The price is ${price}")
# print(f"Your gpa is {gpa}")
# print(f"You ran {distance}km")
# #Boolean
# is_student=True
# for_sale=False
# is_online=True
# print(f"Are you a student? {is_student}")
# if is_student:
#     print(f"You are a student")
# else:
#     print("You are not a student")
# if for_sale:
#     print("That item is for sale")
# else:
#     print("That item is not available")
# if is_online:
#     print("You are online")
# else:
#     print("You are offline")
# user_name="Bro Code"
# year=2024
# pi=3.14
# is_admin=True
# #typecasting
# #Explicit
# name="Bro"
# age=21
# gpa=4.9
# student=True
# print(type(name))
# print(type(age))
# print(type(gpa))
# print(type(student))
# age=float(age)
# print(age)
# gpa=int(gpa)
# print(gpa)
# student=str(student)
# print(type(student))
# age=bool(age)
# print(age)
# age=0
# age=bool(age)
# print(age)
# name=bool(name)
# print(name)
# name=""
# name=bool(name)
# print(name)
# #implicit
# x=2
# y=2.0
# x=x/y
# print(x)
# name=input("Enter your name: ")
# age=int(input("Enter your age: "))
# age=age+1
# print(f"Hello {name}")
# print(f"You are {age} years old")
#mad libs
# adjective1=input("Enter an adjective: ")
# noun=input("Enter a noun: ")
# adjective2=input("Enter an adjective: ")
# verb=input("Enter a verb: ")
# adjective3=input("Enter an adjective: ")
# print(f"Today I went to a {adjective1} zoo")
# print(f"In an exhibit, I saw {noun}")
# print(f"{noun} was {adjective2} and {verb}ing")
# print(f"I was {adjective3}")
#area calc
# length=int(input("Enter the length of a rectangle: "))
# width=int(input("Enter the width of a rectangle: "))
# area=length*width
# print(f"The area is: {area}cm^2")
#shopping cart
# item=input("What item would you like to buy?: ")
# price=float(input("What is the price?: "))
# quantity=int(input("How many would you like?: "))
# total=price*quantity
# print(f"You have bought {quantity}*{item}/s")
# print(f"Your total is: ${round(total)}")
# friends=0
# friends=friends+1
# friends+=1
# friends=friends-2
# friends-=2
# friends=friends*3
# friends*=3
# friends=friends/2
# friends/=2
# friends=friends**2
# friends**=2
# remainder=friends%3
# x=3.14
# y=-4
# z=5
# result=round(x)
# result=abs(y)
# result=pow(4,3)
# result=max(x,y,z)
# result=min(x,y,z)
# print(result)
# import math as m
# print(m.pi)
# x=9.1
# print(m.e)
# result=m.sqrt(x)
# result=m.ceil(x)
# result=m.floor(x)
# print(result)
# import math
# radius=float(input("Enter the radius of a circle: "))
# circumference=2*(math.pi)*radius
# area=(math.pi)*(pow(radius,2))
# print(f"The circumference is: {round(circumference,2)}cm")
# print(f"The area is: {round(area,2)} cm^2")
# import math
# a=int(input('Enter side A: '))
# b=int(input('Enter side B: '))
# c=math.sqrt((a**2)+(b**2))
# print(f"Side C: {c}")
# age=int(input("Enter your age: "))
# if age>=100:
#     print("You are too old to sing up")
# elif age<0:
#     print("You haven't been born yet!")
# elif age>=18:
#     print("You are now signed up!")
# else:
#     print("You must be 18+ to sign up")
# response=input("Would you like food? (Y/N): ")
# if response=='Y':
#     print("Have some food!")
# else:
#     print("No food for you!")
# name=input("Enter your name: ")
# if name=="":
#     print("You did not type in your name!")
# else:
#     print(f"Hello {name}")
# for_sale=True
# if for_sale:
#     print("This item is for sale")
# else:
#     print("This item is not for sale")
# Python calculator
# operator=input("Enter an operator (+ - * /): ")
# num1=float(input("Enter the 1st number: "))
# num2=float(input("Enter the 2nd number: "))
# if operator=='+':
#     print(num1+num2)
# elif operator=='-':
#     print(num1-num2)
# elif operator=='*':
#     print(num1*num2)
# elif operator=='/':
#     print(num1/num2)
# else:
#     print(f"{operator} is not valid")
#python weight converter
# weight=float(input("Enter your weight: "))
# unit=input("Kilograms or Pounds? (K or L): ")
# if unit=='K':
#     weight*=2.205
#     unit='Lbs'
# elif unit=='L':
#     weight/=2.205
#     unit='Kgs'
# else:
#     print(f"{unit} was not valid")
# print(f"Your weight is: {round(weight,2)} {unit}")
# unit=input("Is this tempreture in Celsius or Farhenheit (C/F): ")
# temp=float(input("Enter the temperature: "))
# if unit=='C':
#     temp=((temp*9/5)+32)
#     unit='F'
# elif unit=='F':
#     temp=((temp-32)*5/9)
#     unit='C'
# else:
#     print(f"{unit} was not valid")
# print(f"Tempreture is: {temp}{unit}")
# temp=0
# if temp>0 and temp<30:
#     print("The tempereture is good!")
# else:
#     print("The temperature is bad")
# sunny=False
# if not sunny:
#     print("it is cloudly outside")
# else:
#     print("it is sunny outside")
# print(5 if 6>7 else 9)
# num=6
# print("Positive" if num>0 else "Negative")
# num=99
# result="Even" if num%2==0 else "ODD"
# print(result)
# a=6
# b=7
# age=25
# temperature=30
# user_role='guest'
# max_num=a if a>b else b
# min_num=a if a<b else b
# print(min_num)
# status="Adult" if age>=18 else "Child"
# print(status)
# weather="HOT" if temperature > 20 else "COLD"
# print(weather)
# access_level="Full Access" if user_role=='Admin' else "Limited Access"
# print(access_level)
# name=input("Enter your full name: ")
# result=len(name)
# print(result)
# result=name.rfind("o")
# result=name.capitalize()
# result=name.isalpha()
# print(result)
# phone_number=input("Enter your phone number: ")
# result=phone_number.count('-')
# result=phone_number.replace('-'," ")
# print(result)
# username=input("Enter a username: ")
# if len(username)<=12 and username.find(' ')==-1 and not username.isdigit():
#     print("This username accepted!")
# else:
#     print("This username is not valid")
# user='*'
# print(user.isalpha())
# credit_number="1234-5678-3456"
# print(credit_number[-5])
# print(credit_number[::3])
# print(credit_number[-4:])
# print(credit_number[::-1])
# email=input("Enter your email: ")
# username=email[:email.find("@")]
# domain=email[(email.find("@")+1):]
# print(f"Your username is {username} \nand domain is {domain}")
# email="sharipov"
# print(email.find('k'))
# format specifiers = {:flags} format a value based on what flags are inserted


# .(number)f = round to that many decimal places

# :(number) = allocate that many spaces

# :0(number) = allocate and zero pad that many spaces

# :< = left justify

# :> = right justify

# :^ = center align

# :+ = use a plus sign to indicate positive value

# := = place sign to leftmost position

# :  = insert a space before positive numbers

# :, = comma separator

# # :% = percentage format
# price1 = 30004.14159
# price2 = -98744.65
# price3 = 1287654.35
# print(f"price1 is: ${price1:+,.2f}")
# print(f"price2 is: ${price2:+,.2f}")
# print(f"price3 is: ${price3:+,.2f}")
# name=input("Enter your name: ")
# while name=="":
#     print("You did not enter your name")
#     name=input("Enter your name: ")
# print(f"Hello {name}")
# age=int(input("Enter your age: "))
# while age<0:
#     print("Age can't be negative")
#     age=int(input("Enter your age: "))
# print(f"You are {age} years old")
# food=input("Enter a food you like (q to quit): ")
# while not food=='q':
#     print(f"You like {food}")
#     food=input("Enter another food you like (q to quit): ")
# print("Bye")
# num=int(input("Enter a # between 1- 10: "))
# while num<1 or num>10:
#     print(f"{num} is not valid")
#     num=int(input("Enter a # between 1- 10: "))
# print(f"Your number is {num}")
# principle=0
# rate=0
# time=0
# while True:
#     principle=float(input("Enter the principle amount: "))
#     if principle<0:
#         print("Principle can't be less than zero")
#     else:
#         break
# while True:
#     rate=float(input("Enter the interest rate: "))
#     if rate<0:
#         print("Interest rate can't be less than zero")
#     else:
#         break
# while True:
#     time=float(input("Enter the time in years: "))
#     if time<0:
#         print("Time can't be less than zero")
#     else:
#         break
# total=principle*pow((1+(rate/100)),time)
# print(f"Balance after {time} year/s: ${total:.2f}")
# for x in range(1,11):
#     print(x)
# for x in reversed(range(1,11)):
#     print(x)
# print("Happy New Year!")
# for x in range(1,11,2):
#     print(x)
# credit_card="1234-5678-9012"
# for x in credit_card:
#     print(x)
# for x in range(1,21):
#     if x==13:
#         continue
#     else:
#         print(x)
# for x in range(1,10):
#     print(x)
# print(range(3))
# for x in range(3):
#     for y in range(10):
#         print(y,end='')
#     print()
# rows=int(input("Enter # the number of rows: "))
# columns=int(input("Enter # the number of columns: "))
# symbol=input("Enter a symbol to use: ")
# for x in range(rows):
#     for y in range(columns):
#         print(symbol,end='')
#     print()
# import time
# time.sleep(3)
# print("Time's up!")
# my_time=int(input("Enter the time in second: "))
# for x in range(my_time,0,-1):
#     print(x)
#     time.sleep(1)
# print("Time's up!")
# my_time=int(input("Enter the time in seconds: "))
# for x in range(my_time,0,-1):
#     seconds=x%60
#     minuts=int(x/60)%60
#     hours=int(x/3600)
#     print(f"{hours:02}:{minuts:02}:{seconds:02}")
#     time.sleep(1)
# print("Time's up!")
# N,P=map(int,input().split())
# print(N)
# print(P)
# x=input()
# N,P=x.split()
# N=int(N)
# P=int(P)
# print(N*P)
# frui=("apple","orange","banana","coconut","pineapple","apple")
# print(fruits[::-1])
# for fruit in fruits:
#     print(fruit)
# print(dir(fruits))
# print(len(fruits))
# fruits[0]="grapes"
# print(fruits)
# fruits.append("pear")
# print(fruits)
# fruits.remove("grapes")
# print(fruits)
# fruits.insert(0,"peach")
# fruits.clear()
# print(fruits)
# print(fruits.count("orange"))
# frui.add("grapes")
# frui.pop()
# print(frui)
# frui.clear()
# print(frui)
# print(dir(frui))
# print(help(frui))
# print("apple" in frui)
# print(frui.index("apple"))
# print(frui.count("apple"))
# x = int(input())  # Read the input
# number_of_divisor = 0

# if x == 0:
#     print(-1)  # Infinite divisors for 0
# else:
#     x = abs(x)  # Work with absolute value of x to handle negative numbers
#     for i in range(1, int(x**0.5) + 1):  # Loop until the square root of x
#         if x % i == 0:  # If i divides x evenly
#             number_of_divisor += 1  # Count the divisor
#             if i != x // i:  # Avoid counting the square root twice
#                 number_of_divisor += 1  # Count the corresponding pair
#     if number_of_divisor%2==0:
#       print(number_of_divisor)
#     else:
#       print(number_of_divisor+1)
# foods=[]
# prices=[]
# total=[]
# while True:
#     food=input("Enter a food to buy (q to quit): ")
#     if food.lower()=='q':
#         break
#     else:
#         price=float(input(f"Enter the price of a {food}: $ "))
#         foods.append(food)
#         prices.append(price)
# total=sum(prices)
# print("----Your Cart----")
# for food in foods:
#     print(food,end=" ")
# print(f"\nYour total: $ {total}")
# fruits=["apple","orange","banana","coconut"]
# vegetables=["celery","carrots","potatoes"]
# meats=["chicken","fish","turkey"]
# groceries=[fruits,vegetables,meats]
# print(groceries[1][2])
# groceries=[
#     ["apple","orange","banana","coconut"],
#     ["celery","carrots","potatoes"],
#     ["chicken","fish","turkey"]
# ]
# for collection in groceries:
#     for element in collection:
#         print(element)
#     print("****")
# keypad=(
#     (1,2,3),
#     (4,5,6),
#     (7,8,9),
#     ('*',0,"#")
# )
# for collection in keypad:
#     for element in collection:
#         print(element,end=" ")
#     print()
#Pyhton quiz game
# questions=(
#     "How many elements are in the periodic table?: ",
#     "Which animal lays the largest eggs?: ",
#     "What is the most abundant gas in Earth's atmosphere?: ",
#     "How many bones are in the human body?: ",
#     "Which planet in the solar system is the hottest?: "
# )
# options=(
#     ("A. 116","B. 117","C. 118","D. 119"),
#     ("A. Whale","B. Crocodile","C. Elephant","D. Ostrich"),
#     ("A. Nitrogen","B. Oxygen","C. Carbon-Dioxide","D. Hydrogen"),
#     ("A. 206","B. 207","C. 208","D. 209"),
#     ("A. Mercury","B. Venus","C. Earth","D. Mars")
# )
# answers=("C","D","A","A","B")
# guesses=[]
# score=0
# questions_num=0
# for question in questions:
#     print("------------------------")
#     print(question)
#     for option in options[questions_num]:
#         print(option)
#     guess=input("Enter (A, B, C, D): ").upper()
#     guesses.append(guess)
#     if guess==answers[questions_num]:
#         score+=1
#         print("CORRECT!")
#     else:
#         print("INCORRECT!")
#         print(f"{answers[questions_num]} is the correct answer")
#     questions_num+=1
# print("------------------------")
# print("         RESULT         ")
# print("------------------------")
# print("answers: ",end="")
# for answer in answers:
#     print(answer,end=" ")
# print("\nguesses: ",end="")
# for guess in guesses:
#     print(guess,end=" ")
# score=int((score/len(questions))*100)
# print(f"\nYour score is {score}%")
# capitals={"USA":"Washington",
#           "India":"New Delhi",
#           "China":"Beiging",
#           "Russia":"Moscow"
#           }
# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("USA"))
# print(capitals.get("Japan"))
# if capitals.get("Russia"):
#     print("That capital exists")
# else:
#     print("That capital doesn't exist")
# capitals.update({"Germany":"Berlin"})
# capitals.update({"USA":"UZB"})
# removed_element=capitals.pop("USA","Not Found")
# print(removed_element)
# removed_element=capitals.popitem()
# print(removed_element)
# capitals.clear()
# print(list(capitals.keys()))
# for key in capitals.keys():
#     print(key)
# print(capitals)
# print(list(capitals.values()))
# for value in capitals.values():
#     print(value)
# print(list(capitals.items()))
# for collection in capitals.items():
#     for element in collection:
#         print(element,end=" ")
#     print()
# for key,value in capitals.items():
#     print(f"{key}:{value}")
# for key,value in capitals:
#     print(f"{key}:{value}")
# menu={
#     "pizza":3.00,
#     "nachos":4.50,
#     "popcorn":6.00,
#     "fries":2.50,
#     "chips":1.00,
#     "pretzel":3.50,
#     "soda":3.00,
#     "lemonade":4.25
# }
# cart=[]
# total=0
# print("--------Menu--------")
# for key,value in menu.items():
#     print(f"{key}:{value}")
# print("--------------------")
# while True:
#     food=input("Select an item (q to quit): ").lower()
#     if food=='q':
#         break
#     elif menu.get(food):
#         cart.append(food)
#         total+=menu.get(food)
# print("-------Your Order------")
# for item in cart:
#     print(item,end=" ")
# print()
# print(f"Your total: {total}")
# import random
# number=random.randint(1,6)
# number=random.random()
# options=("rock","paper","scissors")
# number=random.choice(options)
# cards=("2","3","4","5","6","7","8","9","10","J","Q","K","A")
# number=random.choice(cards)
# low=1
# high=100
# guesses=0
# number=random.randint(low,high)
# while True:
#     guess=int(input(f"Enter a number between {low}-{high} : "))
#     guesses+=1
#     if guess>number:
#         print("Ener smaller number!")
#     elif guess<number:
#         print("Enter bigger number!")
#     else:
#         print("Correct")
#         break
# print(f"This round took you {guesses} guesses")
# import random
# low_num=1
# high_num=100
# guesses=0
# answer=random.randint(low_num,high_num)
# print(f"Select a number between {low_num} and {high_num}")
# while True:
#     guess=input("Enter your guess: ")
#     guesses+=1
#     if guess.isdigit():
#         guess=int(guess)
#         if guess<low_num or guess>high_num:
#             print("That number is out of range!")
#             print("Please select a number between {low_num} and {high_num}")
#         elif guess>answer:
#             print("Too high!")
#             print("Try again!")
#         elif guess<answer:
#             print("Too low!")
#             print("Try again!")
#         else:
#             print(f"CORRECT!,The answer was {answer}")
#             print(f"Number of guesses: {guesses}")
#             break
#     else:
#         print("Invalid guess!")
#         print("Please select a number between {low_num} and {high_num}")
# import random
# options=("rock","paper","scissors")
# while True:
#     player=input("Enter a choice (rock,paper,scissors): ")
#     computer=random.choice(options)
#     while player not in options:
#         player=input("Enter a choice (rock,paper,scissors): ")
#     print(f"Computer: {computer}\nPlayer: {player}")
#     if player=="rock" and computer=="scissors":
#         print("You won!")
#     elif player=="paper" and computer=="rock":
#         print("You won!")
#     elif player=="scissors" and computer=="paper":
#         print("You won!")
#     else:
#         print("You lose!")
#     if not input("Play again? (y/n): ").lower()=='y':
#         break
# print("Thanks for playing!")
#dice art
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")
# ● ┌ ─ │ │ └ ┘
# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"
# import random
# dice_art={
#     1:("┌─────────┐",
#        "│         │",
#        "│    ●    │",
#        "│         │",
#        "└─────────┘"),
#     2:("┌─────────┐",
#        "│  ●      │",
#        "│         │",
#        "│      ●  │",
#        "└─────────┘"),
#     3:("┌─────────┐",
#        "│  ●      │",
#        "│    ●    │",
#        "│      ●  │",
#        "└─────────┘"),
#     4:("┌─────────┐",
#        "│  ●   ●  │",
#        "│         │",
#        "│  ●   ●  │",
#        "└─────────┘"),
#     5:("┌─────────┐",
#        "│  ●   ●  │",
#        "│    ●    │",
#        "│  ●   ●  │",
#        "└─────────┘"),
#     6:("┌─────────┐",
#        "│  ●   ●  │",
#        "│  ●   ●  │",
#        "│  ●   ●  │",
#        "└─────────┘")}
# num_of_die=int(input("How many dice?: "))
# dice=[]
# for num in range(num_of_die):
#     dice.append(random.randint(1,6))
# # for num in dice:
# #     for element in dice_art.get(num):
# #         print(element)
# for row in range(5):
#     for element in dice:
#         print(dice_art.get(element)[row],end="  ")
#     print()
# print(f"Total: {sum(dice)}")
# import random
# import string 
# chars=" "+ string.punctuation+string.digits+string.ascii_letters
# chars=list(chars)
# keys=chars.copy()
# random.shuffle(keys)
# print(f"chars: {chars}")
# print(f"keys: {keys}")

# #Encypt
# plain_text=input("Enter a message to encryt: ")
# cipher_text=""
# for letter in plain_text:
#     index=chars.index(letter)
#     cipher_text+=keys[index]
    
# print(f"original message: {plain_text}\nenrcyted message: {cipher_text}")
# cipher_text=input("Enter a message to encryt: ")
# plain_text=""
# for letter in cipher_text:
#     index=keys.index(letter)
#     plain_text+=chars[index]
# print(f"original message: {plain_text}\nenrcyted message: {cipher_text}")
# def happy_birthday(name,age):
#     print(f"Happy birthday to {name}\nYou are {age} old")
    
# happy_birthday("Jonibek")
# happy_birthday("Jonibek",18)
# def display_invoice(username,amount,due_date):
#     print(f"Hello {username}")
#     print(f"Your bill of ${amount:.2f} is due to: {due_date}")
# display_invoice("Jonibek",100.1234,"10/12'2025")
# def add(a,b):
#     return a+b;
# z=add(1,2)
# add(1,2)
# print(z)
# def create_name(first,last):
#     first=first.capitalize()
#     last=last.capitalize()
#     return first+" "+last
# print(f"Full name: {create_name("jonibek","sharipov")}")
# def net_price(list_price,discount=0,tax=0.05):
#     return list_price*(1-discount)*(1+tax)
# print(net_price(500))
# print(net_price(500,0.1,0))
# import time
# def count(end,start=0):
#    for x in range(start,end+1):
#         print(x)
#         time.sleep(1)
#    print("DONE!")
# count(10)
# def hello(greeting,title,first,last):
#     print(f"{greeting} {title}.{first} {last}")
# hello("Hi",last="Sharipov",title="Mr",first="Jonibek",)
# print("Hello","World")
# print("Hello","World",sep="10")
# def get_phone(country,area,first,last):
#     return f"{country}-{area}-{first}-{last}"
# phone_num=get_phone(country=998,area=65,first=123,last=789)
# print(phone_num)
# def add(*nums):
#     total=0
#     for num in nums:
#         total+=num
#     return total;
# print(add(1,2,3,4,5))
# def display_name(*args):
#     for arg in args:
#         print(arg,end=" ")
# display_name("Jonibe","Sharipov","Jamshidovich")
# def print_address(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key}:{value}");
# print_address(street="Arabkhoona",
#               apt=370,
#               city="Bukhara",
#               state="Uzbekistan",
#               zip=200100)
# def shipping_label(*args,**kwargs):
#     for arg in args:
#         print(arg, end=" ")
#     print()
#     for value in kwargs.values():
#         print(value, end=" ")
#     print(f)
# shipping_label("Dr",
#                "Jonibek",
#                "Sharipov",
#                "JShJ",
#                street="1234",
#                apt=100,
#                city="Bukhara",
#                state="Uzbekistan",
#                zip=200100)
# numbers=[1,2,3,4,5]
# for number in reversed(numbers):
#     print(number, end=" ")
# fruits={"apple",
        # "orange",
        # "banana",
        # "conconut"}
# for fruit in fruits:
#     print(fruit)
# print(fruits)
# name="Bro Code"
# for character in name:
#     print(character, end=" ")
# tuples=(1,2,3,4,5)
# for tuple in reversed(tuples):
#     print(tuple)
# my_dictionary={"A":1,
#                "B":2,
#                "C":3,
#                }
# for key,value in my_dictionary.items():
#     print(f"{key}:{value}")
# word="APPLE"
# letter=input("Guess a letter in the secret word: ")
# if letter.upper() not in word:
#     print(f"{letter} was not found")
# else:
#     print(f"There is a {letter}")
# students={"spongebob","Patrick","Sandy"}
# student=input("Enter the name of a student: ")
# if student not in  students:
#     print(f"No, {student} is not here")
# else:
#     print(f"Yes, {student} is here!")
# grades={"Sandy":"A",
#         "Squidward":"B",
#         "Sponebob":"C",
#         "Patrick":"D"}
# student=input("Enter the name of a student: ")
# if student in grades:
#     print(f"{student} got {grades.get(student)}")
# else:
#     print(f"{student} is not here")
# email="BroCode@gmialcom"
# if "@" in email and "." in email:
#     print("Valid email")
# else:
#     print("Invalid")
# doubles=[]
# for x in range(1,11):
#     doubles.append(x*2)
# print(doubles)
# doubles=[]
# doubles=[x*2 for x in range(1,11)]
# triples=[x*3 for x in range(1,11)]
# print(doubles)
# print(triples)
# squares=[x**2 for x in range(1,11)]
# print(squares)
# fruits=["apple","orange","banana","coconut"]
# fruits=[fruit[0] for fruit in fruits]
# print(fruits)
# numbers=[1,-2,3,-4,5,-6,8,-3]
# positive_nums=[num for num in numbers if num>0]
# print(positive_nums)
# negative_nums=[num for num in numbers if num<0]
# print(negative_nums)
# even_nums=[num for num in numbers if num%2==0]
# odd_nums=[num for num in numbers if num%2!=0]
# print(odd_nums)
# grades=[85,42,79,90,61,30]
# passing_grades=[grade for grade in grades if grade>=60]
# print(passing_grades)
# def day_of_week(day):
#     if day==1:
#         print("it is Monday")
#     elif day==2:
#         print("it is Tuesday")
#     elif day==3:
#         print("it is Wednesday")
#     elif day==4:
#         print("it is Thursday")
#     elif day==5:
#         print("it is Friday")
#     elif day==6:
#         print("it is Saturday")
#     elif day==7:
#         print("it is Sunday")
#     else:
#         print("it is Invalid")
# day_of_week("python")
# day=input("Enter number of day of week: ")
# match day:
#     case "Saturday" | "Sunday":
#         print(True)
#     case "Tuesday" | "Monday" | "Wednesday" | "Thursday" | "Friday":
#         print(False)
#     case _:
#         print(False)
# print(help("modules"))
# import math as m
# print(m.pi)
# from math import pi
# print(pi)
# from math import e
# print(e)
# import example
# print(example.pi)
# result=example.square(9)
# print(result)
# def func1():
#     x=1
#     print(x)
# def func2():
#     x=2
#     print(x)
# func1()
# func2()
# def func1():
#     x=1
#     def func2():
#         print(x)
#     func2()
# func1()
# from math import e
# print(e)
# print(__name__)
# def favorite_food(food):
#     print(f"Your favorite food is {food}")
# def main():
#     print("This is brocode")
#     favorite_food("pizza")
# if __name__ == "__main__":
#     main()
# from example import *
# num_even_digits=0
# num_odd_digits=0
# total=0
# card_number=input("Enter a credit card: ")
# card_number=card_number.replace("-","")
# card_number=card_number.replace(" ","")
# card_number=card_number[::-1]
# for i in card_number[::2]:
#     num_odd_digits+=int(i)
# for i in card_number[1::2]:
#     i=int(i)
#     i*=2
#     if i>=10:
#         num_even_digits+=(1+(i%10))
#     else:
#         num_even_digits+=i
# total=num_even_digits+num_odd_digits
# if total%10==0:
#     print("Valid")
# else:
#     print("Invalid")
# def show_balance(balance):
#     print(f"Your balance is ${balance:.2f}")
# def deposit():
#     amount=float(input("Enter an amount to be deposited: "))
#     if amount<=0:
#         print("That is not a valid amount")
#         return 0
#     else:
#         return amount
# def withdraw(balance):
#     amount=float(input("Enter amount ot be withdrawn: "))
#     if amount<0:
#         print("That is not a valid amount")
#         return 0
#     elif amount>balance:
#         print("Insufficient funds")
#         return 0
#     else:
#         return amount
# def main():
#         balance=0
#         while True:
#                 print("Bancking Program")
#                 print("1.Show Balance")
#                 print("2.Deposit")
#                 print("3.Withdraw")
#                 print("4.Exit")

#                 choice=input("Enter your choice (1-4): ")
#                 if choice=="1":
#                         show_balance(balance)
#                 elif choice=="2":
#                         balance+=deposit()
#                 elif choice=="3":
#                         balance-=withdraw(balance)
#                 elif choice=="4":
#                         break
#                 else:
#                         print("That is not a valid choice")
#         print("Thank you! Have a nice day!")
# if __name__=="__main__":
#       main()
# Python Slot  Machine 
# import random as r
# def spin_row():
#     symbols=['🍒','🍉','🍋','🔔','⭐']
#     return [r.choice(symbols) for _ in range(3)]
# def print_row(row):
#     print("**************")
#     print(" | ".join(row))
#     print("**************")
# def get_payout(row,bet):
#     if row[0]==row[1]==row[2]:
#         if row[0]=='🍒':
#             return bet*3
#         elif row[0]=='🍉':
#             return bet*4
#         elif row[0]=='🍋':
#             return bet*5
#         elif row[0]=='🔔':
#             return bet*10
#         elif row[0]=='⭐':
#             return bet*20
#     return 0
# def main():
#     balance=100
#     print("***********************")
#     print("Welcome to Python Slots")
#     print("Symbols:  🍒🍉🍋🔔⭐")
#     print("***********************")
#     while balance>0:
#         print(f"Currenct balance: ${balance}")
#         bet=input("Place your bet amount: ")
#         if not bet.isdigit():
#             print("Please enter a valid number")
#             continue
#         bet=int(bet)
#         if bet>balance:
#             print("Insufficient funds")
#             continue
#         if bet<=0:
#             print("Bet must be greater than 0")
#             continue
#         balance-=bet
#         row=spin_row()
#         print("Spinning...\n")
#         print_row(row)
#         payout=get_payout(row,bet)
#         if payout>0:
#             print(f"You won ${payout}")
#         else:
#             print(f"Sorry,you lost this round")
#         balance+=payout
#         play_again=input("Do you want to spin again? (y/n)?: ").lower()
#         if play_again!='y':
#             break
#     print("*********************************************")
#     print(f"Game over! Your final balance is ${balance}")
#     print("*********************************************")
   


# if __name__=="__main__":
#     main()
# import random as r
# def spin_row():
#     symbols=['🍒','🍉','🍋','🔔','⭐']
#     return [r.choice(symbols) for i in range(3)]
# def print_row(row):
#     print("******************")
#     print(" | ".join(row))
#     print("******************")
# def get_payout(row,bet):
#     if row[0]==row[1]==row[2]:
#         if row[0]=='🍒':
#             return bet*3
#         elif row[0]=='🍉':
#             return bet*4
#         elif row[0]=='🍋':
#             return bet*5
#         elif row[0]=='🔔':
#             return bet*10
#         elif row[0]=='⭐':
#             return bet*20
#     return 0
# def main():
#     balance=100
#     print("**********************")
#     print("Welcome to Python Slot")
#     print("Symbols:  🍒🍉🍋🔔⭐")
#     print("**********************")
#     while balance>0:
#         print(f"Current balance: ${balance}")
#         bet=input("Place your bet amount: ")
#         if not bet.isdigit():
#             print("Please enter a valid number!")
#             continue
#         bet=int(bet)
#         if bet>balance:
#             print("Insufficient funds")
#             continue
#         if bet<=0:
#             print("Bet must be greater than 0")
#             continue
#         balance-=bet
#         row=spin_row()
#         print(row)
#         payout=get_payout(row,bet)
#         if payout>0:
#             print(f"You won ${payout}")
#         else:
#             print("Sorry,you lost this round")
#         balance+=payout
#         play_again=input("Do you want to play again (y/n)?: ").lower()
#         if not play_again=='y':
#             break
#     print("*******************************************")
#     print(f"Game over. Your final balance is {balance}")
#     print("*******************************************")
        

# if __name__=="__main__":
#     main()
# import random as r
# words=("apple","orange","banana","coconut","pineapple")
# hangman_art={0:("    -----",
#                 "    |   |",
#                 "        |",
#                 "        |",
#                 "        |",
#                 "        |",
#                 "========="),
#             1:("    -----",
#                "    |   |",
#                "    O   |",
#                "        |",
#                "        |",
#                "        |",
#                "========="),
#             2:("    -----",
#                "    |   |",
#                "    O   |",
#                "    |   |",
#                "        |",
#                "        |",
#                "========="),
#             3:("    -----",
#                "    |   |",
#                "    O   |",
#                "   /|   |",
#                "        |",
#                "        |",
#                "========="),
#             4:("    -----",
#                "    |   |",
#                "    O   |",
#                "   /|\\  |",
#                "        |",
#                "        |",
#                "========="),
#             5:("    -----",
#                "    |   |",
#                "    O   |",
#                "   /|\\  |",
#                "   /    |",
#                "        |",
#                "========="),
#             6:("    -----",
#                "    |   |",
#                "    O   |",
#                "   /|\\  |",
#                "   / \\  |",
#                "        |",
#                "=========")}
# def display_man(wrong_guess):
#     print("***************")
#     for line in hangman_art[wrong_guess]:
#         print(line)
#     print("***************")
# def display_hint(hint):
#     print(" ".join(hint))
# def display_answer(answer):
#     print(" ".join(answer))
# def main():
#     answer=r.choice(words)
#     hint=["_"]*len(answer)
#     wrong_guesses=0
#     guessed_letters=set()
#     while True:
#         display_man(wrong_guesses)
#         display_hint(hint)
#         guess=input("\nEnter a letter: ").lower()
#         if len(guess)!=1 or not guess.isalpha():
#             print("Invalid input")
#             continue
#         if guess in guessed_letters:
#             print(f"{guess} is already guessed")
#             continue
#         guessed_letters.add(guess)
        
#         if guess in answer:
#             for i in range(len(answer)):
#                 if answer[i]==guess:
#                     hint[i]=guess
#         else:
#             wrong_guesses+=1
#         if "_" not in hint:
#             display_man(wrong_guesses)
#             display_answer(answer)
#             print("YOU WIN!")
#             break
#         elif wrong_guesses>=6:
#             display_man(wrong_guesses)
#             display_answer(answer)
#             print("YOU LOSE!")
#             break





# if __name__=="__main__":
#     main()




















              











        
    
    





    







        



























