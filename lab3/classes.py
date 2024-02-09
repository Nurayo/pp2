#1
class StringManipulator:
    def __init__(self):
        self.input_string = ""

    def getString(self):
        self.input_string = input("Enter a string: ")

    def printString(self):
        print("String in upper case:", self.input_string.upper())

string_manipulator = StringManipulator()
string_manipulator.getString()
string_manipulator.printString()

#2
class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        return self.length * self.length

shape = Shape()
print("Area of Shape:", shape.area())

square = Square(4)
print("Area of Square:", square.area())

#3
class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

rectangle = Rectangle(4, 5)
print("Area of Rectangle:", rectangle.area())

#4
import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point coordinates: ({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        distance = math.sqrt(dx**2 + dy**2)
        return distance

x1 = float(input("Enter x-coordinate for point1: "))
y1 = float(input("Enter y-coordinate for point1: "))
point1 = Point(x1, y1)

x2 = float(input("Enter x-coordinate for point2: "))
y2 = float(input("Enter y-coordinate for point2: "))
point2 = Point(x2, y2)

point1.show()
point2.show()

distance = point1.dist(point2)
print(f"Distance between points: {distance}")

new_x = float(input("Enter new x-coordinate for point1: "))
new_y = float(input("Enter new y-coordinate for point1: "))
point1.move(new_x, new_y)

point1.show()

#5
class Account:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount. Please enter a positive amount.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self.balance}")
            else:
                print("Insufficient funds. Withdrawal amount exceeds the available balance.")
        else:
            print("Invalid withdrawal amount. Please enter a positive amount.")

owner = input("Enter the account owner's name: ")
initial_balance = float(input("Enter the initial balance: "))
account = Account(owner, initial_balance)
while True:
    action = input("Enter 'deposit', 'withdraw', or 'exit': ").lower()
    if action == 'exit':
        break
    if action == 'deposit':
        amount = float(input("Enter the deposit amount: "))
        account.deposit(amount)
    elif action == 'withdraw':
        amount = float(input("Enter the withdrawal amount: "))
        account.withdraw(amount)
    else:
        print("Invalid action. Please enter 'deposit', 'withdraw', or 'exit'.")

#6
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

prime_numbers = list(filter(lambda x: is_prime(x), numbers))
print("Prime numbers in the list:", prime_numbers)
