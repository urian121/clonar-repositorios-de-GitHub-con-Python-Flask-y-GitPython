# GitHub Repository Cloner

Aplicación web para clonar repositorios de GitHub usando Python y GitPython. Interfaz moderna que detecta automáticamente las carpetas del sistema operativo.

![Demo](https://raw.githubusercontent.com/urian121/imagenes-proyectos-github/refs/heads/master/clonar-repositorios-de-GitHub-con-Python-Flask-y-GitPython.png)


## 🚀 Instalación Rápida

```bash
# Clonar repositorio
git clone <url-del-repositorio>
cd como-clonar-un-repositorio-de-GitHub-con-Python

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar aplicación
python app.py
```

Abre `http://localhost:5000` en tu navegador.

## ✨ Características

- **Detección automática del OS**: Windows, macOS, Linux
- **Carpetas del sistema**: Desktop, Downloads, Documents, Pictures, Music, Videos
- **Interfaz moderna**: Bootstrap 5 con estilo Shadcn
- **Validación en tiempo real**: URLs de GitHub
- **Manejo de errores**: Repositorios privados, permisos, etc.

## 📁 Estructura

```
├── app.py                 # Aplicación Flask principal
├── utils/
│   └── system_directories.py  # Detección de carpetas del OS
├── templates/index.html   # Interfaz web
├── static/
│   ├── css/styles.css     # Estilos Shadcn
│   └── js/script.js       # JavaScript simplificado
└── requirements.txt       # Dependencias
```

## 🛠️ Tecnologías

- **Backend**: Python, Flask, GitPython
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Compatibilidad**: Windows, macOS, Linux

## 📝 Uso

1. Ingresa la URL del repositorio de GitHub
2. Selecciona la carpeta de destino (se detecta automáticamente)
3. Haz clic en "Clonar Repositorio"

La aplicación clonará el repositorio en la ubicación seleccionada y mostrará el resultado.
