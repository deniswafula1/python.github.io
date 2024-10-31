from main import Student, Manager, Developer ,Rectangle,Employee,Phone,Device,SavingsAccount,CheckingAccount,Vehicle,Car,Bike
from main import Person
from main import Animal
student1 = Student()
print(student1.first_name)
print(student1.last_name)
print(student1.gender)
print(student1.age)

student2 = Student()
print(student2.first_name)
print(student2.last_name)
print(student2.gender)
print(student2.age)

person1 = Person("Jane","Married", "Female", "Teacher")
person2 = Person("Joel", "Divorced", "Male", "Programmer")
person3 = Person("Dennis", "Single", "Male", "Developer")
person4 = Person("Merry", "Single", "Female", "Lecture")
print(person1.name)
print(person3.marital_status)
print(person3.gender)
print(f"Name:{person4.name}, Gender:{person4.gender}, Occupation:{person4.occupation}")

animal1 = Animal("Tigger", "20","Mellow","Animalia")
animalia2 = Animal("Lion","15","ngrrrh","Simba")
animal3 = Animal("Dog","6","Woof","Canivores")
animal4 = Animal("Cat","3","Meow","Felis catus")
print(f"Name:{animal1.name} Age:{animal1.age} Sound:{animal1.sound} Species:{animal1.species} ")

person1.salutation()
person2.salutation()
person3.salutation()
person4.salutation()

person1.display_name()
person2.display_name()
person3.display_name()

employee1 = Employee("Okoth","24","2000","Male",)
manager1 = Manager("name","2000","34","Male","Degree")
developer1 = Developer("Wafula","21","Male","50000","Java")

print(employee1.name)
print(employee1.gender)
print(employee1.salary)
print(employee1.age)

savings = SavingsAccount("12345", "Melisa ", 7000.0)
savings.deposit(200)
savings.withdraw(100)
savings.add_interest()
savings.apply_bank_fees()

checking = CheckingAccount("67890", "Dennis", 500.0)
checking.deposit(300)
checking.withdraw(900)
checking.apply_bank_fees()

#assignment

#vehicle output
vehicle = Vehicle()
vehicle.start()
#car output
car = Car()
car.start()

#bike output
bike = Bike()
bike.start()

phone1 = Phone("Nokia","2024","version 14")
device1 = Device("Iphone Pro","2025","Version23")

print(f"Brand: {phone1.brand}")
print(f"Year: {phone1.year}")
print(f"Model: {phone1.model}")

print(f"Brand: {device1.brand}")
print(f"Year: {device1.year}")
print(f"Model: {device1.model}")

rectangle1 = Rectangle("12","20")
rectangle2 = Rectangle("23","77")
rectangle3 = Rectangle("20","5")
rectangle4 =Rectangle("40","20")

rectangle1.display()


