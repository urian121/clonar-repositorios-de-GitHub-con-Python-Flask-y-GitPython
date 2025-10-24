# Utilidades para detectar carpetas del sistema operativo
import os
import platform
from pathlib import Path


def get_system_directories():
    """
    Detecta automáticamente las carpetas del sistema operativo del usuario.
    Returns:
        dict: Diccionario con nombre de carpeta como clave y ruta completa como valor
    """
    # Obtener el sistema operativo actual
    system = platform.system().lower()
    
    # Obtener el directorio home del usuario
    home = Path.home()
    
    # Mapeo base de carpetas comunes
    directories = {
        'Desktop': str(home / 'Desktop'),
        'Downloads': str(home / 'Downloads'),
        'Documents': str(home / 'Documents'),
        'Pictures': str(home / 'Pictures'),
        'Music': str(home / 'Music'),
        'Videos': str(home / 'Videos')
    }
    
    # Ajustar rutas según el sistema operativo
    if system == 'windows':
        # Windows usa las mismas carpetas base
        pass  # No necesita cambios adicionales
    elif system == 'darwin':  # macOS
        # En macOS, Videos se llama Movies
        directories['Movies'] = str(home / 'Movies')
        # Eliminar Videos si existe Movies
        if 'Videos' in directories:
            del directories['Videos']
    elif system == 'linux':
        # Linux usa las mismas carpetas base
        pass  # No necesita cambios adicionales
    
    # Filtrar solo directorios que existen físicamente
    existing_dirs = {}
    for name, path in directories.items():
        if os.path.exists(path):
            existing_dirs[name] = path
    
    return existing_dirs


def get_os_info():
    """
    Obtiene información del sistema operativo.
    
    Returns:
        dict: Información del sistema operativo
    """
    return {
        'system': platform.system(),
        'release': platform.release(),
        'version': platform.version(),
        'machine': platform.machine(),
        'processor': platform.processor()
    }
