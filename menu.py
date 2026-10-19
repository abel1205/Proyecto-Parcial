"""
Menu interactivo de la tienda de componentes de PC (con los 8 tipos de producto).

"""

# ---------------------------------------------------------------
# IMPORTACIONES: traemos las clases que ya hicieron los demas modulos
# ---------------------------------------------------------------
from clases_base import (Procesador, PlacaMadre, MemoriaRAM, TarjetaGrafica,
                         Almacenamiento, FuentePoder, Gabinete, Refrigeracion)
from gestion_venta import GestionVenta, Venta
from inventario import Inventario


# ---------------------------------------------------------------
# TIPOS DE PRODUCTO
# Tabla: nombre del tipo -> (clase, lista de datos propios del tipo).
# Cada dato es (pregunta que se muestra, tipo de dato).
# El orden es el mismo que usan los constructores de clases_base.py
# (despues de codigo, nombre, marca, precio y modelo).
# ---------------------------------------------------------------
TIPOS = {
    "Procesador": (Procesador, [
        ("Nucleos", int),
        ("Frecuencia (GHz)", float),
        ("Socket", str)]),
    "PlacaMadre": (PlacaMadre, [
        ("Socket", str),
        ("Formato (ATX/mATX)", str),
        ("Tipo de RAM (DDR4/DDR5)", str)]),
    "MemoriaRAM": (MemoriaRAM, [
        ("Capacidad (GB)", int),
        ("Velocidad (MHz)", int),
        ("Tipo (DDR4/DDR5)", str)]),
    "TarjetaGrafica": (TarjetaGrafica, [
        ("Memoria (GB)", int),
        ("Tipo de memoria (GDDR6)", str)]),
    "Almacenamiento": (Almacenamiento, [
        ("Capacidad (GB)", int),
        ("Tecnologia (SSD/HDD)", str),
        ("Interfaz (NVMe/SATA)", str)]),
    "FuentePoder": (FuentePoder, [
        ("Potencia (W)", int),
        ("Certificacion (80 Plus Bronze)", str)]),
    "Gabinete": (Gabinete, [
        ("Formato compatible (ATX/mATX)", str),
        ("Color", str)]),
    "Refrigeracion": (Refrigeracion, [
        ("Tipo (Aire/Liquida)", str),
        ("Compatibilidad (sockets)", str)]),
}


# ---------------------------------------------------------------
# FUNCIONES AUXILIARES PARA PEDIR DATOS
# Repiten la pregunta hasta que el usuario escribe algo valido,
# asi el programa no se cae por un dato mal escrito.
# ---------------------------------------------------------------
def pedir_texto(mensaje):
    """Pide un texto que no este vacio."""
    while True:
        texto = input(mensaje).strip()  # strip() quita espacios sobrantes
        if texto:
            return texto
        print("  * No puede estar vacio.")


def pedir_entero(mensaje, minimo=1, maximo=None):
    """Pide un numero entero dentro de un rango."""
    while True:
        try:
            numero = int(input(mensaje))  # falla con ValueError si no es entero
        except ValueError:
            print("  * Escribe un numero entero.")
            continue
        if numero < minimo or (maximo is not None and numero > maximo):
            print("  * Numero fuera de rango.")
            continue
        return numero


def pedir_decimal(mensaje):
    """Pide un numero con decimales mayor que cero (por ejemplo, un precio)."""
    while True:
        try:
            numero = float(input(mensaje))
        except ValueError:
            print("  * Escribe un numero (ejemplo: 150.50).")
            continue
        if numero <= 0:
            print("  * Debe ser mayor que cero.")
            continue
        return numero


def pedir_dato(pregunta, tipo_dato):
    """Pide un dato segun su tipo (int, float o str) usando las funciones de arriba."""
    if tipo_dato is int:
        return pedir_entero(pregunta + ": ")
    if tipo_dato is float:
        return pedir_decimal(pregunta + ": ")
    return pedir_texto(pregunta + ": ")


# ---------------------------------------------------------------
# DATOS DE EJEMPLO
# ---------------------------------------------------------------
def cargar_datos_ejemplo(inventario):
    """Registra ocho productos de prueba (uno de cada tipo)."""
    inventario.registrar_producto(
        Procesador("CPU001", "Ryzen 5 5600", "AMD", 650.00, "5600", 6, 3.5, "AM4"),
        cantidad=5, ubicacion="Estante A1")
    inventario.registrar_producto(
        PlacaMadre("MB001", "B550M Pro", "MSI", 480.00, "B550M", "AM4", "mATX", "DDR4"),
        cantidad=4, ubicacion="Estante A2")
    inventario.registrar_producto(
        MemoriaRAM("RAM001", "Fury 16GB", "Kingston", 180.00, "Fury", 16, 3200, "DDR4"),
        cantidad=1, ubicacion="Estante B2")  # solo 1: queda en alerta de stock bajo
    inventario.registrar_producto(
        TarjetaGrafica("GPU001", "RTX 3060", "NVIDIA", 1500.00, "3060", 12, "GDDR6"),
        cantidad=3, ubicacion="Vitrina")
    inventario.registrar_producto(
        Almacenamiento("SSD001", "SSD NVMe 1TB", "Samsung", 320.00, "980", 1000, "SSD", "NVMe"),
        cantidad=10, ubicacion="Estante A3")
    inventario.registrar_producto(
        FuentePoder("PSU001", "Fuente 650W", "Corsair", 290.00, "CV650", 650, "80 Plus Bronze"),
        cantidad=6, ubicacion="Estante C1")
    inventario.registrar_producto(
        Gabinete("CAS001", "Gabinete ATX", "Cooler Master", 260.00, "Q300L", "ATX", "Negro"),
        cantidad=3, ubicacion="Estante C2")
    inventario.registrar_producto(
        Refrigeracion("REF001", "Cooler de aire", "Cooler Master", 120.00, "Hyper 212", "Aire", "AM4/LGA1700"),
        cantidad=8, ubicacion="Estante C3")


# ---------------------------------------------------------------
# OPCIONES DEL MENU
# ---------------------------------------------------------------
def ver_inventario(inventario, gestion):
    """Opcion 1: muestra todos los productos con su stock y ubicacion."""
    print(inventario.resumen_inventario())


def registrar_producto(inventario, gestion):
    """Opcion 2: crea un producto de cualquiera de los 8 tipos y lo registra en el almacen."""
    nombres_tipos = list(TIPOS)  # el diccionario conserva el orden en que se escribio
    print("Tipos de producto:")
    for numero, nombre_tipo in enumerate(nombres_tipos, start=1):
        print(f"  {numero}) {nombre_tipo}")
    eleccion = pedir_entero("Elige el tipo: ", 1, len(nombres_tipos))
    clase, datos_del_tipo = TIPOS[nombres_tipos[eleccion - 1]]

    codigo = pedir_texto("Codigo del producto: ").upper()
    # Revisamos el codigo antes de pedir el resto de datos, para no hacer perder tiempo
    if inventario.buscar_producto(codigo) is not None:
        print(f"Ya existe el producto {codigo}.")
        return

    # Datos comunes a todos los tipos
    nombre = pedir_texto("Nombre: ")
    marca = pedir_texto("Marca: ")
    precio = pedir_decimal("Precio (S/): ")
    modelo = pedir_texto("Modelo: ")

    # Datos propios del tipo elegido: se preguntan segun la tabla TIPOS
    extras = [pedir_dato(pregunta, tipo) for pregunta, tipo in datos_del_tipo]
    producto = clase(codigo, nombre, marca, precio, modelo, *extras)

    # Datos de almacen
    cantidad = pedir_entero("Cantidad inicial: ", minimo=0)
    ubicacion = pedir_texto("Ubicacion: ")
    inventario.registrar_producto(producto, cantidad, ubicacion)
    print(f"Producto {codigo} registrado.")


def ingresar_stock(inventario, gestion):
    """Opcion 3: suma unidades a un producto que ya existe."""
    codigo = pedir_texto("Codigo del producto: ").upper()
    cantidad = pedir_entero("Unidades recibidas: ")
    inventario.ingresar_stock(codigo, cantidad)
    print(f"Stock actual de {codigo}: {inventario.consultar_stock(codigo)}")


def ver_alertas(inventario, gestion):
    """Opcion 4: lista los productos cuyo stock esta en el minimo o por debajo."""
    alertas = inventario.alertas_stock()
    if not alertas:
        print("No hay productos con stock bajo.")
        return
    print("=== STOCK BAJO ===")
    for registro in alertas:
        producto = registro.get_producto()
        print(f"{producto.get_codigo()} | {producto.get_nombre()} | "
              f"{registro.get_cantidad()} unidades (minimo {registro.get_stock_minimo()})")


def ver_especificaciones(inventario, gestion):
    """Opcion 5: muestra los datos tecnicos de un producto."""
    codigo = pedir_texto("Codigo del producto: ").upper()
    producto = inventario.buscar_producto(codigo)
    if producto is None:
        print(f"No existe el producto {codigo}.")
        return
    print(producto)  # usa el __str__ de Producto
    for clave, valor in producto.especificaciones().items():
        print(f"  {clave}: {valor}")


def nueva_venta(inventario, gestion):
    """Opcion 6: arma una venta y la registra (esto descuenta el stock)."""
    venta = Venta(pedir_texto("Codigo de la venta: ").upper(), pedir_texto("Cliente: "))

    # Agregamos productos hasta que el usuario deje el codigo vacio
    while True:
        codigo = input("Codigo del producto (Enter para terminar): ").strip().upper()
        if not codigo:
            break
        # IMPORTANTE: usamos el MISMO objeto que esta en el inventario.
        # inventario.py rechaza una venta con un producto "copiado".
        producto = inventario.buscar_producto(codigo)
        if producto is None:
            print(f"  * No existe el producto {codigo}.")
            continue
        cantidad = pedir_entero("Cantidad: ")
        venta.agregar_producto(producto, cantidad)

    if not venta.detalles:
        print("Venta cancelada: no se agrego ningun producto.")
        return

    # Valida stock, guarda la venta y descuenta unidades (todo o nada)
    inventario.registrar_venta(venta, gestion)
    print("Venta registrada:")
    print(venta.mostrar_resumen())


def listar_ventas(inventario, gestion):
    """Opcion 7: muestra todas las ventas registradas."""
    gestion.listar_ventas()


# ---------------------------------------------------------------
# MENU PRINCIPAL
# ---------------------------------------------------------------

OPCIONES = {
    1: ("Ver inventario", ver_inventario),
    2: ("Registrar producto", registrar_producto),
    3: ("Ingresar stock", ingresar_stock),
    4: ("Alertas de stock bajo", ver_alertas),
    5: ("Ver especificaciones de un producto", ver_especificaciones),
    6: ("Nueva venta", nueva_venta),
    7: ("Listar ventas", listar_ventas),
}


def mostrar_menu():
    """Imprime las opciones disponibles."""
    print("\n===== TIENDA DE COMPONENTES DE PC =====")
    for numero, (texto, _funcion) in OPCIONES.items():
        print(f"{numero}. {texto}")
    print("0. Salir")


def main():
    """Crea los objetos principales y repite el menu hasta que el usuario salga."""
    inventario = Inventario()
    gestion = GestionVenta()
    cargar_datos_ejemplo(inventario)

    while True:
        mostrar_menu()
        opcion = pedir_entero("Elige una opcion: ", minimo=0, maximo=len(OPCIONES))
        if opcion == 0:
            print("Hasta luego.")
            break

        _texto, funcion = OPCIONES[opcion]
        # Los modulos avisan los errores con excepciones (stock insuficiente,
        # codigo repetido, etc.). Las atrapamos aqui para mostrar el mensaje
        # y volver al menu en lugar de cerrar el programa.
        try:
            funcion(inventario, gestion)
        except (ValueError, TypeError) as error:
            print(f"Error: {error}")


# Solo ejecuta el menu si corremos este archivo directamente (python menu_sin_guardar.py)
if __name__ == "__main__":
    main()
