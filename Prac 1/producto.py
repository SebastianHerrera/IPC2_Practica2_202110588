class Producto:
    def __init__(self, nombre, descripcion, tiempo):
        self.nombre = nombre
        self.descripcion = descripcion
        self.tiempo = tiempo
        self.siguiente = None
        self.anterior = None