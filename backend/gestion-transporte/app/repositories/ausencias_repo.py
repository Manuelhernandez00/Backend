"""Repositorio de acceso a datos para Ausencia."""
from app.models import Ausencia
from .base import BaseRepository

class AusenciasRepository(BaseRepository[Ausencia]):
    def __init__(self):
        super().__init__(Ausencia)
