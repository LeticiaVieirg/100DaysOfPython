def palindromo(numero):
  numero_invertido = 0
  numero_original = numero
  while numero != 0:
    numero_invertido = numero_invertido * 10 + numero % 10
    numero //= 10
  return numero_original == numero_invertido

def main():
  maior_palindromo = 0

  for i in range(100, 1000):
    for j in range(i, 1000):
      produto = i * j
      if palindromo(produto) and produto > maior_palindromo:
        maior_palindromo = produto

  print(f"O maior palíndromo produto de dois números de três dígitos é: {maior_palindromo}")

if __name__ == "__main__":
  main()
