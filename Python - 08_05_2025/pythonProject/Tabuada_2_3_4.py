# Tabuada do 2, do 3 e do 4

def tabuada(numero):
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} X {i} = {resultado}")
    print("\n")

tabuada(2)
tabuada(3)
tabuada(4)