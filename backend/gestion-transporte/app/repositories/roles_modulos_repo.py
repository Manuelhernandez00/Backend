"""Repositorio de acceso a datos para RolModulo."""
from app.models import RolModulo
from .base import BaseRepository

class RolesModulosRepository(BaseRepository[RolModulo]):
    def __init__(self):
        super().__init__(RolModulo)
