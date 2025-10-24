# Clonar un Repositorio de GitHub con Python

Una aplicación web moderna desarrollada con Python y Flask que permite clonar repositorios de GitHub usando GitPython.

## Características

- 🎨 **Interfaz moderna**: Diseño inspirado en Tailwind CSS con Bootstrap 5
- 🚀 **Clonación rápida**: Usa GitPython para clonar repositorios de GitHub
- 📁 **Múltiples directorios**: Selecciona dónde guardar tus repositorios
- ✅ **Validación**: Validación en tiempo real de URLs de GitHub
- 📱 **Responsive**: Funciona perfectamente en dispositivos móviles
- 🔒 **Seguro**: Manejo de errores y validaciones de seguridad

## Instalación

1. **Clona este repositorio**:
```bash
git clone <url-del-repositorio>
cd como-clonar-un-repositorio-de-GitHub-con-Python
```

2. **Crea un entorno virtual**:
```bash
python -m venv env
```

3. **Activa el entorno virtual**:
```bash
# En Windows
env\Scripts\activate

# En macOS/Linux
source env/bin/activate
```

4. **Instala las dependencias**:
```bash
pip install -r requirements.txt
```

## Uso

1. **Ejecuta la aplicación**:
```bash
python app.py
```

2. **Abre tu navegador** y ve a `http://localhost:5000`

3. **Ingresa la URL del repositorio** que deseas clonar

4. **Selecciona el directorio de destino** donde quieres guardar el repositorio

5. **Haz clic en "Clonar Repositorio"**

### 1. Instalar GitPython
```bash
pip install GitPython
```

### 2. Instalar Flask (si no está instalado)
```bash
pip install Flask
```

## Directorios Disponibles

La aplicación detecta automáticamente las carpetas del sistema operativo:

### Windows:
- **Desktop** - Escritorio
- **Downloads** - Descargas  
- **Documents** - Documentos
- **Pictures** - Imágenes
- **Music** - Música
- **Videos** - Videos

### macOS:
- **Desktop** - Escritorio
- **Downloads** - Descargas
- **Documents** - Documentos  
- **Pictures** - Imágenes
- **Music** - Música
- **Movies** - Películas

### Linux:
- **Desktop** - Escritorio
- **Downloads** - Descargas
- **Documents** - Documentos
- **Pictures** - Imágenes
- **Music** - Música
- **Videos** - Videos

También disponible:
- **Directorio Actual** - Donde está la aplicación

## API Endpoints

### GET /api/repos
Lista todos los repositorios clonados en el sistema.

### DELETE /api/delete/<path:repo_path>
Elimina un repositorio específico.

## Tecnologías Utilizadas

- **Backend**: Python, Flask
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Git**: GitPython
- **Iconos**: Bootstrap Icons

## Estructura del Proyecto

```
como-clonar-un-repositorio-de-GitHub-con-Python/
├── app.py                 # Aplicación principal Flask
├── requirements.txt       # Dependencias de Python
├── templates/
│   └── index.html        # Plantilla HTML principal
├── static/               # Archivos estáticos
│   ├── css/
│   │   └── styles.css    # Estilos estilo Shadcn
│   └── js/
│       └── script.js     # JavaScript simplificado
└── README.md             # Documentación
```

## Características de la Interfaz

- **Detección automática del OS**: Detecta Windows, macOS y Linux
- **Carpetas del sistema**: Acceso directo a carpetas del usuario
- **Diseño estilo Shadcn**: Interfaz moderna y limpia
- **Validación en tiempo real**: Feedback inmediato al usuario
- **Mensajes flash**: Notificaciones de éxito, error y advertencia
- **Iconos intuitivos**: Bootstrap Icons para mejor UX
- **Responsive**: Funciona en todos los dispositivos

## Manejo de Errores

La aplicación maneja varios tipos de errores:

- **URLs inválidas**: Validación de URLs de GitHub
- **Repositorios no encontrados**: Manejo de repositorios inexistentes
- **Errores de autenticación**: Para repositorios privados
- **Directorios existentes**: Advertencia si el directorio ya existe
- **Errores de red**: Manejo de problemas de conectividad

## Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## Autor

Desarrollado con ❤️ usando Python, Flask y GitPython.
