# import random


# using System.Collections;
# using System.Collections.Generic;
# using UnityEngine;

# public class PlayerMove : MonoBehaviour
# {
#     private Rigidbody2D rb2D; 

#     [Header("Movimiento")]
#     public float movimientoHorizontal = 0f;

#     [SerializeField] private float velocidadDelMovimiento = 0f; 
#     [Range(0, 0.3f)][SerializeField] private float suavizadoDeMovimiento;

#     private Vector3 velocidad = Vector3.zero;
#     private bool mirandoDerecha = true;

#     [Header("Salto")]

#     [SerializeField] private float fuerzaDeSalto;
#     [SerializeField] private LayerMask queEsSuelo;
#     [SerializeField] private Transform controladorSuelo;
#     [SerializeField] private Vector3 dimensionesCaja;
#     [SerializeField] private bool enSuelo;
#     private bool salto = false;

#     // [Header("Animacion")]
#     // private Animator animator;


#     private void Start()
#     {
#         rb2D = GetComponent<Rigidbody2D>(); // ✅ Corrección aquí también
#         // animator = GetComponent<Animator>();
#     }

#     private void Update()
#     {
        
#         movimientoHorizontal = Input.GetAxisRaw("Horizontal") * velocidadDelMovimiento;

#         // animator.SetFloat("Horizontal", Mathf.Abs(movimientoHorizontal));

#         if (Input.GetButtonDown("Jump"))
#         {
#             salto = true;
#         }
#     }

#     private void FixedUpdate()
#     {
#         enSuelo = Physics2D.OverlapBox(controladorSuelo.position, dimensionesCaja, 0f, queEsSuelo);
#         // animator.SetBool("enSuelo",enSuelo );
#         Mover(movimientoHorizontal * Time.fixedDeltaTime, salto);
#         salto = false;
#     }

#     private void Mover(float mover, bool saltar)
#     {
#         Vector3 velocidadObjetivo = new Vector3(mover, rb2D.velocity.y);
#         rb2D.velocity = Vector3.SmoothDamp(rb2D.velocity, velocidadObjetivo, ref velocidad, suavizadoDeMovimiento);

#         if (mover > 0 && !mirandoDerecha)
#         {
#             Girar();
#         }
#         else if (mover < 0 && mirandoDerecha)
#         {
#             Girar();
#         }
#         if (enSuelo && saltar)
#         {
#             enSuelo = false;
#             rb2D.AddForce(new Vector2(0f, fuerzaDeSalto));
#         }

#     }

#     private void Girar()
#     {
#         mirandoDerecha = !mirandoDerecha;
#         Vector3 escala = transform.localScale;
#         escala.x *= -1;
#         transform.localScale = escala; // ✅ Corrección aquí
#     }

#     private void OnDrawGizmos()
#     {
#         Gizmos.color = Color.yellow;
#         Gizmos.DrawWireCube(controladorSuelo.position, dimensionesCaja);
#     }

# }
