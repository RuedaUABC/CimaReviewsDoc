---
id: CU-004
actores_primarios: "Usuario"
actores_secundarios: "N/A"
tipo: caso_de_uso
---
# Buscar y Ordenar Negocios

## Descripción
Permite al usuario buscar un negocio por nombre u ordenarlos por calificación (RF-004, RF-005).

## Condiciones
**Precondiciones:**
El sistema debe tener negocios registrados.

**Postcondiciones:**
El usuario visualiza los resultados esperados.

## Flujo Principal
1.- El usuario navega a la sección de exploración.
2.- El usuario ingresa un nombre en el buscador o selecciona el filtro de orden por calificación.
3.- El sistema procesa la solicitud.
4.- El sistema muestra la lista de negocios que coinciden con los criterios.

## Flujos Alternativos
No se encuentran negocios con el nombre especificado.

# UML

```plantuml
@startuml
left to right direction

actor "Usuario" as user

package "Buscar y Ordenar Negocios" {
  usecase "Buscar Negocio por Nombre" as search_name
  usecase "Ordenar Negocios por Calificación" as sort_rating
  usecase "Mostrar Lista de Negocios" as show_list

  note top of "Buscar y Ordenar Negocios" : Precondición:\nSistema debe tener negocios registrados.
}

user --> search_name
user --> sort_rating

search_name .> show_list : <<includes>>
sort_rating .> show_list : <<includes>>

' Notas para flujos alternativos y postcondiciones
note right of search_name : Flujo Alternativo:\nNo se encuentran negocios.
note right of show_list : Postcondición:\nUsuario visualiza resultados esperados.

@enduml
```

