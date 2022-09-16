class Cola:
    def __init__(self):
        self.primero = None
    def estaVacia(self):
        if self.primero == None:
            return True
        else:
            return False
    def insertarCompra(self, compra):
        if self.estaVacia():
            self.primero = compra
        else:
            temp = self.primero
            while(temp.siguiente != None):
                temp = temp.siguiente
            temp.siguiente = compra
    def extraer(self):
        temp = self.primero
        if self.primero != None:
            print("Orden de " + temp.nombre + ": "+ temp.descripcion +", tiempo estimado: " + str(temp.tiempo)+" min")
            print("")
            self.primero=self.primero.siguiente
            del temp
        else:
            print("No hay ordenes pendientes")