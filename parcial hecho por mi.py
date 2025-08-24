"""1. Registrar mascota (nombre, especie, edad) en una lista.
2. Mostrar todas las mascotas registradas.
3. Buscar una mascota por nombre (usando un ciclo y condicional).
4. Agregar un turno a la cola de espera (usando la estructura de Cola vista en clase).
5. Atender un turno (desencolar una mascota).
6. Mostrar mascotas en espera.
7. Salir del sistema.
Requisitos técnicos del programa:
• Usar mínimo 2 funciones distintas.
• Manejar excepciones simples (por ejemplo, si buscan una mascota que no está en la
lista).
• Utilizar listas para guardar los datos de mascotas.
• Utilizar la estructura Cola (puede estar definida como clase o lista con append y
pop(0)) para los turnos. """


class Mascota:
    
    def __init__ (self, nombre,edad,especie):
        self.nombre= nombre
        self.edad=edad
        self.especie= especie
        
def registrar_mascotas():
    nombre=input("Ingrese el nombre de la mascota: ")
    especimen=input("Ingrese la especie de la mascota: ")
    try:
        time=int(input("Ingrese la edad de la mascota: "))
        mas= Mascota(nombre, especimen, time)
        lista_mascotas.append(mas)
        print(f"{nombre} fue registrada correctamente.")
    except ValueError:
        print("Ingrese una edad correcta")
        
def agregar_turno(cola):
    nombre = input("Nombre de la mascota a agregar al turno: ")
    for m in lista_mascotas:
        if m.nombre.lower() == nombre.lower():
            cola.encolar(m)
            print(f"{m.nombre} fue agregada a la cola de espera.")
            return
    print("Mascota no registrada.")
def mostrar_espera(cola):
    if not cola.items:
        print("No hay mascotas en espera.")
    else:
        print("Mascotas en espera:")
        for m in cola.items:
            print(f"{m.nombre} ({m.edad}, {m.especie} años )")
def buscar_mascota():
    nombre = input("Ingrese el nombre a buscar: ")
    encontrado = False
    for m in lista_mascotas:
        if m.nombre.lower() == nombre.lower():
            print(f"Encontrada: Nombre: {m.nombre}, Edad: {m.edad}, Especie: {m.especie}")
            encontrado = True
            break
    if not encontrado:
        print("Mascota no encontrada.")
def mostrar_mascotas():
    if not lista_mascotas:
        print("No hay mascotas registradas.")
    else:
        for m in lista_mascotas:
            print(f"Nombre: {m.nombre}, Edad: {m.edad}, Especie: {m.especie}")

   
lista_mascotas=[]
fila=[]
cola=[]

class Cola:
    def __init__ (self):
        self.items=[]
    
    def encolar(self,mascota):
        self.items.append(mascota)
    def desencolar (self):
        if self.items:
            atendido=self.items.pop(0)
            print(f"La mascota {atendido} fue atendido")
            return atendido
        else:
            print("No hay mascotas por atender")
            return None


cola_espera = Cola()

while True:
    print("""
1. Registrar mascota
2. Mostrar todas las mascotas
3. Buscar mascota por nombre
4. Agregar turno
5. Atender turno
6. Mostrar mascotas en espera
7. Salir
""")
    opcion = input("Elija una opción: ")
    
    if opcion == "1":
        registrar_mascotas()
    elif opcion == "2":
        mostrar_mascotas()
    elif opcion == "3":
        buscar_mascota()
    elif opcion == "4":
        agregar_turno(cola_espera)
    elif opcion == "5":
        cola_espera.desencolar()
    elif opcion == "6":
        mostrar_espera(cola_espera)
    elif opcion == "7":
        print("Fin del sistema.")
        break
    else:
        print("Opción inválida.")
    
    
    
        
        
        































