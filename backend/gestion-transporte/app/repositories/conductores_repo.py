"""Repositorio de acceso a datos para Conductor."""
from app.models import Conductor
from .base import BaseRepository

class ConductoresRepository(BaseRepository[Conductor]):
    def __init__(self):
        super().__init__(Conductor)
