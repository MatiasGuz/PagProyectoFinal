class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get(Carrito)
        if not carrito:
            carrito = self.session["carrito"] = {}
        
        self.carrito = carrito

    def AgregarCarrito(self, producto):
        if (str(producto.id) not in self.carrito.keys()):
            self.carrito[producto.id] = {
                "producto_id" : producto.id,
                "nombre" : producto.nombre,
                "precio" : str(producto.precio),
                "cantidad" : 1,
            }
        else:
            for key, value in self.carrito.items():
                if key == str(producto.id):
                    value["cantidad"] = value["cantidad"] + 1
                    break
        self.GuardarCarrito()

    def GuardarCarrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True
        
    def Eliminar(self, producto):
        producto.id = str(producto.id)
        if producto.id in self.carrito:
            del self.carrito[producto.id]
            self.GuardarCarrito()

    def RestarUnidad(self, producto):
        for key, value in self.carrito.items():
            if key == str(producto.id):
                value["cantidad"] = value["cantidad"] - 1
                if value["cantidad"] < 1:
                    self.Eliminar(producto)
                break
        self.GuardarCarrito()

    def VaciarCarrito(self):
        carrito = self.session["carrito"] = {}
        self.session.modified = True