from flask import Flask, render_template, request, redirect, url_for, flash
import git # para clonar repositorios de GitHub
import os # para verificar si el directorio existe
from utils.system_directories import get_system_directories

# Configuración de la aplicación Flask
app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_aqui'  # Clave secreta para sesiones

# Página principal de la aplicación.
@app.route('/')
def index():
    # Obtener carpetas del sistema operativo del usuario
    system_dirs = get_system_directories()
    
    # Renderizar la plantilla HTML con las carpetas disponibles
    return render_template('index.html', system_directories=system_dirs)


# Clona un repositorio de GitHub en la ubicación seleccionada.
@app.route('/clone', methods=['POST'])
def clone_repository():
    try:
        # Obtener datos enviados desde el formulario HTML
        repo_url = request.form.get('repoUrl')           # URL del repositorio
        destination_path = request.form.get('destinationPath')  # Carpeta de destino
        
        # Validar que todos los campos estén completos
        if not repo_url or not destination_path:
            flash('Por favor, completa todos los campos requeridos.', 'error')
            return redirect(url_for('index'))
        
        # Validar que la URL sea de GitHub
        if 'github.com' not in repo_url:
            flash('Por favor, ingresa una URL válida de GitHub.', 'error')
            return redirect(url_for('index'))
        
        # Extraer el nombre del repositorio de la URL
        # Ejemplo: "https://github.com/usuario/repo.git" -> "repo"
        repo_name = repo_url.split('/')[-1].replace('.git', '')
        
        # Crear la ruta completa donde se guardará el repositorio
        full_destination = os.path.join(destination_path, repo_name)
        
        # Verificar si ya existe un directorio con ese nombre
        if os.path.exists(full_destination):
            flash(f'El directorio {repo_name} ya existe en {destination_path}.', 'warning')
            return redirect(url_for('index'))
        
        # ========================================================================
        # CLONAR EL REPOSITORIO
        # ========================================================================
        
        # Mostrar información en consola para debugging
        print(f"Clonando {repo_url} en {full_destination}")
        
        # Clonar el repositorio usando GitPython
        repo = git.Repo.clone_from(repo_url, full_destination)
        
        # Obtener información adicional del repositorio clonado
        repo_info = {
            'name': repo_name,
            'url': repo_url,
            'destination': full_destination,
            'branch': repo.active_branch.name,                    # Rama activa
            'commit_count': len(list(repo.iter_commits())),      # Número de commits
            'last_commit': repo.head.commit.message.strip()      # Último commit
        }
        
        # Mostrar mensaje de éxito
        flash(f'¡Repositorio clonado exitosamente!', 'success')
        flash(f'Nombre: {repo_info["name"]}', 'info')        
        return redirect(url_for('index'))
        
    # Manejo de errores específicos de Git
    except git.exc.GitCommandError as e:
        # Error específico de Git (repositorio no encontrado, problemas de auth, etc.)
        error_msg = str(e)
        if 'Authentication failed' in error_msg:
            flash('Error de autenticación. Verifica tus credenciales para repositorios privados.', 'error')
        elif 'Repository not found' in error_msg:
            flash('Repositorio no encontrado. Verifica que la URL sea correcta.', 'error')
        else:
            flash(f'Error al clonar el repositorio: {error_msg}', 'error')
        return redirect(url_for('index'))
        
    except Exception as e:
        # Error inesperado (problemas de permisos, espacio en disco, etc.)
        flash(f'Error inesperado: {str(e)}', 'error')
        return redirect(url_for('index'))

# Iniciar la aplicación
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
