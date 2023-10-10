#Write a script that will calculate the factorial of the entered number without using recursion.
#Example : 0!=1, 1!=1,2!=2, 3!=1*2*3=6, ....

def calculate_factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

try:
    number = int(input("Enter a number: "))
    result = calculate_factorial(number)
    print(f"The factorial of {number} is {result}")
except ValueError:
    print("Invalid input. Please enter a valid number.")
