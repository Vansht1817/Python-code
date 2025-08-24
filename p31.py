#Write a program to find the factorial of a given number using recursion.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# Input from user
number = int(input("Enter a number to find its factorial: "))
# Calculate factorial
result = factorial(number)
# Display result
print(f"The factorial of {number} is: {result}")

