#lista de términos de fibonacci
def n_terminos_de_fibonacci(n):
    lista=[0,1]
    if n==0:
        return [0]
    elif n==1:
        return lista
    else:
        for x in range(0,n+1): 
            if x>1:
                lista.append(lista[x-1]+lista[x-2])
        return lista

#término n de fibonacci, siendo f(0)=0 y f(1)=1
def n_termino_de_fibonacci(n):
    lista=[0,1]
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        for x in range(0,n+1): 
            if x>1:
                lista.append(lista[x-1]+lista[x-2])
        return lista[x]

#suma de todos los términos fibonacci hasta el término n
def suma_de_n_terminos_de_fibonacci(n):
    lista=[0,1]
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        suma=1
        for x in range(0,n+1): 
            if x>1:
                lista.append(lista[x-1]+lista[x-2])
                suma+=lista[x]
        return suma