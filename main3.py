def a_power_b(a,b):
    resultado=pow(a,b)
    return resultado
a=2
b=2
contador=0
while a > 0:
    a=int(input("Ingrese un numero:"))
    b=int(input("Ingrese otro numero: "))
    print(a_power_b(a,b))
    contador=contador+1
    if a == 0:
        print("A tomo valor de cero, el ciclo termino con un total de",contador,"potencias")
        break