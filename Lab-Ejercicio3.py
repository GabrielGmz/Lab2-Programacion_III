class Auto:
    def __init__(self, tipo, precio_compra, caracteristicas):
        self.tipo = tipo  # Nacional o Importado
        self.precio_compra = precio_compra
        self.caracteristicas = caracteristicas  # Lista de 10 características
        self.ruedas = 4
        self.capacidad = 5
        self.margen_ganancia = 1.4

    def precio_venta(self):
        return self.precio_compra * self.margen_ganancia

    def __str__(self):
        return (f"Tipo: {self.tipo}\n"
                f"Precio de venta: ${self.precio_venta():.2f}\n"
                f"Ruedas: {self.ruedas}\n"
                f"Capacidad: {self.capacidad} pasajeros\n"
                f"Características: {', '.join(self.caracteristicas)}")


def ingresar_datos_auto():
    tipo = input("Ingrese el tipo de auto (Nacional o Importado): ").strip().capitalize()
    precio_compra = float(input("Ingrese el precio de compra del auto: "))
    caracteristicas = []
    print("Ingrese las 10 principales características del auto:")
    for i in range(10):
        caracteristica = input(f"Característica {i + 1}: ").strip()
        caracteristicas.append(caracteristica)

    return Auto(tipo, precio_compra, caracteristicas)


autos = []

for i in range(2):  # Ajustar la cantidad de autos que deseas ingresar
    print(f"\nIngresando datos del auto {i + 1}:")
    auto = ingresar_datos_auto()
    autos.append(auto)

print("\nAutos registrados:")
for auto in autos:
    print("\n" + str(auto))
