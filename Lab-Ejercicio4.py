class DispositivoElectronico:
    def __init__(self, tipo, precio_compra, caracteristicas):
        self.tipo = tipo  # Celular, Tablet o Portátil
        self.precio_compra = precio_compra
        self.caracteristicas = caracteristicas  # Lista de 6 características
        self.marca = "PHR"  # Marca fija
        self.margen_ganancia = 1.7  # Todos son importados

    def precio_venta(self):
        return self.precio_compra * self.margen_ganancia

    def __str__(self):
        return (f"Tipo: {self.tipo}\n"
                f"Marca: {self.marca}\n"
                f"Precio de venta: ${self.precio_venta():.2f}\n"
                f"Características: {', '.join(self.caracteristicas)}")


def ingresar_datos_dispositivo():
    tipo = input("Ingrese el tipo de dispositivo (Celular, Tablet, Portátil): ").strip().capitalize()
    precio_compra = float(input("Ingrese el precio de compra del dispositivo: "))
    caracteristicas = []
    print("Ingrese las 6 principales características del dispositivo:")
    for i in range(6):
        caracteristica = input(f"Característica {i + 1}: ").strip()
        caracteristicas.append(caracteristica)

    return DispositivoElectronico(tipo, precio_compra, caracteristicas)

dispositivos = []

for i in range(2):  # Ajustar la cantidad de dispositivos que deseas ingresar
    print(f"\nIngresando datos del dispositivo {i + 1}:")
    dispositivo = ingresar_datos_dispositivo()
    dispositivos.append(dispositivo)

print("\nDispositivos registrados:")
for dispositivo in dispositivos:
    print("\n" + str(dispositivo))

