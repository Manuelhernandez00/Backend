"""Repositorio de acceso a datos para EstudianteRuta."""
from app.models import EstudianteRuta
from .base import BaseRepository

class EstudianteRutaRepository(BaseRepository[EstudianteRuta]):
    def __init__(self):
        super().__init__(EstudianteRuta)
