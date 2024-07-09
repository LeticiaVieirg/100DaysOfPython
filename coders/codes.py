for i in range(128):
  tensDigit = chr(i // 10 + ord('0'))
  unitsDigit = chr(i % 10 + ord('0'))
  print(tensDigit * 5 + unitsDigit * 5)
