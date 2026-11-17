"""Repositorio de acceso a datos para Usuario."""
from app.models import Usuario
from .base import BaseRepository

class UsuariosRepository(BaseRepository[Usuario]):
    def __init__(self):
        super().__init__(Usuario)
