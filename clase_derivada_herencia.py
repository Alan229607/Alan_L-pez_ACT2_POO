from Producto import Producto

class ProductoElectronico(Producto):
    def __init__(self, nombre, precio, stock, garantia_meses):
        super().__init__(nombre, precio, stock)
        self.garantia_meses = garantia_meses

    def mostrar_info(self):
        info = super().mostrar_info()
        return f"{info}, Garantía: {self.garantia_meses} meses"

class ProductoAlimento(Producto):
    def __init__(self, nombre, precio, stock, fecha_caducidad):
        super().__init__(nombre, precio, stock)
        self.fecha_caducidad = fecha_caducidad

    def mostrar_info(self):
        info = super().mostrar_info()
        return f"{info}, Caducidad: {self.fecha_caducidad}"

