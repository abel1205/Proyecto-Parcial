"Tienda de componentes de PC"
"Este será nuestro script principal"


##########################################################
##################### clases_base.py #####################
##########################################################


'''
Simulación de productos para una tienda de componentes de PC.
'''


class Producto:
    def __init__(self, codigo, nombre, marca, precio, descripcion=""):
        self.codigo = codigo
        self.nombre = nombre
        self.marca = marca
        self.precio = precio
        self.descripcion = descripcion

    def get_codigo(self):
        return self.codigo
    def set_codigo(self, valor):
        self.codigo = valor
    def get_nombre(self):
        return self.nombre
    def set_nombre(self, valor):
        self.nombre = valor
    def get_marca(self):
        return self.marca
    def set_marca(self, valor):
        self.marca = valor
    def get_precio(self):
        return self.precio
    def set_precio(self, valor):
        self.precio = valor
    def get_descripcion(self):
        return self.descripcion
    def set_descripcion(self, valor):
        self.descripcion = valor

    def especificaciones(self):
        return {}
    def __str__(self):
        return f"{self.get_codigo()} - {self.get_nombre()} ({self.__class__.__name__}) - S/ {self.get_precio():.2f}"


class Componente(Producto):
    def __init__(self, codigo, nombre, marca, precio, modelo, descripcion=""):
        Producto.__init__(self, codigo, nombre, marca, precio, descripcion)
        self.modelo = modelo

    def get_modelo(self):
        return self.modelo
    def set_modelo(self, valor):
        self.modelo = valor

class Procesador(Componente):
    def __init__(self, codigo, nombre, marca, precio, modelo, nucleos,
                 frecuencia_ghz, socket, descripcion=""):
        Componente.__init__(self, codigo, nombre, marca, precio, modelo, descripcion)
        self.nucleos = nucleos
        self.frecuencia_ghz = frecuencia_ghz
        self.socket = socket

    def get_nucleos(self):
        return self.nucleos
    def set_nucleos(self, valor):
        self.nucleos = valor
    def get_frecuencia_ghz(self):
        return self.frecuencia_ghz
    def set_frecuencia_ghz(self, valor):
        self.frecuencia_ghz = valor
    def get_socket(self):
        return self.socket
    def set_socket(self, valor):
        self.socket = valor

    def especificaciones(self):
        return {"Modelo": self.get_modelo(), "Núcleos": self.get_nucleos(),
                "Frecuencia": f"{self.get_frecuencia_ghz()} GHz", "Socket": self.get_socket()}


class PlacaMadre(Componente):
    def __init__(self, codigo, nombre, marca, precio, modelo, socket,
                 formato, tipo_ram, descripcion=""):
        Componente.__init__(self, codigo, nombre, marca, precio, modelo, descripcion)
        self.socket = socket
        self.formato = formato
        self.tipo_ram = tipo_ram

    def get_socket(self):
        return self.socket
    def set_socket(self, valor):
        self.socket = valor
    def get_formato(self):
        return self.formato
    def set_formato(self, valor):
        self.formato = valor
    def get_tipo_ram(self):
        return self.tipo_ram
    def set_tipo_ram(self, valor):
        self.tipo_ram = valor
        
    def especificaciones(self):
        return {"Modelo": self.get_modelo(), "Socket": self.get_socket(),
                "Formato": self.get_formato(), "Tipo de RAM": self.get_tipo_ram()}


class MemoriaRAM(Componente):
    def __init__(self, codigo, nombre, marca, precio, modelo, capacidad_gb,
                 velocidad_mhz, tipo, descripcion=""):
        Componente.__init__(self, codigo, nombre, marca, precio, modelo, descripcion)
        self.capacidad_gb = capacidad_gb
        self.velocidad_mhz = velocidad_mhz
        self.tipo = tipo

    def get_capacidad_gb(self):
        return self.capacidad_gb
    def set_capacidad_gb(self, valor):
        self.capacidad_gb = valor
    def get_velocidad_mhz(self):
        return self.velocidad_mhz
    def set_velocidad_mhz(self, valor):
        self.velocidad_mhz = valor
    def get_tipo(self):
        return self.tipo
    def set_tipo(self, valor):
        self.tipo = valor

    def especificaciones(self):
        return {"Modelo": self.get_modelo(), "Capacidad": f"{self.get_capacidad_gb()} GB",
                "Velocidad": f"{self.get_velocidad_mhz()} MHz", "Tipo": self.get_tipo()}


class TarjetaGrafica(Componente):
    def __init__(self, codigo, nombre, marca, precio, modelo, memoria_gb,
                 tipo_memoria, descripcion=""):
        Componente.__init__(self, codigo, nombre, marca, precio, modelo, descripcion)
        self.memoria_gb = memoria_gb
        self.tipo_memoria = tipo_memoria

    def get_memoria_gb(self):
        return self.memoria_gb
    def set_memoria_gb(self, valor):
        self.memoria_gb = valor
    def get_tipo_memoria(self):
        return self.tipo_memoria
    def set_tipo_memoria(self, valor):
        self.tipo_memoria = valor

    def especificaciones(self):
        return {"Modelo": self.get_modelo(), "Memoria gráfica": f"{self.get_memoria_gb()} GB",
                "Tipo de memoria": self.get_tipo_memoria()}
        

class Almacenamiento(Componente):
    def __init__(self, codigo, nombre, marca, precio, modelo, capacidad_gb,
                 tecnologia, interfaz, descripcion=""):
        Componente.__init__(self, codigo, nombre, marca, precio, modelo, descripcion)
        self.capacidad_gb = capacidad_gb
        self.tecnologia = tecnologia
        self.interfaz = interfaz

    def get_capacidad_gb(self):
        return self.capacidad_gb
    def set_capacidad_gb(self, valor):
        self.capacidad_gb = valor
    def get_tecnologia(self):
        return self.tecnologia
    def set_tecnologia(self, valor):
        self.tecnologia = valor
    def get_interfaz(self):
        return self.interfaz
    def set_interfaz(self, valor):
        self.interfaz = valor
        
    def especificaciones(self):
        return {"Modelo": self.get_modelo(), "Capacidad": f"{self.get_capacidad_gb()} GB",
                "Tecnología": self.get_tecnologia(), "Interfaz": self.get_interfaz()}


class FuentePoder(Componente):
    def __init__(self, codigo, nombre, marca, precio, modelo, potencia_w,
                 certificacion, descripcion=""):
        Componente.__init__(self, codigo, nombre, marca, precio, modelo, descripcion)
        self.potencia_w = potencia_w
        self.certificacion = certificacion

    def get_potencia_w(self):
        return self.potencia_w
    def set_potencia_w(self, valor):
        self.potencia_w = valor
    def get_certificacion(self):
        return self.certificacion
    def set_certificacion(self, valor):
        self.certificacion = valor
        
    def especificaciones(self):
        return {"Modelo": self.get_modelo(), "Potencia": f"{self.get_potencia_w()} W",
                "Certificación": self.get_certificacion()}


class Gabinete(Componente):
    def __init__(self, codigo, nombre, marca, precio, modelo, formato,
                 color, descripcion=""):
        Componente.__init__(self, codigo, nombre, marca, precio, modelo, descripcion)
        self.formato = formato
        self.color = color

    def get_formato(self):
        return self.formato
    def set_formato(self, valor):
        self.formato = valor
    def get_color(self):
        return self.color
    def set_color(self, valor):
        self.color = valor

    def especificaciones(self):
        return {"Modelo": self.get_modelo(), "Formato compatible": self.get_formato(),
                "Color": self.get_color()}


class Refrigeracion(Componente):
    def __init__(self, codigo, nombre, marca, precio, modelo, tipo,
                 compatibilidad, descripcion=""):
        Componente.__init__(self, codigo, nombre, marca, precio, modelo, descripcion)
        self.tipo = tipo
        self.compatibilidad = compatibilidad

    def get_tipo(self):
        return self.tipo
    def set_tipo(self, valor):
        self.tipo = valor
    def get_compatibilidad(self):
        return self.compatibilidad
    def set_compatibilidad(self, valor):
        self.compatibilidad = valor

    def especificaciones(self):
        return {"Modelo": self.get_modelo(), "Tipo": self.get_tipo(),
                "Compatibilidad": self.get_compatibilidad()}


__all__ = ["Producto", "Componente", "Procesador", "PlacaMadre", "MemoriaRAM",
    "TarjetaGrafica", "Almacenamiento", "FuentePoder", "Gabinete",
    "Refrigeracion"
    ]


#########################################################
##################### inventario.py #####################
#########################################################


"Modulo de inventario y almacen para la tienda de componentes de PC"

# from clases_base import Producto
# from gestion_venta import GestionVenta, Venta

def validar_cantidad(cantidad, permitir_cero=False): # Evita cantidades negativas, decimales o booleanas
    if type(cantidad) is not int or cantidad < (0 if permitir_cero else 1):
        limite = "no negativo" if permitir_cero else "positivo"
        raise ValueError(f"La cantidad debe ser un entero {limite}.")


class RegistroStock: # Asocia un Producto con su cantidad, ubicacion y stock minimo
    def __init__(self, producto, cantidad=0, ubicacion= "Sin asignar", stock_minimo=2):
        if not isinstance(producto, Producto):
            raise TypeError("Se necesita un Producto de clases_base.py.")
        validar_cantidad(cantidad, permitir_cero=True)
        validar_cantidad(stock_minimo, permitir_cero=True)
        if not isinstance(ubicacion, str) or not ubicacion.strip():
            raise ValueError("La ubicacion debe ser un texto no vacio.")
        self.__producto = producto
        self.__cantidad = cantidad
        self.__ubicacion = ubicacion.strip()
        self.__stock_minimo = stock_minimo

    def get_producto(self):
        return self.__producto

    def get_cantidad(self):
        return self.__cantidad

    def get_ubicacion(self):
        return self.__ubicacion

    def get_stock_minimo(self):
        return self.__stock_minimo

    def set_ubicacion(self, ubicacion):
        if not isinstance(ubicacion, str) or not ubicacion.strip():
            raise ValueError("La ubicacion debe ser un texto no vacio.")
        self.__ubicacion = ubicacion.strip()

    def set_stock_minimo(self, stock_minimo):
        validar_cantidad(stock_minimo, permitir_cero=True)
        self.__stock_minimo = stock_minimo

    def ingresar(self, cantidad): # Suma unidades recibidas en almacen
        validar_cantidad(cantidad)
        self.__cantidad += cantidad

    def retirar(self, cantidad): # Resta unidades solo si existen suficientes
        validar_cantidad(cantidad)
        if cantidad > self.__cantidad:
            raise ValueError(
                f"Stock insuficiente de {self.__producto.get_nombre()}: "
                f"disponibles {self.__cantidad}, solicitadas {cantidad}."
            )
        self.__cantidad -= cantidad

    def esta_bajo_minimo(self):
        return self.__cantidad <= self.__stock_minimo


class Almacen: # Guarda registros de stock identificados por el codigo del producto
    def __init__(self, nombre="Almacen principal"):
        self.__nombre = nombre
        self.__registros = {}  # codigo -> RegistroStock

    def registrar_producto(self, producto, cantidad=0, ubicacion="Sin asignar", stock_minimo=2): # Crea un registro de stock sin duplicar el codigo del producto
        if not isinstance(producto, Producto):
            raise TypeError("El elemento registrado debe ser un Producto.")
        codigo = producto.get_codigo()
        if codigo in self.__registros:
            raise ValueError(f"El producto {codigo} ya esta registrado.")
        self.__registros[codigo] = RegistroStock(producto, cantidad, ubicacion, stock_minimo)

    def buscar_registro(self, codigo): #  Devuelve un RegistroStock, o None si no esta registrado
        return self.__registros.get(codigo)

    def obtener_registro(self, codigo): # Busca un registro; genera error si no existe
        registro = self.buscar_registro(codigo)
        if registro is None:
            raise ValueError(f"No existe el producto {codigo} en el almacen.")
        return registro

    def ingresar(self, codigo, cantidad):
        self.obtener_registro(codigo).ingresar(cantidad)

    def retirar(self, codigo, cantidad):
        self.obtener_registro(codigo).retirar(cantidad)

    def cambiar_ubicacion(self, codigo, ubicacion):
        self.obtener_registro(codigo).set_ubicacion(ubicacion)

    def listar_registros(self): # Devuelve los registros ordenados por codigo, para mostrarlos en el menu
        return [self.__registros[codigo] for codigo in sorted(self.__registros)]

    def productos_bajo_stock(self):
        return [r for r in self.listar_registros() if r.esta_bajo_minimo()]


class Inventario: # Coordina operaciones de almacen y verifica existencias antes de vender
    def __init__(self, almacen=None):
        if almacen is not None and not isinstance(almacen, Almacen):
            raise TypeError("El inventario necesita un objeto Almacen.")
        self.__almacen = almacen if almacen is not None else Almacen()

    def registrar_producto(self, producto, cantidad=0, ubicacion="Sin asignar", stock_minimo=2):
        self.__almacen.registrar_producto(producto, cantidad, ubicacion, stock_minimo)

    def buscar_producto(self, codigo):
        registro = self.__almacen.buscar_registro(codigo)
        return registro.get_producto() if registro is not None else None

    def consultar_stock(self, codigo):
        return self.__almacen.obtener_registro(codigo).get_cantidad()

    def ingresar_stock(self, codigo, cantidad):
        self.__almacen.ingresar(codigo, cantidad)

    def retirar_stock(self, codigo, cantidad):
        self.__almacen.retirar(codigo, cantidad)

    def cambiar_ubicacion(self, codigo, ubicacion):
        self.__almacen.cambiar_ubicacion(codigo, ubicacion)

    def listar_productos(self): # Entrega registros para que el menu de Flavio los muestre como prefiera
        return self.__almacen.listar_registros()

    def alertas_stock(self):
        return self.__almacen.productos_bajo_stock()

    def _cantidades_de_venta(self, venta): # Suma cantidades por codigo (incluye productos repetidos en una venta)
        if not isinstance(venta, Venta):
            raise TypeError("Se necesita un objeto Venta de gestion_venta.py.")
        if not venta.detalles:
            raise ValueError("No se puede procesar una venta sin productos.")
        cantidades = {}
        for detalle in venta.detalles:
            codigo = detalle.producto.get_codigo()
            # Valida que el producto de Venta sea el mismo objeto registrado.
            # Asi no se acepta otro articulo distinto que reutilice un codigo.
            producto_registrado = self.buscar_producto(codigo)
            if producto_registrado is None:
                raise ValueError(f"El producto {codigo} no existe en el inventario.")
            if producto_registrado is not detalle.producto:
                raise ValueError(f"La venta usa un producto diferente para el codigo {codigo}.")
            validar_cantidad(detalle.cantidad)
            cantidades[codigo] = cantidades.get(codigo, 0) + detalle.cantidad
        return cantidades

    def verificar_venta(self, venta): # Comprueba todas las existencias ANTES de modificar el stock
        cantidades = self._cantidades_de_venta(venta)
        for codigo, cantidad in cantidades.items():
            disponibles = self.consultar_stock(codigo)
            if cantidad > disponibles:
                raise ValueError(
                    f"Stock insuficiente para {codigo}: "
                    f"disponibles {disponibles}, solicitadas {cantidad}."
                )
        return cantidades

    def registrar_venta(self, venta, gestion_ventas): #  """Integra ventas e inventario: valida, registra venta y descuenta stock. 
        # La prueba con los archivos del equipo es de un solo usuario (sin concurrencia) La gestion de ventas existente se encarga de rechazar codigos de venta duplicados.
        if not isinstance(gestion_ventas, GestionVenta):
            raise TypeError("Se necesita un objeto GestionVenta de gestion_venta.py.")
        cantidades = self.verificar_venta(venta)
        # Si el codigo de venta ya existe, registrar_venta genera un error
        # y el stock permanece intacto.
        gestion_ventas.registrar_venta(venta)
        for codigo, cantidad in cantidades.items():
            self.retirar_stock(codigo, cantidad)

    def resumen_inventario(self): # Devuelve texto para usar en consola; el menu puede usar listar_productos
        lineas = ["=== INVENTARIO DE COMPONENTES ==="]
        for registro in self.listar_productos():
            producto = registro.get_producto()
            lineas.append(
                f"{producto.get_codigo()} | {producto.get_nombre()} | "
                f"{registro.get_cantidad()} unidades | {registro.get_ubicacion()}"
            )
        if not self.listar_productos():
            lineas.append("No hay productos registrados.")
        return "\n".join(lineas)


############################################################
##################### gestion_venta.py #####################
############################################################


"""
Modulo de gestion de ventas para una tienda de componentes de PC.
"""

# from clases_base import Producto

class DetalleVenta:
    """Representa un producto incluido en una venta."""

    def __init__(self, producto, cantidad):
        if not isinstance(producto, Producto):
            raise TypeError("El producto no es valido.")
        if not isinstance(cantidad, int) or cantidad <= 0:
            raise ValueError("La cantidad debe ser un entero positivo.")

        self.producto = producto
        self.cantidad = cantidad

    def calcular_subtotal(self):
        """Calcula el precio por la cantidad de unidades."""
        return self.producto.get_precio() * self.cantidad


class Venta:
    """Almacena los detalles y calcula el total de una venta."""

    def __init__(self, codigo, cliente):
        self.codigo = codigo
        self.cliente = cliente
        self.detalles = []

    def agregar_producto(self, producto, cantidad):
        """Agrega un producto a la venta."""
        detalle = DetalleVenta(producto, cantidad)
        self.detalles.append(detalle)

    def calcular_total(self):
        """Suma los subtotales de todos los productos."""
        total = 0

        for detalle in self.detalles:
            total = total + detalle.calcular_subtotal()

        return total

    def mostrar_resumen(self):
        """Devuelve un resumen de la venta."""
        lineas = [f"Venta: {self.codigo}",
            f"Cliente: {self.cliente}",
            "Productos:"]

        for detalle in self.detalles:
            producto = detalle.producto
            subtotal = detalle.calcular_subtotal()
            lineas.append(
                f"- {producto.get_nombre()} x {detalle.cantidad}: "
                f"S/ {subtotal:.2f}")

        lineas.append(f"TOTAL: S/ {self.calcular_total():.2f}")
        return "\n".join(lineas)


class GestionVenta:
    """Administra el registro y la consulta de ventas."""

    def __init__(self):
        self.ventas = []

    def registrar_venta(self, venta):
        """Registra una venta con un codigo unico."""
        if any(v.codigo == venta.codigo for v in self.ventas):
            raise ValueError("Ya existe una venta con ese codigo.")
        self.ventas.append(venta)

    def buscar_venta(self, codigo):
        """Busca una venta por su codigo."""
        for venta in self.ventas:
            if venta.codigo == codigo:
                return venta
        return None

    def listar_ventas(self):
        """Muestra todas las ventas registradas."""
        if not self.ventas:
            print("No hay ventas registradas.")
            return

        for venta in self.ventas:
            print(venta.mostrar_resumen())
            print("-" * 30)


if __name__ == "__main__":
    # Prueba de funcionamiento del modulo.
    producto1 = Producto(
        "P001", "Mouse gamer", "Logitech", 80.00)
    producto2 = Producto(
        "P002", "Teclado mecanico", "Redragon", 150.00)

    venta1 = Venta("V001", "Cliente de prueba")
    venta1.agregar_producto(producto1, 2)
    venta1.agregar_producto(producto2, 1)

    gestion = GestionVenta()
    gestion.registrar_venta(venta1)

    print("=== SISTEMA DE GESTION DE VENTAS ===")
    print(venta1.mostrar_resumen())
    print("\n=== CONSULTA DE VENTAS ===")
    gestion.listar_ventas()


####################################################################################################
######################################### gestion_venta.py #########################################
####################################################################################################


"""
Menu interactivo de la tienda de componentes de PC.

"""

# ---------------------------------------------------------------
# IMPORTACIONES
# ---------------------------------------------------------------
#from clases_base import (Procesador, PlacaMadre, MemoriaRAM, TarjetaGrafica,
#                         Almacenamiento, FuentePoder, Gabinete, Refrigeracion)
#from gestion_venta import GestionVenta, Venta
#from inventario import Inventario


# ---------------------------------------------------------------
# TIPOS DE PRODUCTO
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










