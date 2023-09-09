Motos = {
    'Honda': 'African Twin 1100',
    'BMW': 'Turing 1250',
    'Ducati': 'Desert X 960',
    'Royal Enfield': 'Super Meteoro 650',
}

while True:
    print("\nMenu:")
    print("1. Agregar motos")
    print("2. Buscar motos")
    print("3. Actualizar motos")
    print("4. Eliminar motos")
    print("5. Listar motos")
    print("6. Salir")

    opcion = input("Digite una opción: ")

    if opcion == "1":
        nombre = input("Ingrese la marca de la moto: ")
        cilindraje = input("Ingrese el cilindraje: ")
        Motos[nombre] = cilindraje
        print(f"motos '{nombre}' agregado correctamente.")

    elif opcion == "2":
        nombre = input("Ingrese el nombre de la marca a buscar: ")
        cilindraje = Motos.get(nombre, "No se encontró la marca de la moto")
        print(f"la moto '{nombre}' su cilindraje es: {cilindraje}")

    elif opcion == "3":
        nombre = input("Ingrese la marca de la moto que desea actualizar: ")
        if nombre in Motos:
            nuevo_cilindraje = input("Ingrese el nuevo cilindraje: ")
            Motos[nombre] = nuevo_cilindraje
            print(f"la moto  '{nombre}' fuen actualizada correctamente.")
        else:
            print(f"'{nombre}' no se encontró en la lista de motos.")

    elif opcion == "4":
        nombre = input("Ingrese el nombre de la marca de la moto que desea eliminar: ")
        if nombre in Motos:
            del Motos[nombre]
            print(f"La la marca'{nombre}' fue eliminada correctamente.")
        else:
            print(f"'{nombre}' no se encontró en la lista de motos.")

    elif opcion == "5":
        print("\nLista de Motos:")
        for marca, modelo in Motos.items():
            print(f"{marca}: {modelo}")

    elif opcion == "6":
        print("Saliendo del programa.")
        break

    else:
        print("Opción no válida. Por favor, elija una opción válida del menú.")

