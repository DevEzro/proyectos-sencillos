// Interfaz para tarea
interface Tarea {
    id: number;
    descripcion: string;
    completada: boolean;
}

// Gestión de las tareas
class ListaDeTareas {
    private tareas: Tarea[] = [];

    // Agrega tarea
    agregarTarea(descripcion: string): Tarea {
        const nuevaTarea: Tarea = {
            id: this.tareas.length + 1,
            descripcion: descripcion,
            completada: false,
        };
        this.tareas.push(nuevaTarea);
        return nuevaTarea;
    }

    // Termina tarea
    completarTarea(id: number): boolean {
        const tarea = this.tareas.find(t => t.id === id);
        if (tarea) {
            tarea.completada = true;
            return true;
        }
        return false;
    }

    // Elimina tarea
    eliminarTarea(id: number): boolean {
        const indice = this.tareas.findIndex(t => t.id === id);
        if (indice !== -1) {
            this.tareas.splice(indice, 1);
            return true;
        }
        return false;
    }

    // lista tareas
    listarTareas(): void {
        console.log("Lista de tareas:");
        this.tareas.forEach(tarea => {
            console.log(`${tarea.id}. ${tarea.descripcion} - ${tarea.completada ? "Completada" : "Pendiente"}`);
        });
    }
}

// Pausa
function esperar(ms: number) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

// Manejo de tareas asíncronas
async function manejarTareas() {
    const listaDeTareas = new ListaDeTareas();

    // Agregar tareas
    listaDeTareas.agregarTarea("Aprender TypeScript");
    listaDeTareas.agregarTarea("Desarrollar una app");
    await esperar(1000); // Simula una espera de 1 segundo

    // Listar tareas
    listaDeTareas.listarTareas();
    await esperar(1000);

    // Completar tarea
    console.log("\nCompletando la tarea con ID 1...");
    listaDeTareas.completarTarea(1);
    await esperar(1000);

    // Listar tareas
    listaDeTareas.listarTareas();
    await esperar(1000);

    // Eliminar tarea
    console.log("\nEliminando la tarea con ID 2...");
    listaDeTareas.eliminarTarea(2);
    await esperar(1000);

    // Listar tareas
    listaDeTareas.listarTareas();
}

// Ejecutar la función
manejarTareas();