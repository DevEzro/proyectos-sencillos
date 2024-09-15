package Concesionario;

import java.util.*;

public class Main {

    static String opcion, modelo;
    static int matricula, velocidad;
    static Scanner teclado = new Scanner(System.in);
    static boolean salir = false;
    static ArrayList<Coches> lista = new ArrayList();

    public static void main(String[] args) {

        do {
            System.out.println("Introduce una opcion");
            System.out.println("1- Añadir coche");
            System.out.println("2- Quitar coche");
            System.out.println("3- Mostrar info coche");
            System.out.println("0- SALIR");
            opcion = teclado.next();
            switch (opcion) {
                case "0":
                    System.out.println("Hasta otra!");
                    salir = true;
                    break;
                case "1":
                    Registro();
                    break;
                case "2":
                    Borrar();
                    break;
                case "3":
                    Info();
                    break;

                default:
                    System.out.println("Opcion no válida vuelve a intentarlo");
            }
        } while (salir == false);

    }

    private static void Registro() {
        Coches coche = new Coches();
        System.out.println("Introduce una matricula");
        matricula = teclado.nextInt();
        coche.setMatricula(matricula);
        System.out.println("Introduce un modelo");
        modelo = teclado.next();
        coche.setModelo(modelo);
        System.out.println("Introduce una velocidad");
        velocidad = teclado.nextInt();
        coche.setVelocidad(velocidad);
        lista.add(coche);
    }

    private static void Borrar() {
        System.out.println("Introduce una matricula");
        matricula = teclado.nextInt();

        Iterator<Coches> iterator = lista.iterator();
        
        while(iterator.hasNext()){
            Coches c = iterator.next();
            if (matricula == c.getMatricula()) {
                iterator.remove();
            } else {
                System.out.println("La matricula no existe");
                System.out.println("Saliendo...");
            }
        }
    }

    private static void Info() {
        for (Coches c : lista) {
            System.out.println("******INFO-COCHE*****");
            /*System.out.println(c.getMatricula());
            System.out.println(c.getModelo());
            System.out.println(c.getVelocidad());*/
            c.toString(matricula, modelo, velocidad);
            System.out.println("*********************");
        
        }
    }
}
