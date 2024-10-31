class Student:
    first_name = "Jane"
    last_name = "Achieng"
    gender = "Female"
    age = "22"
class Person:
    def __init__(self,name,marital_status,gender,occupation):
        self.name =name
        self.marital_status = marital_status
        self.gender = gender
        self.occupation = occupation

    def salutation(self):
            print(f"Good afternoon {self.name}, you are {self.marital_status}")

    def display_name(self):
        print(f"Your name is {self.name}")

class Animal:
    def __init__(self,name,age,sound,species):
        self.name = name
        self.age = age
        self.sound = sound
        self.species = species

class Employee:
    def __init__(self,name,age,salary,gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.salary = salary

    def display_name(self):
        return f"{self.name} is {self.age} years old"


class Manager(Employee):
    def __init__(self,name,salary,age,gender,education_level):
        super().__init__(name,age,salary,gender)
        self.education_level = education_level

class Developer(Employee):
    def __init__(self,name,age,gender,salary,prog_language):
        super().__init__(name,age,gender,salary)
        self.prog_language = prog_language


#class assignment
class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"\nDeposited ksh{amount:.2f} successfully!")
            self.display()
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"\nWithdrew ksh{amount:.2f} successfully!")
            self.display()
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def apply_bank_fees(self):
        fee = self.balance * 0.05
        self.balance -= fee
        print("\nBank fees of 5% applied.")
        self.display()

    def display(self):
        print("\n--- Account Details ---")
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Balance: ksh{self.balance:.2f}")
        print("-----------------------\n")

class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0.0, interest_rate=0.02):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"\nInterest of {self.interest_rate*100}% added.")
        self.display()

class CheckingAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0.0, overdraft_limit=500):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if 0 < amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"\nWithdrew ksh{amount:.2f} successfully!")
            self.display()
        else:

            print("Withdrawal exceeds overdraft limit or is invalid.")

#Vehicle
class Vehicle:
  def start(self):
    print("Vehicle is starting.")

class Car(Vehicle):
    def start(self):
        print("Car is starting with ignition.")

class Bike(Vehicle):
    def start(self):
        print("Bike is starting with a kick.")


# device

class Device:
    def __init__(self,brand,year,model):
        self.brand = brand
        self.year = year
        self.model = model
class Phone(Device):
    def __init__(self, brand, year, model):
        super().__init__(brand, year, model)  # Call the parent class's __init__ method
        self.model = model

# morning warm up
class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

def perimeter(self):
    return 2 * (self.length + self.width)

def area(self):
    return self.length * self.width

def display_info(self):
    print(f" length: {self.length}, width: {self.width}")
    print(f"perimeter:{self.perimeter()}")
    print(f"area:{self.area()}")















