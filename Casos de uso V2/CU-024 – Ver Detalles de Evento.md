**Nombre:** Ver Detalles de Evento  
**ID:** CU-024  
**Descripción:** Permite visualizar información completa de un evento.  
**Actor:** Usuario  

**Precondiciones:**

- Evento existe.

**Flujo principal:**

1. Usuario selecciona evento.
2. Sistema muestra:
    - Información
    - Participantes
    - Ubicación

**Postcondiciones:**

- Evento visualizado.

**Excepciones:**

- N/A.

```plantuml
@startuml

actor Usuario
participant "Sistema" as Sistema
database "Base de Datos" as DB

Usuario -> Sistema: 1. Seleccionar evento
activate Sistema

Sistema -> DB: 2. Solicitar información completa del evento
activate DB
DB --> Sistema: 3. Retornar información del evento
deactivate DB

Sistema -> DB: 4. Solicitar lista de participantes
activate DB
DB --> Sistema: 5. Retornar participantes
deactivate DB

Sistema -> DB: 6. Solicitar ubicación del evento
activate DB
DB --> Sistema: 7. Retornar ubicación
deactivate DB

Sistema --> Usuario: 8. Mostrar detalles completos:\n- Información\n- Participantes\n- Ubicación
deactivate Sistema

@enduml
```
