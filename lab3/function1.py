#1
grams = float(input())
def ounces(grams):
    print(28.3495231 * grams)
ounces(grams)

#2
def centigrade(f):
    return (5 / 9) * (f - 32)
f = float(input())
result = centigrade(f)
print(result)

#3
def solve(numheads, numlegs):
    for num_chickens in range(numheads + 1):
        num_rabbits = numheads - num_chickens
        if (2 * num_chickens + 4 * num_rabbits) == numlegs:
            return num_chickens, num_rabbits
    return None

numheads = 35
numlegs = 94
result = solve(numheads, numlegs)

if result:
    num_chickens, num_rabbits = result
    print(num_chickens)
    print(num_rabbits)
else:
    print("No solution found")

#4
def is_prime(num):
    return num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1))

def filter_prime(numbers):
    prime_numbers = []
    for num in numbers:
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers
numbers_str = input()
numbers = [int(num) for num in numbers_str.split()]

prime_numbers = filter_prime(numbers)

print(prime_numbers)

#5
def perm(a, l, r):
    if l == r:
        print(a)
    else:
        for i in range(l, r):
            a[l], a[i] = a[i], a[l]
            perm(a, l+1, r)
            a[l], a[i] = a[i], a[l]

string = input()
n = len(string)
a = list(string)
perm(a, 0, n)

#6
def reverse(s, start, end):
    while start < end:
        s[start], s[end] = s[end], s[start]
        start = start + 1
s = input()
s = list(s)
start = 0

while start < len(s):
    end = s.index('', start)
    reverse(s, start, end - 1)
    start = end + 1
s.reverse()
s = "".join(s)
print(s)


#7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))

#8
def spy_game(nums):
    code = [0, 0, 7]
    index = 0
    
    for num in nums:
        if num == code[index]:
            index += 1
            if index == len(code):
                return True
    
    return False

print(spy_game([1, 2, 4, 0, 0, 7, 5]))
print(spy_game([1, 0, 2, 4, 0, 5, 7]))
print(spy_game([1, 7, 2, 0, 4, 5, 0]))

#9
import math

def sphere_volume(radius):
    if radius < 0:
        return "Radius cannot be negative"
    
    volume = (4/3) * math.pi * radius**3
    return volume

radius = input()
result = sphere_volume(radius)
print(result)


#10
def unique_elements(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

original_list = [1, 2, 2, 3, 4, 4, 5]
result = unique_elements(original_list)
print("Original List:", original_list)
print("List with Unique Elements:", result)

#11
def is_palindrome(word):
    cleaned_word = ''.join(word.lower().split())
    return cleaned_word == cleaned_word[::-1]
word = "madam"
result = is_palindrome(word)

if result:
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")

#12
def histogram():
    input = input()
    if all(num.isdigit() or (num[1:].isdigit() and num[0] == '-') for num in input.split()):
        numbers = [int(x) for x in input.split()]

        for num in numbers:
            print('*' * num)
histogram()


#13
import random

def guess_the_number():
    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    
    gen_number = random.randint(1, 20)
    
    guesses_taken = 0

    while True:
        print("Take a guess.")
        guess = int(input())
        guesses_taken += 1

        if guess < gen_number:
            print("Your guess is too low.")
        elif guess > gen_number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
            break

guess_the_number()
