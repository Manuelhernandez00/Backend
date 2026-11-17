"""Repositorio de acceso a datos para FallaVehiculo."""
from app.models import FallaVehiculo
from .base import BaseRepository

class FallasVehiculoRepository(BaseRepository[FallaVehiculo]):
    def __init__(self):
        super().__init__(FallaVehiculo)
