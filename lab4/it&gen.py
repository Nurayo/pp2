#1
def gensquares(N):
    for i in range(N): 
        yield i**2
N = 5
gen = gensquares(N)
for square in gen:
    print(square)


#2
def evengen(n):
    for i in range(0,n + 1, 2):
        yield i
n = int(input())
even = evengen(n)
even_str = ',' join(map(str, even))
print(f"Even numbers between 0 and {n}: {even_numbers_str}")


#3
def my_generator(n):
    i = 0
    while i < n:
        if i % 3 == 0 or i % 4 == 0:
            yield i
        i += 1
        
n = int(input())

for i in my_generator(n):
    print(i)
    
    
#ex 4
def squares(a, b):
    while a <= b:
        yield a**2
        a += 1
a = int(input())
b = int(input())
for i in squares(a, b):
    print(i)
    
#ex 5

def my_generator(n):
    while n > 0:
        yield n
        n -= 1
n = int(input())
for i in my_generator(n):
    print(i)