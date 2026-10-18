
"""
Modulo de gestion de ventas para una tienda de componentes de PC.
"""

from clases_base import Producto


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
