**Nombre:** Eliminar Reseña  
**ID:** CU-017  
**Descripción:** Permite al usuario eliminar una reseña propia.  
**Actor:** Usuario  

**Precondiciones:**

- El usuario tiene reseñas.

**Flujo principal:**

1. El usuario selecciona eliminar reseña.
2. El sistema solicita confirmación.
3. El usuario confirma.
4. El sistema elimina la reseña.

**Postcondiciones:**

- Reseña eliminada.

**Excepciones:**

- N/A.

```plantuml
@startuml

actor Usuario
participant "Sistema" as Sistema
database "Base de Datos" as DB

Usuario -> Sistema: Selecciona eliminar reseña
activate Sistema
Sistema --> Usuario: Solicita confirmación de eliminación
Usuario -> Sistema: Confirma eliminación
Sistema -> DB: Elimina la reseña
activate DB
DB --> Sistema: Confirmación de eliminación
deactivate DB
Sistema --> Usuario: Mensaje de reseña eliminada exitosamente
deactivate Sistema

@enduml
```