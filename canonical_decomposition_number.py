#definimos la funcion que traiga los primos que hay hasta cierto numero
ListaPrimos = []
def Primos(HastaNumero):
    for i in range(2, HastaNumero+1):
        for j in range(2, i):
            if (i % j == 0):
                break
        else:
            ListaPrimos.append(i)
    return(ListaPrimos)
        
#definimos la funcion con la que se descompondra un numero
ListaDescompo = []
def Descomposicion(DescompoNumero):
    Primos(int(DescompoNumero))
    for i in ListaPrimos:
        if (DescompoNumero%i==0):
            ListaDescompo.append(i)
    print(f"{DescompoNumero} es descompuesto por ", end="")
    for j in ListaDescompo:
        Contador = 0
        while (DescompoNumero%j==0):
            Contador = Contador + 1
            DescompoNumero = DescompoNumero/j
        print(f"{j} ^ {Contador}", end="")
        if (j != ListaDescompo[-1]):
            print(" x ", end="")

#de la siguiente forma se obtendra el ValorEntrada que nos dara la persona y se analizara
ValorEntrada = int(input("Ingrese el numero"))
Descomposicion(ValorEntrada)

"""
import random
Prueba = random.randrange(1,300)
Descomposicion(Prueba)
"""