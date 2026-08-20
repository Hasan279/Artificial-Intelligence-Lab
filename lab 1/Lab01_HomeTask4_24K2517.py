def triangle(n):
    for i in range(1, n+1):
        for j in range (1, i+1):
            print(j, end= ' ')
        print()

def multiplication_table(*numbers):
    for num in numbers:
        print(f"\nMultiplication Table for {num}:")
        for i in range(1, 11):
            print(f"{num} x {i} = {num * i}")
    return None

def fibonacci(limit):
    fib_list = [0,1]
    i = 1
    a = 1
    while a < limit:
        a = fib_list[i] + fib_list[i-1]
        fib_list.append(a)
        i +=1
    fib_list.pop()
    return fib_list

def collatz(n):
    a = n
    steps = 0
    while a != 1:
        if a%2 == 0: a = a/2
        else: a = 3*a + 1
        steps +=1
    return steps


triangle(5)

multiplication_table(3, 7, 12)

fib_list = fibonacci(100)
print("Fibonacci series:", fib_list)

steps = collatz(27)
print("Collatz steps:", steps)
