"""Repositorio de acceso a datos para Paradero."""
from app.models import Paradero
from .base import BaseRepository

class ParaderosRepository(BaseRepository[Paradero]):
    def __init__(self):
        super().__init__(Paradero)
