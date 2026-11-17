"""Repositorios de acceso a datos para Gestión de Transporte Escolar."""
from .base import BaseRepository
from .acudientes_repo import AcudientesRepository
from .ausencias_repo import AusenciasRepository
from .conductores_repo import ConductoresRepository
from .estudiante_ruta_repo import EstudianteRutaRepository
from .estudiantes_repo import EstudiantesRepository
from .fallas_vehiculo_repo import FallasVehiculoRepository
from .modulos_repo import ModulosRepository
from .paraderos_repo import ParaderosRepository
from .registros_abordaje_repo import RegistrosAbordajeRepository
from .roles_modulos_repo import RolesModulosRepository
from .roles_repo import RolesRepository
from .rutas_repo import RutasRepository
from .usuarios_repo import UsuariosRepository
from .vehiculos_repo import VehiculosRepository

__all__ = [name for name in globals() if name.endswith("Repository") or name == "BaseRepository"]
