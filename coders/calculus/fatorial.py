def recursive_factorial(n):
  if n == 0:
    return 1
  else:
    return n * recursive_factorial(n - 1)
    
number=int(input("Enter a number: "))
factorial=recursive_factorial(number)
print(f"The factorial of the number is:{factorial}")
