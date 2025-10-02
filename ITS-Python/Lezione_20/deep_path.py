def fib_memo(n):
    if n<= 0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return fib_memo(n-1)+fib_memo(n-2)

# Driver Program

print(fib_memo(10))