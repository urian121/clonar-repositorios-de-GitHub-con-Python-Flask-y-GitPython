from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import git
import os
import platform
from pathlib import Path

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_aqui'

# Obtener rutas del sistema según el OS
def get_system_directories():
    system = platform.system().lower()
    home = Path.home()
    
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
        directories.update({
            'Desktop': str(home / 'Desktop'),
            'Downloads': str(home / 'Downloads'),
            'Documents': str(home / 'Documents'),
            'Pictures': str(home / 'Pictures'),
            'Music': str(home / 'Music'),
            'Videos': str(home / 'Videos')
        })
    elif system == 'darwin':  # macOS
        directories.update({
            'Desktop': str(home / 'Desktop'),
            'Downloads': str(home / 'Downloads'),
            'Documents': str(home / 'Documents'),
            'Pictures': str(home / 'Pictures'),
            'Music': str(home / 'Music'),
            'Movies': str(home / 'Movies')
        })
    elif system == 'linux':
        directories.update({
            'Desktop': str(home / 'Desktop'),
            'Downloads': str(home / 'Downloads'),
            'Documents': str(home / 'Documents'),
            'Pictures': str(home / 'Pictures'),
            'Music': str(home / 'Music'),
            'Videos': str(home / 'Videos')
        })
    
    # Filtrar solo directorios que existen
    existing_dirs = {}
    for name, path in directories.items():
        if os.path.exists(path):
            existing_dirs[name] = path
    
    return existing_dirs

@app.route('/')
def index():
    system_dirs = get_system_directories()
    return render_template('index.html', system_directories=system_dirs)

@app.route('/clone', methods=['POST'])
def clone_repository():
    try:
        # Obtener datos del formulario
        repo_url = request.form.get('repoUrl')
        destination_path = request.form.get('destinationPath')
        
        # Validar datos
        if not repo_url or not destination_path:
            flash('Por favor, completa todos los campos requeridos.', 'error')
            return redirect(url_for('index'))
        
        # Validar URL de GitHub
        if 'github.com' not in repo_url:
            flash('Por favor, ingresa una URL válida de GitHub.', 'error')
            return redirect(url_for('index'))
        
        # Extraer nombre del repositorio de la URL
        repo_name = repo_url.split('/')[-1].replace('.git', '')
        
        # Usar la ruta directamente (ya viene completa del formulario)
        full_destination = os.path.join(destination_path, repo_name)
        
        # Verificar si el directorio ya existe
        if os.path.exists(full_destination):
            flash(f'El directorio {repo_name} ya existe en {destination_path}.', 'warning')
            return redirect(url_for('index'))
        
        # Clonar el repositorio usando GitPython
        print(f"Clonando {repo_url} en {full_destination}")
        repo = git.Repo.clone_from(repo_url, full_destination)
        
        # Obtener información del repositorio
        repo_info = {
            'name': repo_name,
            'url': repo_url,
            'destination': full_destination,
            'branch': repo.active_branch.name,
            'commit_count': len(list(repo.iter_commits())),
            'last_commit': repo.head.commit.message.strip()
        }
        
        flash(f'¡Repositorio clonado exitosamente!', 'success')
        flash(f'Nombre: {repo_info["name"]}', 'info')
        flash(f'Rama: {repo_info["branch"]}', 'info')
        flash(f'Commits: {repo_info["commit_count"]}', 'info')
        flash(f'Ubicación: {repo_info["destination"]}', 'info')
        
        return redirect(url_for('index'))
        
    except git.exc.GitCommandError as e:
        error_msg = str(e)
        if 'Authentication failed' in error_msg:
            flash('Error de autenticación. Verifica tus credenciales para repositorios privados.', 'error')
        elif 'Repository not found' in error_msg:
            flash('Repositorio no encontrado. Verifica que la URL sea correcta.', 'error')
        else:
            flash(f'Error al clonar el repositorio: {error_msg}', 'error')
        return redirect(url_for('index'))
        
    except Exception as e:
        flash(f'Error inesperado: {str(e)}', 'error')
        return redirect(url_for('index'))


@app.route('/api/repos')
def list_repos():
    """API endpoint para listar repositorios clonados"""
    try:
        repos = []
        base_dirs = ['repos', 'downloads', 'projects', 'temp', '.']
        
        for base_dir in base_dirs:
            if os.path.exists(base_dir):
                for item in os.listdir(base_dir):
                    item_path = os.path.join(base_dir, item)
                    if os.path.isdir(item_path) and os.path.exists(os.path.join(item_path, '.git')):
                        try:
                            repo = git.Repo(item_path)
                            repos.append({
                                'name': item,
                                'path': item_path,
                                'branch': repo.active_branch.name,
                                'last_commit': repo.head.commit.message.strip(),
                                'last_commit_date': repo.head.commit.committed_datetime.isoformat()
                            })
                        except:
                            continue
        
        return jsonify(repos)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
