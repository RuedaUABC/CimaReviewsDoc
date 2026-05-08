**Nombre:** Administrar Reportes  
**ID:** CU-023  
**Descripción:** Permite al administrador gestionar reportes.  
**Actor:** Administrador  

**Precondiciones:**

- Usuario administrador.

**Flujo principal:**

1. Selecciona un reporte.
2. Analiza información.
3. Decide acción:
    - Eliminar contenido
    - Banear usuario
4. Ejecuta acción.

**Postcondiciones:**

- Acción aplicada.

**Excepciones:**

- N/A.

```plantuml
@startuml

actor Administrador
participant "Sistema" as Sistema
database "Base de Datos" as DB

Administrador -> Sistema: 1. Seleccionar un reporte
activate Sistema
Sistema --> Administrador: 2. Mostrar información del reporte
deactivate Sistema

Administrador -> Sistema: 3. Analizar información
activate Sistema
Sistema --> Administrador: 4. Información analizada (no aplica acción directa)
deactivate Sistema

Administrador -> Sistema: 5. Decidir acción\na) Eliminar contenido\nb) Banear usuario
activate Sistema

alt Acción = Eliminar contenido
    Administrador -> Sistema: 6a. Ejecutar eliminación de contenido
    activate Sistema
    Sistema -> DB: 7a. Eliminar contenido reportado
    activate DB
    DB --> Sistema: 8a. Contenido eliminado
    deactivate DB
    Sistema --> Administrador: 9a. Confirmar eliminación
    deactivate Sistema
else Acción = Banear usuario
    Administrador -> Sistema: 6b. Ejecutar baneo de usuario
    activate Sistema
    Sistema -> DB: 7b. Banear usuario (actualizar estado)
    activate DB
    DB --> Sistema: 8b. Usuario baneado
    deactivate DB
    Sistema --> Administrador: 9b. Confirmar baneo
    deactivate Sistema
end

deactivate Sistema

@enduml
```
