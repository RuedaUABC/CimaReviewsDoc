**Nombre:** Ver Reportes  
**ID:** CU-022  
**Descripción:** Permite al administrador visualizar reportes.  
**Actor:** Administrador  

**Precondiciones:**

- Usuario administrador.

**Flujo principal:**

1. Accede al dashboard.
2. Selecciona reportes.
3. El sistema muestra la lista.

**Postcondiciones:**

- Reportes visibles.

**Excepciones:**

- No hay reportes.

```plantuml
@startuml

actor Administrador
participant "Sistema" as Sistema
database "Base de Datos" as DB

Administrador -> Sistema: 1. Acceder al dashboard
activate Sistema
Sistema --> Administrador: 2. Mostrar dashboard
deactivate Sistema

Administrador -> Sistema: 3. Seleccionar reportes
activate Sistema

Sistema -> DB: 4. Solicitar lista de reportes
activate DB
DB --> Sistema: 5. Retornar reportes (o vacío)
deactivate DB

alt Existe al menos un reporte
    Sistema --> Administrador: 6. Mostrar lista de reportes
else No hay reportes
    Sistema --> Administrador: 6. Mostrar mensaje "No hay reportes disponibles"
end

deactivate Sistema

@enduml
```
