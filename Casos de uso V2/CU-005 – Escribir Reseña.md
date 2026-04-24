**Nombre:** Escribir Reseña  
**ID:** CU-005  
**Descripción:** Permite al usuario crear una reseña para un negocio.  
**Actor:** Usuario  

**Precondiciones:**

- El usuario ha iniciado sesión.
- El usuario se encuentra en un negocio.

**Flujo principal:**

1. El usuario selecciona “Escribir reseña”.
2. El sistema muestra el formulario.
3. El usuario ingresa:
    - Calificación
    - Comentario
4. El usuario envía la reseña.
5. El sistema guarda la reseña.

**Postcondiciones:**

- La reseña queda registrada.

**Excepciones:**

- N/A.



```plantuml
@startuml
autonumber

actor Usuario
participant "Sistema" as Sistema
database "Base de Datos" as DB

Usuario -> Sistema: 1. Selecciona "Escribir reseña"
activate Sistema
Sistema --> Usuario: 2. Muestra formulario de reseña
Usuario -> Sistema: 3. Ingresa Calificación y Comentario
Usuario -> Sistema: 4. Envía la reseña
Sistema -> DB: 5. Guarda la reseña (Calificación, Comentario, ID_Usuario, ID_Negocio)
activate DB
DB --> Sistema: Confirmación de guardado
deactivate DB
Sistema --> Usuario: Mensaje de reseña guardada exitosamente
deactivate Sistema

@enduml
```