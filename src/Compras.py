from Productos import Producto

class Carrito:

    def __init__(self):
        self.productos = [] 

    def agregar_producto(self, producto, cantidad=1):

        total = 0
        for prod, cant in self.productos:
            total += cant

        if total + cantidad > 50:
            print("No se pueden agregar más de 50 productos.")
            return

        if producto.stock < cantidad:
            print("No hay suficiente stock.")
            return

        for i in range(len(self.productos)):
            prod, cant = self.productos[i]

            if prod.id == producto.id:
                self.productos[i] = (prod, cant + cantidad)
                print("Producto agregado.")
                return

        self.productos.append((producto, cantidad))
        print("Producto agregado.")

    def calcular_total(self):
        total = 0

        for prod, cant in self.productos:
            total += prod.precio_base * cant

        return total

    def vaciar_carrito(self):
        self.productos.clear()
        print("Carrito vaciado.")

    def generar_factura(self):

        if len(self.productos) == 0:
            print("El carrito está vacío.")
            return

        print("Procesando compra...")

        for prod, cant in self.productos:
            prod.reducir_stock(cant)

        print("Total a pagar:", self.calcular_total())

        self.productos.clear()

        print("Compra finalizada.")
