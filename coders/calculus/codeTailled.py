def factorial_tail(n, accumulator=1):
  if n == 0:
    return accumulator
  else:
    return factorial_tail(n - 1, n * accumulator)
