"Tienda de componentes de PC"
"Este será nuestro script principal"

class Producto:
    def __init__(self, codigo, nombre, marca, precio, descripcion=""):
        self.codigo = codigo
        self.nombre = nombre
        self.marca = marca
        self.precio = precio
        self.descripcion = descripcion

    def especificaciones(self):
        return {}

    def __str__(self):
        return f"{self.codigo} - {self.nombre} ({self.__class__.__name__}) - S/ {self.precio:.2f}"


class Componente(Producto):
    def __init__(self, codigo, nombre, marca, precio, modelo, descripcion=""):
        Producto.__init__(self, codigo, nombre, marca, precio, descripcion)
        self.modelo = modelo


class Procesador(Componente):
    def __init__(self, codigo, nombre, marca, precio, modelo, nucleos,
                 frecuencia_ghz, socket, descripcion=""):
        Componente.__init__(self, codigo, nombre, marca, precio, modelo, descripcion)
        self.nucleos = nucleos
        self.frecuencia_ghz = frecuencia_ghz
        self.socket = socket

    def especificaciones(self):
        return {"Modelo": self.modelo, "Núcleos": self.nucleos,
                "Frecuencia": f"{self.frecuencia_ghz} GHz", "Socket": self.socket}


class PlacaMadre(Componente):
    def __init__(self, codigo, nombre, marca, precio, modelo, socket,
                 formato, tipo_ram, descripcion=""):
        Componente.__init__(self, codigo, nombre, marca, precio, modelo, descripcion)
        self.socket = socket
        self.formato = formato
        self.tipo_ram = tipo_ram

    def especificaciones(self):
        return {"Modelo": self.modelo, "Socket": self.socket,
                "Formato": self.formato, "Tipo de RAM": self.tipo_ram}


class MemoriaRAM(Componente):
    def __init__(self, codigo, nombre, marca, precio, modelo, capacidad_gb,
                 velocidad_mhz, tipo, descripcion=""):
        Componente.__init__(self, codigo, nombre, marca, precio, modelo, descripcion)
        self.capacidad_gb = capacidad_gb
        self.velocidad_mhz = velocidad_mhz
        self.tipo = tipo

    def especificaciones(self):
        return {"Modelo": self.modelo, "Capacidad": f"{self.capacidad_gb} GB",
                "Velocidad": f"{self.velocidad_mhz} MHz", "Tipo": self.tipo}


class TarjetaGrafica(Componente):
    def __init__(self, codigo, nombre, marca, precio, modelo, memoria_gb,
                 tipo_memoria, descripcion=""):
        Componente.__init__(self, codigo, nombre, marca, precio, modelo, descripcion)
        self.memoria_gb = memoria_gb
        self.tipo_memoria = tipo_memoria

    def especificaciones(self):
        return {"Modelo": self.modelo, "Memoria gráfica": f"{self.memoria_gb} GB",
                "Tipo de memoria": self.tipo_memoria}


class Almacenamiento(Componente):
    def __init__(self, codigo, nombre, marca, precio, modelo, capacidad_gb,
                 tecnologia, interfaz, descripcion=""):
        Componente.__init__(self, codigo, nombre, marca, precio, modelo, descripcion)
        self.capacidad_gb = capacidad_gb
        self.tecnologia = tecnologia
        self.interfaz = interfaz

    def especificaciones(self):
        return {"Modelo": self.modelo, "Capacidad": f"{self.capacidad_gb} GB",
                "Tecnología": self.tecnologia, "Interfaz": self.interfaz}


class FuentePoder(Componente):
    def __init__(self, codigo, nombre, marca, precio, modelo, potencia_w,
                 certificacion, descripcion=""):
        Componente.__init__(self, codigo, nombre, marca, precio, modelo, descripcion)
        self.potencia_w = potencia_w
        self.certificacion = certificacion

    def especificaciones(self):
        return {"Modelo": self.modelo, "Potencia": f"{self.potencia_w} W",
                "Certificación": self.certificacion}


class Gabinete(Componente):
    def __init__(self, codigo, nombre, marca, precio, modelo, formato,
                 color, descripcion=""):
        Componente.__init__(self, codigo, nombre, marca, precio, modelo, descripcion)
        self.formato = formato
        self.color = color

    def especificaciones(self):
        return {"Modelo": self.modelo, "Formato compatible": self.formato,
                "Color": self.color}


class Refrigeracion(Componente):
    def __init__(self, codigo, nombre, marca, precio, modelo, tipo,
                 compatibilidad, descripcion=""):
        Componente.__init__(self, codigo, nombre, marca, precio, modelo, descripcion)
        self.tipo = tipo
        self.compatibilidad = compatibilidad

    def especificaciones(self):
        return {"Modelo": self.modelo, "Tipo": self.tipo,
                "Compatibilidad": self.compatibilidad}


__all__ = ["Producto", "Componente", "Procesador", "PlacaMadre", "MemoriaRAM",
    "TarjetaGrafica", "Almacenamiento", "FuentePoder", "Gabinete",
    "Refrigeracion"
    ]