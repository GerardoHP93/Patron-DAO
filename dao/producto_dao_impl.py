from .producto_dao import ProductoDAO
from models.producto import Producto
from config import get_db
from bson.objectid import ObjectId
from typing import List, Optional

class ProductoDAOImpl(ProductoDAO):
    """
    Implementación concreta de ProductoDAO para MongoDB.
    """
    
    def __init__(self):
        self.db = get_db()
        self.collection = self.db.productos
    
    def listar_todos(self) -> List[Producto]:
        productos = []
        for doc in self.collection.find():
            producto = Producto.from_dict(doc, str(doc['_id']))
            productos.append(producto)
        return productos
    
    def leer_por_id(self, id) -> Optional[Producto]:
        doc = self.collection.find_one({"_id": ObjectId(id)})
        if doc:
            return Producto.from_dict(doc, str(doc['_id']))
        return None
    
    def registrar(self, producto: Producto) -> str:
        datos = producto.to_dict()
        resultado = self.collection.insert_one(datos)
        return str(resultado.inserted_id)
    
    def actualizar(self, id, producto: Producto) -> bool:
        datos = producto.to_dict()
        resultado = self.collection.update_one(
            {"_id": ObjectId(id)},
            {"$set": datos}
        )
        return resultado.modified_count > 0
    
    def eliminar(self, id) -> bool:
        resultado = self.collection.delete_one({"_id": ObjectId(id)})
        return resultado.deleted_count > 0
    
    def buscar_por_nombre(self, nombre):
        productos = []
        cursor = self.collection.find({"nombre": {"$regex": nombre, "$options": "i"}})
        for doc in cursor:
            producto = Producto.from_dict(doc, str(doc['_id']))
            productos.append(producto)
        return productos
    
    def productos_disponibles(self):
        productos = []
        cursor = self.collection.find({"stock": {"$gt": 0}})
        for doc in cursor:
            producto = Producto.from_dict(doc, str(doc['_id']))
            productos.append(producto)
        return productos
    
    def actualizar_stock(self, id, cantidad):
        resultado = self.collection.update_one(
            {"_id": ObjectId(id)},
            {"$inc": {"stock": cantidad}}
        )
        return resultado.modified_count > 0