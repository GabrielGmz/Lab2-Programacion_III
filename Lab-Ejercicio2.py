#PAPELERIA

class Item:
    def __init__(self, nombre, precio_compra, margen_ganancia=1.30):
        self.nombre = nombre
        self.precio_compra = precio_compra
        self.margen_ganancia = margen_ganancia

    def precio_venta(self):
        return self.precio_compra * self.margen_ganancia

    def __str__(self):
        return f"{self.nombre} - Precio de venta: ${self.precio_venta():.2f}"


class Cuaderno(Item):
    def __init__(self, tipo, precio_compra):
        nombre = f"Cuaderno HOJITAS de {tipo} hojas"
        super().__init__(nombre, precio_compra)


class Lapiz(Item):
    def __init__(self, tipo, precio_compra):
        nombre = f"Lápiz RAYAS de {tipo}"
        super().__init__(nombre, precio_compra)


# Función para ingresar los datos del artículo
def ingresar_datos_articulo():
    tipo_articulo = input("¿Desea ingresar un Cuaderno o un Lápiz? (C/L): ").strip().lower()
    if tipo_articulo == 'c':
        tipo = input("Ingrese el tipo de cuaderno (50 o 100 hojas): ").strip()
        precio_compra = float(input("Ingrese el precio de compra del cuaderno: "))
        return Cuaderno(tipo, precio_compra)
    elif tipo_articulo == 'l':
        tipo = input("Ingrese el tipo de lápiz (grafito o colores): ").strip().lower()
        precio_compra = float(input("Ingrese el precio de compra del lápiz: "))
        return Lapiz(tipo, precio_compra)
    else:
        print("Opción no válida. Intente de nuevo.")
        return ingresar_datos_articulo()


articulos = []

for i in range(2):  # Ingresar al menos dos artículos
    print(f"\nIngresando datos del artículo {i + 1}:")
    articulo = ingresar_datos_articulo()
    articulos.append(articulo)

print("\nArtículos registrados:")
for articulo in articulos:
    print(articulo)
