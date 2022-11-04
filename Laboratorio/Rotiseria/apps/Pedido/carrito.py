class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            carrito = self.session["carrito"] = {}
        self.carrito = carrito

    def agregar(self, plato):
        id = str(plato.codigo_plato)
        if id not in self.carrito.keys():
            self.carrito[id]={
                "plato_id": plato.codigo_plato,
                "nombre": plato.nombre_plato,
                "precio": plato.precio_plato,
                "cantidad": 1,
                "subtotal": plato.precio_plato,
            }
        else:
            for key, value in self.carrito.items():
                if key == id:
                    value["cantidad"] += 1
                    value["subtotal"] = value["precio"] * value["cantidad"]
                    break
        self.guardar()

    def lista(self):
        lista_platos_carrito = []
        for key, value in self.carrito.items():
            lista_platos_carrito.append(key)
        return lista_platos_carrito

    def guardar(self):
        self.session["carrito"] = self.carrito
        self.session.modified=True

    def eliminar(self, plato):
        id = str(plato.codigo_plato)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar()
    
    def restar(self, plato):
        id = str(plato.codigo_plato)
        for key, value in self.carrito.items():
            if key == id:
                value["cantidad"] -= 1
                value["subtotal"] = value["precio"] * value["cantidad"]
                if value["cantidad"]<1:
                    self.eliminar(plato)
                    break
        self.guardar()
    
    def limpiar(self):
        self.session["carrito"]={}
        self.session.modified=True