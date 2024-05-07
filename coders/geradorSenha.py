import secrets
import string

def geraSenha(tamanho=10):
   senha = ''
   tamanho = max(min(tamanho, 20), 12)
   caracteres = string.ascii_letters + string.digits + string.punctuation
   senha =''.join(secrets.choice(caracteres) for_ in range(tamanho))
   return senha

tamanhos = [12,14,17, 20]
senhas = [gerar_senha(tamanho) for tamanho in tamanhos]

for senha in senhas:
   print(senha)
