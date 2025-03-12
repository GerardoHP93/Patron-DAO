# dao/producto_dao.py
from dao.base_dao import BaseDAO
from models.producto import Producto
from abc import abstractmethod

class ProductoDAO(BaseDAO[Producto]):
    """
    Interface específica para Producto que extiende de BaseDAO.
    Similar a MedicoDAO en el ejemplo Java.
    """
    
    @abstractmethod
    def buscar_por_nombre(self, nombre):
        """Método específico para buscar productos por nombre"""
        pass
    
    @abstractmethod
    def productos_disponibles(self):
        """Método específico para listar productos con stock disponible"""
        pass
    
    @abstractmethod
    def actualizar_stock(self, id, cantidad):
        """Método específico para actualizar el stock de un producto"""
        pass