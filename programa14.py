# Pedir un valor entero comprendido entre
# 1 y 10. Segun sea el valor, mostrar:
# 1..3: Desaprobado.
# 4..6: En proceso.
# 7..9: Aprobado.
#   10: Excelente.
# ---------------------------------------

nota = int(input("Ingrese su nota: "))

if nota >= 1 and nota <= 3:
    print("Desaprobado.")
else:
    if nota >= 4 and nota <= 6:
        print("En proceso.")
    else:
        if nota >= 7 and nota <= 9:
            print("Aprobado.")
        else:
            print("Excelente.")
            
print("Programa finalizado.")
