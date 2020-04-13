def a_power_b(a,b):
    resultado=pow(a,b)
    return resultado
a=2
b=2
while a > 0:
    a=int(input("Ingrese un numero:"))
    b=int(input("Ingrese otro numero: "))
    print(a_power_b(a,b))
    if a == 0:
        print("a vale cero, el ciclo termino")
        break