"""1. Lectura de archivo
Crear una función llamada leer_inventario(nombre_archivo) que lea el archivo
inventario.txt y devuelva una lista de diccionarios, donde cada libro es
representado con claves: 'codigo', 'titulo', 'autor', 'precio'.
2. Ordenamiento por precio (descendente)
Implementar una función llamada ordenar_por_precio_desc(libros) que reciba
la lista de libros y la ordene de mayor a menor precio usando cualquier método de
ordenamiento aprendido (por ejemplo, selección, burbuja o quicksort).
3. Búsqueda por título
Crear una función llamada buscar_por_titulo(libros, titulo_buscado) que
realice una búsqueda secuencial del libro por título (sin distinguir
mayúsculas/minúsculas). Retornar el libro si se encuentra, o un mensaje indicando
que no existe.
MODELO DE EXAMEN PARCIAL 2 - INTEGRADOR 2
4. Filtrar libros por autor
Crear una función llamada filtrar_por_autor(libros, autor_buscado) que
devuelva una nueva lista con todos los libros de ese autor (puede haber varios).
5. Guardar los libros ordenados
Crear una función llamada guardar_ordenados(libros_ordenados,
nombre_archivo) que escriba en un archivo .txt llamado ordenados.txt la lista
ordenada por precio."""

def crear_inventario_de_prueba():
    libros_prueba = [
        "L001,El principito,Antoine de Saint-Exupéry,3200",
        "L002,Cien años de soledad,Gabriel García Márquez,5900",
        "L003,Fahrenheit 451,Ray Bradbury,4100",
        "L004,Don Quijote,Miguel de Cervantes,7500",
        "L005,Rayuela,Julio Cortázar,6700"
    ]
    with open("inventario.txt", "w") as f:
        for linea in libros_prueba:
            f.write(linea + "\n")
    print("Archivo inventario.txt creado con libros de prueba.")


def leer_inventario(nombre_archivo):
    libros= []
    try:
        with open(nombre_archivo, 'r', encoding="latin-1") as archivo:
            for linea in archivo:
                partes = linea.strip().split ("|")
                if len(partes) == 4:
                    libro = {
                        "codigo": partes[0],
                        "titulo": partes[1],
                        "autor": partes[2],
                        "precio": float(partes[3])
                    }
                    libros.append(libro)
            
    except FileNotFoundError:
        print("Archivo no encontrado")
    return libros
def mostrar_inventario(inventario):
    print("\n----- Inventario -----")
    for m in inventario:
        print(f"Número de libro: {m['codigo']} | Libro: {m['titulo']} | Autor: {m['autor']} | Precio: {m['precio']}")

        
        
def ordenar_por_precio_desc(libros):
    ordenar= len(libros)
    for i in range(ordenar-1):
        precio = i
        for j in range(i + 1, ordenar):
            if libros[j]["precio"] > libros[precio]["precio"]:  # Comparación precio
                precio = j
        libros[i], libros[precio] = libros[precio], libros[i]
    print("Libros acomodados por precio")
    
def buscar_por_titulo(libros):
    opcion=input("Ingrese el libro que desee: ")
    encontrado= False
    for p in libros:
        if p["titulo"].lower()== opcion.lower():
            print(f"Orden: {p['codigo']} | Libro: {p['titulo']} | Autor: {p['autor']} | Precio {p['precio']}")
            encontrado = True
            
            break
        else:
            print("Libro no disponible")
            
def filtrar_por_autor(libros):
    autor_buscado=input("Ingrese el nombre del autor:")
    libros_filtrados= []
    for libro in libros:
        if libro["autor"].lower() == autor_buscado.lower():
            libros_filtrados.append(libro)
    if libros_filtrados:
         print("Libros del autor: ")
         for l in libros_filtrados:
             print(f"{l['codigo']} | {l['titulo']} | {l['autor']} | {l['precio']}")
    else:
        print("No se encuentran libros de ese autor")


def guardar_ordenados(libros_ordenados,nombre_archivo):
    with open(nombre_archivo, 'w', encoding="utf-8") as archivo:
        for p in libros_ordenados:
            linea = f"{p['codigo']}|{p['titulo']}|{p['autor']}|{p['precio']}\n"
            archivo.write(linea)
    print("Libros guardadas correctamente.")

def menu():
    nombre_archivo = "inventario.txt"
    libros= leer_inventario(nombre_archivo)
    while True:
        print("\n--- MENÚ ---")
        print("1. Mostrar todos los libros")
        print("2. Buscar libro por título")
        print("3. Buscar autor")
        print("4. Ordenar libros por precio")
        print("5. Guardar cambios")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_inventario(libros)
        elif opcion == "2":
            buscar_por_titulo(libros)
        elif opcion == "3":
            filtrar_por_autor(libros)
        elif opcion == "4":
            ordenar_por_precio_desc(libros)
        elif opcion == "5":
            guardar_ordenados(libros,nombre_archivo)
        elif opcion == "6":
            print("Fin del programa")
            break
        else:
            print("Opción inválida. Intente nuevamente.")
            
crear_inventario_de_prueba()

menu()
















































