"""Repositorio de acceso a datos para Ruta."""
from app.models import Ruta
from .base import BaseRepository

class RutasRepository(BaseRepository[Ruta]):
    def __init__(self):
        super().__init__(Ruta)
