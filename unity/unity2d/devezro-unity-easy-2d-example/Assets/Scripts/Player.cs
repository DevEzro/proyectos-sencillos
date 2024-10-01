using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Player : MonoBehaviour
{

    public Transform controles;
    private SpriteRenderer playerSprite;
    private bool tocaSuelo = true;

    void Start()
    {
        
    }

    void Update()
    {
        if (Input.GetKey(KeyCode.A) || Input.GetKey(KeyCode.LeftArrow)){
            Izquierda();
        }
        
        if (Input.GetKey(KeyCode.D) || Input.GetKey(KeyCode.LeftArrow)){
            Derecha();
        }
        
        if (Input.GetKey(KeyCode.Space) && tocaSuelo == true){ 
            Saltar();
            tocaSuelo = true;
        }    
    }

    public void Izquierda(){
        gameObject.transform.position = new Vector3(
            gameObject.transform.position.x - 0.01f,
            gameObject.transform.position.y,
            gameObject.transform.position.z
        );
    }

    public void Derecha(){
        gameObject.transform.position = new Vector3(
            gameObject.transform.position.x + 0.01f,
            gameObject.transform.position.y,
            gameObject.transform.position.z
        );
    }

    public void Saltar(){
        if (tocaSuelo == true){
            tocaSuelo = false;
            if(Input.GetKey(KeyCode.Space)){
            }
            gameObject.transform.position = new Vector3(
                gameObject.transform.position.x,
                gameObject.transform.position.y + 0.01f,
                gameObject.transform.position.z
            );
        }
    }
}
