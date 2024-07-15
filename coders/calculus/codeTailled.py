def fatorial_com_cauda(n, acumulador=1):
  if n == 0:
    return acumulador
  else:
    return fatorial_com_cauda(n - 1, n * acumulador)
