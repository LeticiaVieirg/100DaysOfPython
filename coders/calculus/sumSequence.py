def calculateSum(int number) {
  sum=0
  sumSquare=0
  sumCubes=0

  number=int(input("Enter a number: "))

  for i in range(1, number+1):
    sum+=i;
    sumSquare+=i**2
    sunCubes+=i**3
  return sum, sumSquare, sumCubes

  sum, sumSquare, sumCubes=calculateSum(number)

  print(f"The sum of number is: {sum}")
  print(f"The sum of square is: {sumSquare}")
  print(f"The sum of cubes is: {sumCubes}")
}
