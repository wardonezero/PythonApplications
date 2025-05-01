# Create a class named Car with no methods or attributes. Then, create an instance of this class and print the type of the instance.
# Modify the Car class to accept brand and model as parameters during object creation. Then, create an instance and print the attributes.
# Extend the Car class by adding a method display_info() that prints the brand and model of the car.
# Modify the Car class to have a default value for the model ("Unknown"). If the model is not provided during initialization, it should use the default value.
class Car:
    def __init__(self, brand, model="Unknown"):
        self.brand = brand
        self.model = model

    def displayInfo(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

car = Car()
print(type(car))
car1 = Car("Rolls-Royce", "Specter")
print(f"Brand: {car1.brand}, Model: {car1.model}")
car1.display_info()
car2 = Car("Audi")
car2.display_info()


# Create a class Person with attributes name and age. Create three instances of this class and store them in a list. Then, loop through the list and print each person's information.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


people = [Person("Alice", 30), Person("Bob", 25), Person("Charlie", 35)]
for person in people:
    person.display_info()

#Create a class BankAccount with account_number and balance. Add a method deposit(amount) to increase the balance
#Modify the BankAccount class to include a withdraw(amount) method that reduces the balance if there are enough funds.
import decimal

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount: decimal.Decimal):
        if amount <= 0 not isinstance(amount, decimal.Decimal , float, int):
            raise ValueError("Invalid amount")
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount: decimal.Decimal):
        if amount <= 0 not isinstance(amount, decimal.Decimal , float, int):
            raise ValueError("Invalid amount")
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
account = BankAccount("123456789")
account.deposit(1000)
account.withdraw(500)

# Create a class Student that keeps track of the total number of students created using a class variable.
#Modify the Student class to include a __str__ method so that printing a student instance displays their name.
class Student:
    total_students = 0

    def __init__(self, name):
        self.name = name
        Student.total_students += 1

    @classmethod
    def get_total_students(cls):
        return cls.total_students

    def __str__(self):
        return f"Student Name: {self.name}"
student1 = Student("Alice")
student2 = Student("Bob")
print(student1)
print(student2)
print(f"Total students: {Student.get_total_students()}")

#Create a class Employee with name and salary. Add a method give_raise(amount) that increases the salary
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def give_raise(self, amount):
        if amount <= 0 not isinstance(amount, decimal.Decimal , float, int):
            raise ValueError("Invalid amount")
        self.salary += amount
        print(f"New salary for {self.name}: {self.salary}")
employee = Employee("Alice", 50000)
employee.give_raise(5000)