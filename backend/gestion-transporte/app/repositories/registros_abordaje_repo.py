"""Repositorio de acceso a datos para RegistroAbordaje."""
from app.models import RegistroAbordaje
from .base import BaseRepository

class RegistrosAbordajeRepository(BaseRepository[RegistroAbordaje]):
    def __init__(self):
        super().__init__(RegistroAbordaje)
