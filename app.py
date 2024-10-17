from recursividade import fatorial

if __name__ == "__main__":
    try:
        n = int(input("Informe um número inteiro positivo: "))
        if n >= 0:
            print(f"{n}! = {fatorial(n)}.")
        else:
            print(f"Não existe fatorial de {n}.")
    except Exception as e:
        print(f"Não foi possível calcular o fatorial. {e}.")

    