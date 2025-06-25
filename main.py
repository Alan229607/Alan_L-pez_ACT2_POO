from Producto import Producto

# Instanciación de objetos
producto1 = Producto("Laptop", 15000, 5)
producto2 = Producto("Mouse", 300, 20)

# Uso de métodos
print(producto1.mostrar_info())
print(producto2.mostrar_info())

# Actualizar stock
producto1.actualizar_stock(3)
producto2.actualizar_stock(-5)

# Mostrar info nuevamente
print(producto1.mostrar_info())
print(producto2.mostrar_info())
