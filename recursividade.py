
#criando uma funçao recursiva espelho dentro de espelho
def fatorial(n):
    # Caso base: o fatorial de 0 ou 1 é 1
    if n==0:
    
 
        return 1
    else:
        # Chamada recursiva
        return n * fatorial(n - 1)



