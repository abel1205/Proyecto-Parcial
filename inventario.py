"Modulo de inventario y almacen para la tienda de componentes de PC"
from clases_base import Producto
from gestion_venta import GestionVenta, Venta


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
