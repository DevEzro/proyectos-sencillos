// Clase usuario con propiedades
class Usuario {
    private static contadorId: number = 1; // Para generar IDs automáticos
    public id: number;
    public nombre: string;
    public email: string;

    // Constructor
    constructor(nombre: string, email: string) {
        this.id = Usuario.contadorId++; // Asignar un ID único a cada usuario
        this.nombre = nombre;
        this.email = email;
    }

    // Obtiene información del usuario
    obtenerInfo(): string {
        return `ID: ${this.id}, Nombre: ${this.nombre}, Email: ${this.email}`;
    }
}

// Clase GestorDeUsuarios
class GestorDeUsuarios {
    //Crea objeto usuario
    private usuarios: Usuario[] = [];

    // Agregar usuario
    agregarUsuario(nombre: string, email: string): void {
        const nuevoUsuario = new Usuario(nombre, email);
        this.usuarios.push(nuevoUsuario);
        console.log(`Usuario ${nombre} agregado con éxito.`);
    }
    
    // Listar usuarios
    listarUsuarios(): void {
        console.log("Lista de usuarios:");
        if (this.usuarios.length === 0) {
            console.log("No hay usuarios.");
        } else {
            this.usuarios.forEach(usuario => {
                console.log(usuario.obtenerInfo());
            });
        }
    }
}

// Crear objeto GestorDeUsuarios
const gestor = new GestorDeUsuarios();

// Agregar usuarios
gestor.agregarUsuario("David", "david@correo.com");
gestor.agregarUsuario("Laura", "laura@correo.com");

// Listar usuarios agregados
gestor.listarUsuarios();  