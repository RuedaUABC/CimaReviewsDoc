---
id: CU-010
actores_primarios: "Vendedor"
actores_secundarios: "N/A"
tipo: caso_de_uso
---

# Gestionar Negocio

## Descripción
Permite a los vendedores editar o eliminar la información de sus propios negocios (RF-015, RF-016).

## Condiciones
**Precondiciones:**
El vendedor debe ser el creador/propietario del negocio en el sistema.

**Postcondiciones:**
La información del negocio se actualiza o este deja de estar disponible en el sistema.

## Flujo Principal
1.- El vendedor accede al panel de mis negocios.
2.- Selecciona un negocio para editar o eliminar.
3.- Si edita, actualiza la información y guarda.
4.- Si elimina, el sistema solicita confirmación y desactiva el negocio.
5.- El sistema aplica los cambios.

## Flujos Alternativos
El vendedor cancela la acción.

# UML
```plantuml
@startuml
left to right direction

actor "Vendedor" as seller

package "Gestionar Negocio" {
  usecase "Acceder al Panel de Mis Negocios" as access_panel
  usecase "Seleccionar Negocio" as select_business
  usecase "Editar Información del Negocio" as edit_info
  usecase "Eliminar Negocio" as delete_business
  usecase "Aplicar Cambios al Negocio" as apply_changes

  note top of "Gestionar Negocio" : Precondición:\nEl vendedor debe ser el creador/propietario del negocio en el sistema.
}

seller --> access_panel
access_panel --> select_business

select_business --> edit_info
select_business --> delete_business

edit_info .> apply_changes : <<includes>>
delete_business .> apply_changes : <<includes>>

note right of edit_info : Flujo Alternativo:\nEl vendedor cancela la acción.
note right of delete_business : Flujo Alternativo:\nEl vendedor cancela la acción.
note right of apply_changes : Postcondición:\nLa información del negocio se actualiza o este deja de estar disponible en el sistema.

@enduml
```