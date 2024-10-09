// Clase usuario con propiedades
var Usuario = /** @class */ (function () {
    // Constructor
    function Usuario(nombre, email) {
        this.id = Usuario.contadorId++; // Asignar un ID único a cada usuario
        this.nombre = nombre;
        this.email = email;
    }
    // Obtiene información del usuario
    Usuario.prototype.obtenerInfo = function () {
        return "ID: ".concat(this.id, ", Nombre: ").concat(this.nombre, ", Email: ").concat(this.email);
    };
    Usuario.contadorId = 1; // Para generar IDs automáticos
    return Usuario;
}());
// Clase GestorDeUsuarios
var GestorDeUsuarios = /** @class */ (function () {
    function GestorDeUsuarios() {
        //Crea objeto usuario
        this.usuarios = [];
    }
    // Agregar usuario
    GestorDeUsuarios.prototype.agregarUsuario = function (nombre, email) {
        var nuevoUsuario = new Usuario(nombre, email);
        this.usuarios.push(nuevoUsuario);
        console.log("Usuario ".concat(nombre, " agregado con \u00E9xito."));
    };
    // Listar usuarios
    GestorDeUsuarios.prototype.listarUsuarios = function () {
        console.log("Lista de usuarios:");
        if (this.usuarios.length === 0) {
            console.log("No hay usuarios.");
        }
        else {
            this.usuarios.forEach(function (usuario) {
                console.log(usuario.obtenerInfo());
            });
        }
    };
    return GestorDeUsuarios;
}());
// Crear objeto GestorDeUsuarios
var gestor = new GestorDeUsuarios();
// Agregar usuarios
gestor.agregarUsuario("David", "david@correo.com");
gestor.agregarUsuario("Laura", "laura@correo.com");
// Listar usuarios agregados
gestor.listarUsuarios();
