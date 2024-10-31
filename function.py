def my_function():
    print("Hello ,world")
    print("Hello ,world")
    print("Hello ,world")
    print("Hello ,world")
    print("Hello ,world")
    print("Hello ,world")

my_function()

def my_func():
    name="Wafula"
    print(name)

my_func()

def my_func2(name):
  print(name)

my_func2("kemboi")
my_func2("osoo")
my_func2("elvis")

def concate( first_name):

 print("hello " + first_name + " how are you? ")
 concate("abedy")
 concate("liz")

#def concate2(first_name,last_name,age)

 # print(f"hello {first_name} {last_name}, you are {age} years old")

#concate2(first_name:"wafula", last_name"wafula":"kipkemboi")


#def multyply(num1,num2):
  #  multiplier = num1 * num2
   # return multiplier

#print(multyply(num1num2:,100))

#def age_calc():
# new_age = current_age -10
 #return new_age
#print(age_calc(21))#

def school(name,age,):
    if age>5 and age<=10:
        return f"{name} your age {age} years old for lower secondary"
    if age > 10 and age <= 15:
        return f"{name} your age {age} years old for upper secondary"
    if age > 15 and age <= 20:
        return f"{name} your age {age} years old for juniour secondary"
    if age > 20 and age <= 25:
        return f"{name} your age {age} years old for none secondary"


# Greating function
def greet(name):
    if name == 'Alice' or name == 'Bob':
        return f"Your are {name}, Thank you"
    else:
        return f"How are you doing today"
fname = greet('Bob')
print(fname)


# Finding grater number
def great(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return f'{num1} is greater than {num2} and {num3}'
    elif num2 > num1 and num2 > num3:
        return f'{num2} is greater than {num1} and {num3}'
    elif num3 > num1 and num3 > num2:
        return f'{num3} is greater than {num1} and {num2}'
    else:
        return 'All numbers are equal or not in range'

numbersGreater = great(12, 93, 89)
print(numbersGreater)


# list calculator
def add_numbers(numbers):
    return sum(numbers)

#list = [2, 4, 89, 9]

print(add_numbers([2, 4, 89, 9 ]))





