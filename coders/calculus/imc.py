def calculate_imc(weight, height):
  if height <=0 or weight:
    raise ValueError("Height and weight must be greater than 0!")

  imc=weight/(height*height)
  return imc

def main():
  try:
    weight=float(input("Enter a value of the weight in kg: "))
    height=float(input("Enter a value of the height in metters: "))
  except ValueError:
    print("Enter valid numbers! ")
    return

imc=calculate_imc(weight, height)
print(f"Your IMC is {imc: .2f}")

  if imc < 18.5:
    print("Classification: Underweight")
  elif imc < 25:
    print("Classification: Ideal weight")
  elif imc < 30:
    print("Classification: Overweight")
  elif imc < 35:
    print("Classification: Grade I obesity")
  elif imc < 40:
    print("Classification: Grade II obesity")
  else:
    print("Classification: Grade III obesity")

if __name__ == "__main__":
  main()
