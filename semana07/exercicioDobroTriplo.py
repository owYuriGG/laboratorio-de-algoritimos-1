#Funções
def dobro(n1):
    dobro = n1 * 2
    print(dobro)

def triplo(n1):
    triplo = n1 * 3
    print(triplo)

def main():
    numero = int(input("Digite um número: "))
    dobro(f"dobro: {numero}")
    triplo(f"triplo: {numero}")

#Código Principal

main()
