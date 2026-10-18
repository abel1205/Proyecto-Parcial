"Tienda de componentes de PC"
"Este será nuestro script principal"

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