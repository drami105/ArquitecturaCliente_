#Elaborado por Duban Ferney Ramírez Suárez

# Defino arreglo para almacenar las tareas en la memoria cliente
tareas = []

# Función para agregar tarea
def agregar_tarea(tarea):
    tareas.append(tarea)
    print(f"Tarea '{tarea}' añadida.")

# Función para ver las tareas
def ver_tareas():
    #Valido si el arreglo está vacío
    if tareas:
        print("Tareas actuales:")
        for tarea in tareas:
            print(f"- {tarea}")
    else:
        #En caso de que no haya tareas agregadas
        print("No hay tareas.")

# Función para eliminar tarea
def eliminar_tarea(tarea):
    if tarea in tareas:
        #Elimino la tarea
        tareas.remove(tarea)
        print(f"Tarea '{tarea}' eliminada.")
    else:
        #En caso de que no se encuentre la tarea
        print(f"Tarea '{tarea}' no encontrada.")

# Función principal
def main():
    while True:
        # Se muestran las opciones que se pueden utilizar
        print("\nOpciones:")
        print("1. Agregar tarea")
        print("2. Ver tareas")
        print("3. Eliminar tarea")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        # Se determina que acción realizar según la opción seleccionada
        if opcion == '1':
            tarea = input("Ingrese la tarea a agregar: ")
            agregar_tarea(tarea)
        elif opcion == '2':
            ver_tareas()
        elif opcion == '3':
            tarea = input("Ingrese la tarea a eliminar: ")
            eliminar_tarea(tarea)
        elif opcion == '4':
            print("Saliendo...")
            break
        else:
            # Mensaje para opciones no válidas
            print("Opción no válida.")

if __name__ == "__main__":
    main()
