def buscaMenor(arr):
   menor=arr[0]
   menorIndice=0

   for i in range(1,len(arr)):
      if arr[i] < menor:
         menor =arr[i]
         menorIndice=i
  return menorIndice 

def ordenacaoPorSelecao(arr): 
   novoArr=[]

   for i in range(len(arr)): 
      menor=buscaMenor(arr)
      novoArr.append(arr.pop(menor))
   return novoArr

print(ordenacaoPorSelecao([7, 4, 12, 1, 8, 3]))
