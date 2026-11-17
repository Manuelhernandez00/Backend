"""Repositorio de acceso a datos para Estudiante."""
from app.models import Estudiante
from .base import BaseRepository

class EstudiantesRepository(BaseRepository[Estudiante]):
    def __init__(self):
        super().__init__(Estudiante)
