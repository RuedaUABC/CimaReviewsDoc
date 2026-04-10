---
id: CU-007
actores_primarios: "Usuario registrado"
actores_secundarios: "N/A"
tipo: caso_de_uso
---

# Gestionar Reseña y Calificación

## Descripción
Permite al usuario editar o eliminar sus propias reseñas y calificaciones (RF-009, RF-010, RF-013).

## Condiciones
**Precondiciones:**
El usuario debe tener al menos una reseña o calificación previamente publicada.

**Postcondiciones:**
La reseña o calificación es modificada o eliminada permanentemente.

## Flujo Principal
1.- El usuario accede a su historial o al perfil del negocio.
2.- Selecciona la opción de editar o eliminar sobre su reseña/calificación.
3.- Si edita, modifica los datos y confirma.
4.- Si elimina, el sistema pide confirmación y procesa el borrado.
5.- El sistema actualiza la base de datos.

## Flujos Alternativos
El usuario cancela la edición o eliminación.

# UML 
```plantuml
@startuml
left to right direction

actor "Usuario registrado" as registered_user

package "Gestionar Reseña y Calificación" {
  usecase "Acceder a Historial o Perfil del Negocio" as access_history_profile
  usecase "Seleccionar Reseña/Calificación" as select_review_rating
  usecase "Editar Reseña/Calificación" as edit_review_rating
  usecase "Eliminar Reseña/Calificación" as delete_review_rating
  usecase "Actualizar Base de Datos" as update_database

  note top of "Gestionar Reseña y Calificación" : Precondición:\nEl usuario debe tener al menos una reseña o calificación previamente publicada.
}

registered_user --> access_history_profile
access_history_profile --> select_review_rating

select_review_rating --> edit_review_rating
select_review_rating --> delete_review_rating

edit_review_rating .> update_database : <<includes>>
delete_review_rating .> update_database : <<includes>>

note right of edit_review_rating : Flujo Alternativo:\nEl usuario cancela la edición.
note right of delete_review_rating : Flujo Alternativo:\nEl usuario cancela la eliminación.
note right of update_database : Postcondición:\nLa reseña o calificación es modificada o eliminada permanentemente.

@enduml
```