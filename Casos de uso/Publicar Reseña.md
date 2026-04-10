---
id: CU-005
actores_primarios: "Usuario registrado"
actores_secundarios: "N/A"
tipo: caso_de_uso
---

# Publicar Reseña

## Descripción
Permite al usuario publicar reseñas textuales en el perfil de un negocio (RF-006).

## Condiciones
**Precondiciones:**
El usuario debe haber iniciado sesión.

**Postcondiciones:**
La reseña es visible públicamente en el perfil del negocio.

## Flujo Principal
1.- El usuario ingresa al perfil del negocio.
2.- El usuario selecciona la opción de escribir reseña.
3.- El usuario redacta su reseña.
4.- El usuario presiona enviar.
5.- El sistema guarda y publica la reseña en el perfil.

## Flujos Alternativos
El texto excede el límite de caracteres (RE-003).
El usuario cancela la publicación.

# UML

```plantuml
@startuml
left to right direction

actor "Usuario registrado" as registered_user

package "Publicar Reseña" {
  usecase "Ingresar al Perfil del Negocio" as enter_business_profile
  usecase "Seleccionar Opción de Escribir Reseña" as select_write_review
  usecase "Redactar Reseña" as write_review
  usecase "Presionar Enviar" as press_send
  usecase "Guardar y Publicar Reseña" as save_publish_review

  note top of "Publicar Reseña" : Precondición:\nEl usuario debe haber iniciado sesión.
}

registered_user --> enter_business_profile
enter_business_profile --> select_write_review
select_write_review --> write_review
write_review --> press_send

press_send .> save_publish_review : <<includes>>

note right of write_review : Flujo Alternativo:\nEl texto excede el límite de caracteres (RE-003).
note right of press_send : Flujo Alternativo:\nEl usuario cancela la publicación.
note right of save_publish_review : Postcondición:\nLa reseña es visible públicamente en el perfil del negocio.

@enduml
```