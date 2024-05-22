from collections import deque

grafo={ 
'Clara': ['Diana', 'Aline', 'Joana'],
'Diana': ['Luiza', 'Bruna'],
'Aline': ['Italo', 'Pedro'],
'Joana': ['Bruna'],
'Luiza': [],
'Bruna': [],
'Italo': [],
'Pedro': []
}

def pessoaAtleta(nome):
  return nome[-1]=='m'

def pesquisar(nome):
  filaPesquisa=deque(nome)
  filaPesquisa+=grafo[nome]
  pessoasVerificadas=[]
  
  while filaPesquisa:
    pessoa=filaPesquisa.popleft()
    if pessoa not in pessoasVerificadas:
       if pessoaAtleta(pessoa):
         print(f'{pessoa} eh um atleta.')
         return True
       else:
         filaPesquisa+=grafo[pessoa]
         pessoasVerificadas.append(pessoa)   
     return False

pesquisa('Clara')
