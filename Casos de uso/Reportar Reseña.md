---
id: CU-008
actores_primarios: "Usuario registrado"
actores_secundarios: "Moderador"
tipo: caso_de_uso
---

# Reportar Reseña

## Descripción
Permite al usuario reportar una reseña que considere inapropiada (RF-011).

## Condiciones
**Precondiciones:**
El usuario debe haber iniciado sesión.

**Postcondiciones:**
La reseña queda marcada en el sistema para revisión administrativa.

## Flujo Principal
1.- El usuario visualiza una reseña específica.
2.- El usuario selecciona la opción de reportar.
3.- El usuario proporciona el motivo del reporte.
4.- El sistema registra el reporte y notifica a los moderadores.

## Flujos Alternativos
El usuario cancela el proceso.

# UML 
```plantuml
@startuml
left to right direction

actor "Usuario registrado" as registered_user
actor "Moderador" as moderator

package "Reportar Reseña" {
  usecase "Visualizar Reseña Específica" as view_review
  usecase "Seleccionar Opción de Reportar" as select_report_option
  usecase "Proporcionar Motivo del Reporte" as provide_reason
  usecase "Registrar Reporte y Notificar Moderadores" as register_notify

  note top of "Reportar Reseña" : Precondición:\nEl usuario debe haber iniciado sesión.
}

registered_user --> view_review
view_review --> select_report_option
select_report_option --> provide_reason

provide_reason .> register_notify : <<includes>>

register_notify --> moderator

note right of provide_reason : Flujo Alternativo:\nEl usuario cancela el proceso.
note right of register_notify : Postcondición:\nLa reseña queda marcada en el sistema para revisión administrativa.

@enduml
```
