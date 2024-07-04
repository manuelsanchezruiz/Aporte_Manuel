document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('btn-registrarse').addEventListener('click', function(event) {
        if (!validateForm()) {
            event.preventDefault(); // Evita que el formulario se envíe si la validación falla
        }
    });
});

function validateForm() {
    var nombreUsuario = document.getElementById('nombre-usuario').value;
    var correoElectronico = document.getElementById('correo-electronico').value;
    var contraseña = document.getElementById('contraseña').value;
    var repetirContraseña = document.getElementById('repetir-contraseña').value;

    // Verifica si todos los campos están llenos
    if (!nombreUsuario || !correoElectronico || !contraseña || !repetirContraseña) {
        alert("Por favor, complete todos los campos antes de registrarse.");
        return false;
    }

    // Verifica si las contraseñas coinciden
    if (contraseña !== repetirContraseña) {
        alert("Las contraseñas no coinciden.");
        return false;
    }

    return true; // Devuelve true si la validación es exitosa
}
