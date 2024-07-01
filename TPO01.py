# Lista de materias
materias = [
    {"ID": 1, "Materia": "Matematicas", "Horas_catedra": 40, "Turno": "Mañana"},
    {"ID": 2, "Materia": "Lengua", "Horas_catedra": 40, "Turno": "Mañana"},
    {"ID": 3, "Materia": "Ciencias Naturales", "Horas_catedra": 40, "Turno": "Mañana"},
    {"ID": 4, "Materia": "Ciencias Sociales", "Horas_catedra": 40, "Turno": "Mañana"}
]

# Función para mostrar el menú
def mostrar_menu():
    print("\nMenu:")
    print("1. Agregar materia")
    print("2. Listar materias")
    print("3. Buscar materia")
    print("4. Eliminar materia")
    print("5. Modificar materia")
    print("6. Salir")

def agregar_materia(materias):
    if materias:
        ultimo_id = materias[-1]["ID"]
    else:
        ultimo_id = 0
        
    nuevo_id = ultimo_id + 1
    materia = input("Ingrese el nombre de la materia: ")
    horas_catedra = int(input("Ingrese la cantidad de horas catedra: "))
    turno = input("Ingrese el turno: ")
    
    nueva_materia = {"ID": nuevo_id, "Materia": materia, "Horas_catedra": horas_catedra, "Turno": turno}
    materias.append(nueva_materia)
    print(f"La materia {materia} fue agregada exitosamente con el ID {nuevo_id}")

# Función para listar todas las materias
def listar_materias(materias):
    if materias:
        # Encabezado de la tabla
        print("-" * 68)
        print(f"| {'ID':<5} | {'Materia':<30} | {'H. Catedra':<10} | {'Turno':<10} |")
        print("-" * 68) # Línea separadora
    
        # Filas de las materias
        for materia in materias:
            print(f"| {materia['ID']:<5} | {materia['Materia']:<30} | {materia['Horas_catedra']:<10} | {materia['Turno']:<10} |")
            print("-" * 68)
    else:
        print("No hay materias cargadas.")

def main():
    while True:
        mostrar_menu()
        opcion = input("Ingrese su opcion: ")
        if opcion == "1":
            agregar_materia(materias)
        elif opcion == "2":
            listar_materias(materias)
        elif opcion == "6":
            print("Saliendo del sistema de gestion de materias")
            break

main()
print(materias)