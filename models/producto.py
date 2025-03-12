class Producto:
    def __init__(self, id=None, nombre="", descripcion="", precio=0.0, stock=0):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
    
    def to_dict(self):
        return {
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "precio": self.precio,
            "stock": self.stock
        }
    
    @staticmethod
    def from_dict(data, id=None):
        return Producto(
            id=id,
            nombre=data.get("nombre", ""),
            descripcion=data.get("descripcion", ""),
            precio=data.get("precio", 0.0),
            stock=data.get("stock", 0)
        )