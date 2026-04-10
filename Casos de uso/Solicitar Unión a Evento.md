---
id: CU-012
actores_primarios: "Vendedor"
actores_secundarios: "Moderador"
tipo: caso_de_uso
---

# Solicitar Unión a Evento

## Descripción
Permite a los negocios solicitar unirse a un evento universitario activo (RF-038).

## Condiciones
**Precondiciones:**
Debe existir un evento activo. El vendedor debe tener un negocio registrado.

**Postcondiciones:**
Se genera una solicitud en estado pendiente de aprobación.

## Flujo Principal
1.- El vendedor consulta los eventos activos.
2.- Selecciona un evento y presiona solicitar participación.
3.- El sistema genera la petición y la envía al panel de moderación.

## Flujos Alternativos
El evento ya cerró sus inscripciones.
El negocio ya había enviado una solicitud.

# UML
```plantuml
@startuml
left to right direction

actor "Vendedor" as seller
actor "Moderador" as moderator

package "Solicitar Unión a Evento" {
  usecase "Consultar Eventos Activos" as consult_events
  usecase "Seleccionar Evento y Solicitar Participación" as select_request_participation
  usecase "Generar Petición y Enviar a Moderación" as generate_send_request

  note top of "Solicitar Unión a Evento" : Precondiciones:\n- Debe existir un evento activo.\n- El vendedor debe tener un negocio registrado.
}

seller --> consult_events
consult_events --> select_request_participation

select_request_participation .> generate_send_request : <<includes>>

generate_send_request --> moderator : Notifica

note right of select_request_participation : Flujos Alternativos:\n- El evento ya cerró sus inscripciones.\n- El negocio ya había enviado una solicitud.
note right of generate_send_request : Postcondición:\nSe genera una solicitud en estado pendiente de aprobación.

@enduml
```