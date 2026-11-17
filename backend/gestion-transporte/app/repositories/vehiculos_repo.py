"""Repositorio de acceso a datos para Vehiculo."""
from app.models import Vehiculo
from .base import BaseRepository

class VehiculosRepository(BaseRepository[Vehiculo]):
    def __init__(self):
        super().__init__(Vehiculo)
