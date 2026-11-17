"""Repositorio de acceso a datos para Rol."""
from app.models import Rol
from .base import BaseRepository

class RolesRepository(BaseRepository[Rol]):
    def __init__(self):
        super().__init__(Rol)
