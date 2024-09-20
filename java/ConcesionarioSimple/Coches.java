package Concesionario;

public class Coches {
    int matricula;
    String modelo;
    int velocidad;

    Coches() {
    }

    public int getMatricula() {
        return matricula;
    }

    public String getModelo() {
        return modelo;
    }

    public int getVelocidad() {
        return velocidad;
    }

    public void setMatricula(int matricula) {
        this.matricula = matricula;
    }

    public void setModelo(String modelo) {
        this.modelo = modelo;
    }

    public void setVelocidad(int velocidad) {
        this.velocidad = velocidad;
    }
    
    public void toString(int matricula, String modelo, int velocidad){
        System.out.println("Matricula: "+matricula+"\nModelo: "+modelo+"\nVelocidad: "+velocidad);
    }
}    
