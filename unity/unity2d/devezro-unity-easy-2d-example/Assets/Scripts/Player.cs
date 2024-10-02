using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Player : MonoBehaviour
{
    // Inicialización de objetos
    public Transform controles; // Para el movimientos
    private bool tocaSuelo = true; // Para el control de salto

    void Start()
    {
        
    }

    void Update() // En constante actualización para comprobar los inputs
    {
        // Si se pulsa A/flecga izda llama al método de mover a la izda
        if (Input.GetKey(KeyCode.A) || Input.GetKey(KeyCode.LeftArrow)){
            Izquierda();
        }

        // Si se pulsa D/flecga dcha llama al método de mover a la dcha
        if (Input.GetKey(KeyCode.D) || Input.GetKey(KeyCode.LeftArrow)){
            Derecha();
        }
        // Si se pulsa el espacio llama al método de saltar y activa el boolean tocarSuelo
        if (Input.GetKey(KeyCode.Space) && tocaSuelo == true){ 
            Saltar();
            tocaSuelo = true;
        }    
    }

    public void Izquierda(){ // Resta en el eje x para aparentar movimiento a la izda
        gameObject.transform.position = new Vector3(
            gameObject.transform.position.x - 0.01f,
            gameObject.transform.position.y,
            gameObject.transform.position.z
        );
    }

    public void Derecha(){ // Suma en el eje x para aparentar movimiento a la dcha
        gameObject.transform.position = new Vector3(
            gameObject.transform.position.x + 0.01f,
            gameObject.transform.position.y,
            gameObject.transform.position.z
        );
    }

    public void Saltar(){ // Comprueba que se ha activado tocarSuelo y lo desactiva para no permitir dobles saltos
        if (tocaSuelo == true){
            tocaSuelo = false;
            if(Input.GetKey(KeyCode.Space)){}
            // Sumna en el eje y para aparentar movimiento vertical
            gameObject.transform.position = new Vector3(
                gameObject.transform.position.x,
                gameObject.transform.position.y + 0.01f,
                gameObject.transform.position.z
            );
        }
    }
}
