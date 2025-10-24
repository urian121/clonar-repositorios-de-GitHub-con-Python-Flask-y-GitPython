// GitHub Repository Cloner - JavaScript Simplificado

document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('cloneForm');
    const repoUrl = document.getElementById('repoUrl');
    const cloneBtn = document.getElementById('cloneBtn');
    
    // Validación del formulario
    form.addEventListener('submit', function(e) {
        const url = repoUrl.value.trim();
        
        if (!url || !document.getElementById('destinationPath').value) {
            e.preventDefault();
            alert('Por favor, completa todos los campos.');
            return;
        }
        
        if (!url.includes('github.com')) {
            e.preventDefault();
            alert('Por favor, ingresa una URL válida de GitHub.');
            return;
        }
        
        // Cambiar estado del botón
        cloneBtn.innerHTML = '<i class="bi bi-hourglass-split me-2"></i>Clonando...';
        cloneBtn.disabled = true;
    });
    
    // Validación simple en tiempo real
    repoUrl.addEventListener('input', function() {
        const url = this.value.trim();
        if (url && !url.includes('github.com')) {
            this.classList.add('is-invalid');
        } else {
            this.classList.remove('is-invalid');
        }
    });
});
