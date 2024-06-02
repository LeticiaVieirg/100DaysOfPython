qtd_interacao = int(input("Informe o termo da Fibonacci que você deseja saber: "))

contador = 2
valor1 = 0
valor2 = 1
valor3 = 0

if qtd_interacao == 0:
   print("O primeiro termo da sequência é: 0")
elif qtd_interacao == 1:
   print("O segundo termo da sequência é: 1")
else:
   while qtd_interacao > contador:
      valor3 = valor1 + valor2
      valor1 = valor2
      valor2 = valor3
      contador += 1
   print("O termo {} da sequência de Fibonacci é: {}".format(qtd_interacao, valor3)
