class Animal:
    def __init__(self, name, species, age, sound):
        self.name = name
        self.species = species
        self.age = age
        self.sound = sound

    def make_sound(self):
        return f"{self.name} says {self.sound}"

    def get_info(self):
        return f"{self.name} is a {self.age}-year-old {self.species}"


# Creating 4 animal objects
dog = Animal("Doggy", "Dog", 5, "Woof")
cat = Animal("Cherry", "Cat", 3, "Meow")
cow = Animal("Tommy", "Cow", 8, "Moo")
bird = Animal("Ducky", "Bird", 1, "Tweet")

# Using the objects
print(dog.get_info())
print(dog.make_sound())

print(cat.get_info())
print(cat.make_sound())

print(cow.get_info())
print(cow.make_sound())

print(bird.get_info())
print(bird.make_sound())


#test two


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

    def display(self):
        print(f"Length: {self.length}")
        print(f"Width: {self.width}")
        print(f"Perimeter: {self.perimeter()}")
        print(f"Area: {self.area()}")
        print()  # Just for formatting


# Creating 4 objects of the Rectangle class
rect1 = Rectangle(2, 10)
rect2 = Rectangle(4, 12)
rect3 = Rectangle(4, 6)
rect4 = Rectangle(6, 14)

# Displaying details of each rectangle
rect1.display()
rect2.display()
rect3.display()
rect4.display()

# assigment tuesday

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
# Creating a savings account and performing operations
savings = SavingsAccount("12345", "John", 1000.0)
savings.deposit(200)
savings.withdraw(100)
savings.add_interest()
savings.apply_bank_fees()

# Creating a checking account and performing operations
checking = CheckingAccount("67890", "Mwende", 500.0)
checking.deposit(300)        # Display after deposit
checking.withdraw(900)       # Display after withdrawal within overdraft limit
checking.apply_bank_fees()   # Display after applying bank fees

