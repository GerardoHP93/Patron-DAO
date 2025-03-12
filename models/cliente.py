class Cliente:
    def __init__(self, id=None, nombre="", email="", telefono=""):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
    
    def to_dict(self):
        return {
            "nombre": self.nombre,
            "email": self.email,
            "telefono": self.telefono
        }
    
    @staticmethod
    def from_dict(data, id=None):
        return Cliente(
            id=id,
            nombre=data.get("nombre", ""),
            email=data.get("email", ""),
            telefono=data.get("telefono", "")
        )
