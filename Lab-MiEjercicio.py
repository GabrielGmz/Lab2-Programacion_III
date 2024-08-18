"""
Diseñar un ejercicio que aplique los principios de la Programación
Orientada a Objetos (POO), con su respectiva implementación e
instanciación. El ejercicio debe permitir la entrada de datos por
teclado. Además, proporciona una explicación detallada sobre qué
hace el programa y qué problema resuelve, basado en una situación
problemática de tu entorno

"""

from datetime import datetime

class Medicamento:
    def __init__(self, nombre, precio, cantidad, fecha_caducidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.fecha_caducidad = datetime.strptime(fecha_caducidad, "%d/%m/%Y")

    def actualizar_cantidad(self, cantidad):
        self.cantidad += cantidad

    def esta_caducado(self):
        return datetime.now() > self.fecha_caducidad

class Inventario:
    def __init__(self):
        self.medicamentos = []

    def agregar_medicamento(self, medicamento):
        self.medicamentos.append(medicamento)

    def actualizar_inventario(self, nombre, cantidad):
        for medicamento in self.medicamentos:
            if medicamento.nombre == nombre:
                medicamento.actualizar_cantidad(cantidad)
                print(f"Inventario actualizado: {nombre} ahora tiene {medicamento.cantidad} unidades.")
                return
        print(f"Medicamento {nombre} no encontrado en el inventario.")

    def verificar_disponibilidad(self, nombre):
        for medicamento in self.medicamentos:
            if medicamento.nombre == nombre:
                if medicamento.esta_caducado():
                    print(f"El medicamento {nombre} está caducado.")
                else:
                    print(f"El medicamento {nombre} tiene {medicamento.cantidad} unidades disponibles.")
                return
        print(f"Medicamento {nombre} no encontrado en el inventario.")

    def mostrar_inventario(self):
        print("\nInventario de Medicamentos:")
        for medicamento in self.medicamentos:
            estado = "Caducado" if medicamento.esta_caducado() else "Vigente"
            print(f"{medicamento.nombre}: {medicamento.cantidad} unidades, {estado}, Fecha de Caducidad: {medicamento.fecha_caducidad.strftime('%d/%m/%Y')}")


# Crear el inventario y agregar medicamentos
inventario = Inventario()

# Actualizar inventario ingresando datos por teclado
while True:
    print("\nSeleccione una acción:")
    print("1. Agregar medicamento")
    print("2. Actualizar inventario")
    print("3. Verificar disponibilidad de un medicamento")
    print("4. Mostrar inventario")
    print("5. Salir")
    
    opcion = input("Ingrese el número de la acción que desea realizar: ")
    
    if opcion == '5':
        break
    elif opcion == '1':
        nombre = input("Nombre del medicamento: ")
        precio = float(input("Precio del medicamento: "))
        cantidad = int(input("Cantidad: "))
        fecha_caducidad = input("Fecha de caducidad (dd/mm/yyyy): ")
        inventario.agregar_medicamento(Medicamento(nombre, precio, cantidad, fecha_caducidad))
    elif opcion == '2':
        nombre = input("Nombre del medicamento: ")
        cantidad = int(input("Cantidad a agregar o restar (use valores negativos para restar): "))
        inventario.actualizar_inventario(nombre, cantidad)
    elif opcion == '3':
        nombre = input("Nombre del medicamento: ")
        inventario.verificar_disponibilidad(nombre)
    elif opcion == '4':
        inventario.mostrar_inventario()
    else:
        print("Opción no válida. Por favor, ingrese un número entre 1 y 5.")

        # EXPLICACION
        """
        Este programa soluciona el problema de mantener el control de los medicamentos en casa. Te ayuda a saber cuántos medicamentos
        tienes, si están caducados o no, y cuándo necesitas comprar más. Así, evitas quedarte sin medicamentos importantes o usar
        alguno que ya no sea seguro.

        """
