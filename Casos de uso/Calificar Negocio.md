---
id: CU-003
actores_primarios: "Usuario registrado"
actores_secundarios: "N/A"
tipo: caso_de_uso
---

# Calificar Negocio

## Descripción
Permite al usuario calificar negocios en una escala de 1 a 5 estrellas (RF-003).

## Condiciones
**Precondiciones:**
El usuario debe haber iniciado sesión.
El negocio debe existir en el catálogo.

**Postcondiciones:**
La calificación general del negocio se actualiza en el sistema.

## Flujo Principal
1.- El usuario ingresa al perfil del negocio.
2.- El usuario selecciona la opción de calificar.
3.- El usuario asigna una calificación de 1 a 5 estrellas.
4.- El usuario confirma la calificación.
5.- El sistema registra y promedia la calificación del negocio.

## Flujos Alternativos
El usuario cancela la acción.
El usuario ya había calificado (se actualiza su calificación anterior).

# UML

```plantuml
@startuml
left to right direction

actor "Usuario registrado" as registered_user

package "Calificar Negocio" {
  usecase "Ingresar al Perfil del Negocio" as view_profile
  usecase "Seleccionar Opción de Calificar" as select_rate_option
  usecase "Asignar Calificación (1-5 estrellas)" as assign_rating
  usecase "Confirmar Calificación" as confirm_rating
  usecase "Registrar y Promediar Calificación" as update_rating_system

  note top of "Calificar Negocio" : Precondiciones:\n- Usuario debe haber iniciado sesión.\n- Negocio debe existir en el catálogo.
}

registered_user --> view_profile
view_profile --> select_rate_option
select_rate_option --> assign_rating
assign_rating --> confirm_rating

confirm_rating .> update_rating_system : <<includes>>

' Notas para flujos alternativos y postcondiciones
note right of confirm_rating : Flujo Alternativo:\n- Usuario cancela la acción.\n- Usuario ya había calificado (se actualiza su calificación anterior).
note right of update_rating_system : Postcondición:\nLa calificación general del negocio se actualiza en el sistema.

@enduml
```

