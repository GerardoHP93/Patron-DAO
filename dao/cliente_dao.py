from dao.base_dao import BaseDAO
from models.cliente import Cliente
from abc import abstractmethod

class ClienteDAO(BaseDAO[Cliente]):
    """
    Interface específica para Cliente que extiende de BaseDAO.
    Similar a PersonaDAO en el ejemplo Java.
    """
    
    @abstractmethod
    def buscar_por_email(self, email):
        """Método específico de Cliente para buscar por email"""
        pass
    
    @abstractmethod
    def clientes_activos(self):
        """Método específico para listar clientes activos"""
        pass
