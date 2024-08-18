

class Veterinaria:
    def __init__(self, nombre, edad, raza, peso, color):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.peso = peso
        self.color = color
        self.estado = "NO ATENDIDO"
        self.tipo = "Perro Grande" if peso >= 10 else "Perro Pequeño"

    def mostrar_informacion(self):
        print(f"\nNombre: {self.nombre}")
        print(f"Edad: {self.edad} años")
        print(f"Raza: {self.raza}")
        print(f"Peso: {self.peso} kg")
        print(f"Color: {self.color}")
        print(f"Estado: {self.estado}")
        print(f"Tipo: {self.tipo}")

    def registrar(self):
        self.estado = "ATENDIDO"
        self.mostrar_informacion()

# Solicitar datos al usuario
nombre = input("Ingrese el nombre del perro: ")
edad = int(input("Ingrese la edad del perro (en años): "))
raza = input("Ingrese la raza del perro: ")
peso = float(input("Ingrese el peso del perro (en kg): "))
color = input("Ingrese el color del perro: ")

# Crear el perro
perro = Veterinaria(nombre, edad, raza, peso, color)

# Mostrar información antes de registrar
print("\nInformación antes de registrar:")
perro.mostrar_informacion()

# Registrar y mostrar información después
print("\nInformación después de registrar:")
perro.registrar()

