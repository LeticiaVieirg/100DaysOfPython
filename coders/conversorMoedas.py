print("----------" "\n1 - Dolar", "\n2 - Euro", "\n3 - Libra", \n ----------")

tipoMoeda=int(input("Informe o tipo da moeda para converter: "))

def conversao (tipoMoeda):
   if tipoMoeda==1:
      print("Conversão de dolar para real")
      valor=float(input("Digite o valor para converter: ")
      valor=valor*5.07
      valorAproximado=round(valor,2)
      print("O valor convertido e:", valorAproximado)

      
