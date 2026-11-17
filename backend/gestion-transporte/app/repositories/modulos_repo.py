"""Repositorio de acceso a datos para Modulo."""
from app.models import Modulo
from .base import BaseRepository

class ModulosRepository(BaseRepository[Modulo]):
    def __init__(self):
        super().__init__(Modulo)
