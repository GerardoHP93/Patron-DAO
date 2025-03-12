
# dao/cliente_dao_impl.py
from .cliente_dao import ClienteDAO  # Change this line if needed
from models.cliente import Cliente
from config import get_db
from bson.objectid import ObjectId
from typing import List, Optional

class ClienteDAOImpl(ClienteDAO):
    """
    Implementación concreta de ClienteDAO para MongoDB.
    """
    
    def __init__(self):
        self.db = get_db()
        self.collection = self.db.clientes
    
    def listar_todos(self) -> List[Cliente]:
        clientes = []
        for doc in self.collection.find():
            cliente = Cliente.from_dict(doc, str(doc['_id']))
            clientes.append(cliente)
        return clientes
    
    def leer_por_id(self, id) -> Optional[Cliente]:
        doc = self.collection.find_one({"_id": ObjectId(id)})
        if doc:
            return Cliente.from_dict(doc, str(doc['_id']))
        return None
    
    def registrar(self, cliente: Cliente) -> str:
        datos = cliente.to_dict()
        resultado = self.collection.insert_one(datos)
        return str(resultado.inserted_id)
    
    def actualizar(self, id, cliente: Cliente) -> bool:
        datos = cliente.to_dict()
        resultado = self.collection.update_one(
            {"_id": ObjectId(id)},
            {"$set": datos}
        )
        return resultado.modified_count > 0
    
    def eliminar(self, id) -> bool:
        resultado = self.collection.delete_one({"_id": ObjectId(id)})
        return resultado.deleted_count > 0
    
    def buscar_por_email(self, email):
        doc = self.collection.find_one({"email": email})
        if doc:
            return Cliente.from_dict(doc, str(doc['_id']))
        return None
    
    def clientes_activos(self):
        # Este método podría implementarse con lógica adicional
        # Por simplicidad, devolvemos todos los clientes
        return self.listar_todos()