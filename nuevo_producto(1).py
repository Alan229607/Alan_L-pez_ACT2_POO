class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def mostrar_info(self):
        return f"Producto: {self.nombre}, Precio: ${self.precio}, Stock: {self.stock} unidades"

    def actualizar_stock(self, cantidad):
        self.stock += cantidad
        print(f"El stock de {self.nombre} ha sido actualizado a {self.stock} unidades.")
