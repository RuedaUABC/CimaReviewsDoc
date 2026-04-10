---
id: CU-013
actores_primarios: "Moderador"
actores_secundarios: "Vendedor"
tipo: caso_de_uso
---

# Moderar Solicitudes de Eventos

## Descripción
Permite a los moderadores aprobar o rechazar solicitudes de negocios para eventos (RF-039).

## Condiciones
**Precondiciones:**
Debe haber solicitudes pendientes enviadas por los vendedores.

**Postcondiciones:**
El negocio queda inscrito en el evento o su participación es denegada.

## Flujo Principal
1.- El moderador accede al panel administrativo de eventos.
2.- Visualiza la lista de solicitudes pendientes.
3.- El moderador selecciona aprobar o rechazar para cada solicitud.
4.- El sistema actualiza el estado y notifica al vendedor.

# UML

```plantuml
@startuml
left to right direction

actor "Moderador" as moderator

package "Moderar Solicitudes de Eventos" {
  usecase "Acceder al Panel Administrativo de Eventos" as access_panel
  usecase "Visualizar Solicitudes Pendientes" as view_requests
  usecase "Aprobar Solicitud" as approve_request
  usecase "Rechazar Solicitud" as reject_request
  usecase "Actualizar Estado y Notificar Vendedor" as update_notify

  note top of "Moderar Solicitudes de Eventos" : Precondición:\nDebe haber solicitudes pendientes enviadas por los vendedores.
}

moderator --> access_panel
access_panel --> view_requests

view_requests --> approve_request
view_requests --> reject_request

approve_request .> update_notify : <<includes>>
reject_request .> update_notify : <<includes>>

note right of update_notify : Postcondición:\nEl negocio queda inscrito en el evento o su participación es denegada.

@enduml
```