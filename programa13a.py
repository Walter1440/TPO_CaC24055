# Pedir el numero entero al usuario
# y determinar si esta dentro del
# intervalo cerrado [18;65]

numero = int(input("Ingrese un numero entero:"))

if numero >= 18 and numero <=65:
    print("El numero es correcto.")
else:
    print("Numero fuera de rango.")
            
print("Programa finalizado.")