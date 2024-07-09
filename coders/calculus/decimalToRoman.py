def decimalRoman(number){

  romanNumeral=""
  
  if number<=0 or number>=4000:
    reaise ValueError("Number must between 1 and 3999")
  
  romanMap={
    1000="M",
    900="CM",
    500="D",
    400="CD",
    100="C",  
    90="XC",
    50="L",
    40="XL",
    10="X",
    9="IX",
    5="V",
    4="IV",
    1="I"
  }

  for value, sybol in romanMap.items():
    while number>=value:
      romanNumeral+=sybol
      number-=value
  return romanNumeral
 
def main(){
  try: 
    decimalNumber=int(input("Enter a number to convert: "))
    romanNumber=decimalRoman(decimalNumber)
    print(f"{decimalNumber} in Roman numerals is: {RomanNumber}")
  except ValueError as e:
    print(e)
}

if "__name__"=="__main__":
  main()
