**Nombre:** Ver Eventos  
**ID:** CU-008  
**Descripción:** Permite al usuario visualizar eventos disponibles.  
**Actor:** Usuario  
**Relación:** N/A

**Precondiciones:**

- Usuario autenticado.

**Flujo principal:**

1. El usuario accede a la sección de eventos.
2. El sistema muestra la lista de eventos.
3. El usuario selecciona un evento.

**Postcondiciones:**

- El usuario visualiza eventos disponibles.

**Excepciones:**

- No hay eventos.



```plantuml
@startuml

actor Usuario
participant "Sistema" as Sistema
database "Base de Datos" as DB

Usuario -> Sistema: Accede a la sección de eventos
activate Sistema
Sistema -> DB: Solicita lista de eventos disponibles
activate DB
alt Hay eventos
    DB --> Sistema: Envía lista de eventos
    deactivate DB
    Sistema --> Usuario: Muestra la lista de eventos
    Usuario -> Sistema: Selecciona un evento
else No hay eventos
    DB --> Sistema: No se encontraron eventos
    deactivate DB
    Sistema --> Usuario: Muestra mensaje "No hay eventos disponibles"
end
deactivate Sistema

@enduml
```