from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List, Optional

T = TypeVar('T')  # Tipo genérico para el modelo

class BaseDAO(Generic[T], ABC):
    """
    Clase base abstracta que define operaciones CRUD básicas.
    Similar al interface CRUD<T> en Java.
    """
    
    @abstractmethod
    def listar_todos(self) -> List[T]:
        """Obtener todos los registros"""
        pass
    
    @abstractmethod
    def leer_por_id(self, id) -> Optional[T]:
        """Leer un registro por su ID"""
        pass
    
    @abstractmethod
    def registrar(self, entidad: T) -> str:
        """Registrar una nueva entidad"""
        pass
    
    @abstractmethod
    def actualizar(self, id, entidad: T) -> bool:
        """Actualizar una entidad existente"""
        pass
    
    @abstractmethod
    def eliminar(self, id) -> bool:
        """Eliminar una entidad por su ID"""
        pass