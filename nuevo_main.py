from ProductosDerivados import ProductoElectronico, ProductoAlimento

# Instanciación de subclases
laptop = ProductoElectronico("Laptop", 15000, 5, 24)
pan = ProductoAlimento("Pan Integral", 35, 30, "2025-08-01")

# Mostrar información de los productos
print(laptop.mostrar_info())
print(pan.mostrar_info())

# Actualizar stock
laptop.actualizar_stock(3)
pan.actualizar_stock(-5)

# Mostrar información actualizada
print(laptop.mostrar_info())
print(pan.mostrar_info())
