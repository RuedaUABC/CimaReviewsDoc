**Nombre:** Ver Mapa  
**ID:** CU-009  
**Descripción:** Permite al usuario visualizar la ubicación de negocios o eventos en un mapa.  
**Actor:** Usuario  

**Precondiciones:**

- Usuario autenticado.

**Flujo principal:**

1. El usuario selecciona “Ver ubicación”.
2. El sistema abre el mapa.
3. El sistema muestra la ubicación con un marcador.
4. El usuario puede interactuar con el mapa.

**Postcondiciones:**

- Ubicación visualizada.

**Excepciones:**

- N/A.


```plantuml
@startuml

actor Usuario
participant "Sistema" as Sistema
database "Base de Datos" as DB

Usuario -> Sistema: Selecciona "Ver ubicación"
activate Sistema
Sistema -> DB: Solicita datos de ubicación (negocios/eventos)
activate DB
DB --> Sistema: Envía datos de ubicación
deactivate DB
Sistema --> Usuario: Abre el mapa y muestra ubicación con marcador
Usuario <-> Sistema: Interactúa con el mapa (zoom, mover, etc.)
deactivate Sistema

@enduml
```