---
id: CU-006
actores_primarios: "Usuario"
actores_secundarios: "N/A"
tipo: caso_de_uso
---

# Ver Perfil de Negocio

## Descripción
Permite al usuario ver la información detallada, reseñas y calificaciones de un negocio (RF-007, RF-008, RF-012).

## Condiciones
**Precondiciones:**
El negocio debe estar activo en el sistema.

**Postcondiciones:**
El usuario visualiza toda la información pública del negocio.

## Flujo Principal
1.- El usuario selecciona un negocio desde el catálogo o búsqueda.
2.- El sistema consulta la base de datos.
3.- El sistema despliega el perfil completo, mostrando calificaciones y lista de reseñas.

## Flujos Alternativos
El negocio fue eliminado o se encuentra inactivo.

# UML
```plantuml
@startuml
left to right direction

actor "Usuario" as user

package "Ver Perfil de Negocio" {
  usecase "Seleccionar Negocio del Catálogo o Búsqueda" as select_business
  usecase "Consultar Base de Datos" as query_database
  usecase "Desplegar Perfil Completo (Información, Reseñas, Calificaciones)" as display_profile

  note top of "Ver Perfil de Negocio" : Precondición:\nEl negocio debe estar activo en el sistema.
}

user --> select_business
select_business --> query_database
query_database .> display_profile : <<includes>>

note right of query_database : Flujo Alternativo:\nEl negocio fue eliminado o se encuentra inactivo.
note right of display_profile : Postcondición:\nEl usuario visualiza toda la información pública del negocio.

@enduml
```