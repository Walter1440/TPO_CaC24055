# Pedir un numero entero al usuario
# y determinar si es o no par.

valor = int(input("Ingrese un valor entero: "))

# Utilizamos IF para determinar la paridad:
if valor % 2 == 0:
    print("El numero", valor, "es PAR.")
else:
    print("El numero", valor, "es IMPAR.")
