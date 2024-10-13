grafo={}
grafo["inicio"] = {"a": 7, "b": 3}
grafo["a"]={"fim":2}
grafo["b"]={"b":4, "fim": 5}
grafo["fim"]={}

infinito = float("inf")
custos = {"a": 4, "b": 2, "fim": infinito}
pais = {"a":"inicio", "b":"inicio", "fim": None}
processados=[]

def encontrar_menorCusto(custos):
  menorCusto = float("inf")
  nodo_menorCusto = None
  for nodo in custos: 
    custo = custos[nodo]
    if custo<menorCusto and nodo not in processados: 
      menorCusto = custo 
      nodo_menorCusto = nodo
  return nodo_menorCusto

nodo = encontrar_menorCusto(custos) 

while nodo is not None: 
  custo = custos[nodo]
  vizinhos = grafo[nodo]
  for n in vizinhos.keys(): 
    novo_custo = custo + vizinhos[n]
    if custos[n] > novo_custo: 
      custos[n] = novo_custo 
      pais[n] = nodo 
  processados.append(nodo) 
  nodo = encontrar_menorCusto(custos)

print(f'Custos: {custos}')
print(f'Pais: {pais}')
