"""Repositorio de acceso a datos para Acudiente."""
from app.models import Acudiente
from .base import BaseRepository

class AcudientesRepository(BaseRepository[Acudiente]):
    def __init__(self):
        super().__init__(Acudiente)
