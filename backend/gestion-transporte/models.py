"""Compatibilidad con los imports existentes (`from models import ...`).

Las definiciones principales viven en `app.models`. Este módulo evita tener
que modificar todos los routers existentes al reorganizar la estructura.
"""
from app.models import (
    Auditoria, Rol, Modulo, RolModulo, Usuario, Acudiente, Estudiante,
    Conductor, Vehiculo, Ruta, Paradero, EstudianteRuta, RegistroAbordaje,
    Ausencia, FallaVehiculo, ZONA_CO, ahora,
)

__all__ = [
    "Auditoria", "Rol", "Modulo", "RolModulo", "Usuario", "Acudiente",
    "Estudiante", "Conductor", "Vehiculo", "Ruta", "Paradero",
    "EstudianteRuta", "RegistroAbordaje", "Ausencia", "FallaVehiculo",
    "ZONA_CO", "ahora",
]
