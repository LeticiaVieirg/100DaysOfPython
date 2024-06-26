#limite de 1-12 caracteres 

import random
import string

def gerar_senha(tamanho_senha):
  if tamanho_senha < 1 or tamanho_senha > 12:
    raise ValueError("Tamanho da senha deve estar entre 1 e 12 dígitos.")

  #Conjunto de caracteres para formar a senha
  caracteres = string.ascii_letters + string.digits

  #Gera a senha de forma aleatoria
  senha = "".join(random.choice(caracteres) for _ in range(tamanho_senha))

  return senha

#Solicita o tamanho da senha ao usuário e informa os limites
tamanho_senha = int(input("Informe o tamanho da senha (entre 1 e 12): "))

#Gera e imprime a senha aleatória 
senha_gerada = gerar_senha(tamanho_senha)
print(f"Sua senha aleatória com {tamanho_senha} dígitos é: {senha_gerada}")

