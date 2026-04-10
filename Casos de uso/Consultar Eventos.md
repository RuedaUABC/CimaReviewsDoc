---
id: CU-011
actores_primarios: "Usuario"
actores_secundarios: "N/A"
tipo: caso_de_uso
---

# Consultar Eventos

## Descripción
Permite a los usuarios ver los eventos activos dentro de la universidad (RF-040).

## Condiciones
**Precondiciones:**
N/A

**Postcondiciones:**
El usuario visualiza la información de los eventos.

## Flujo Principal
1.- El usuario ingresa a la sección de eventos.
2.- El sistema consulta la base de datos por eventos vigentes.
3.- El sistema muestra la lista o calendario de eventos activos.

## Flujos Alternativos
No hay eventos activos en ese momento.

# UML
```plantuml
@startuml
left to right direction

actor "Usuario" as user

package "Consultar Eventos" {
  usecase "Ingresar a Sección de Eventos" as enter_section
  usecase "Consultar Eventos Vigentes" as query_events
  usecase "Mostrar Lista/Calendario de Eventos Activos" as display_events

  note top of "Consultar Eventos" : Precondiciones:\nN/A
}

user --> enter_section
enter_section --> query_events
query_events .> display_events : <<includes>>

note right of display_events : Flujo Alternativo:\nNo hay eventos activos.
note right of display_events : Postcondición:\nEl usuario visualiza la información de los eventos.

@enduml
```