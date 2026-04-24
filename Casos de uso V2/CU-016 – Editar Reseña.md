**Nombre:** Editar Reseña  
**ID:** CU-016  
**Descripción:** Permite al usuario modificar una reseña propia.  
**Actor:** Usuario  

**Precondiciones:**

- El usuario ha creado una reseña.

**Flujo principal:**

1. El usuario accede a “Mis reseñas”.
2. Selecciona una reseña.
3. Modifica el contenido.
4. Guarda los cambios.
5. El sistema actualiza la reseña.

**Postcondiciones:**

- Reseña actualizada.

**Excepciones:**

- N/A.
```plantuml
@startuml

actor Usuario
participant "Sistema" as Sistema
database "Base de Datos" as DB

Usuario -> Sistema: Accede a "Mis reseñas"
activate Sistema
Sistema -> DB: Solicita reseñas del usuario
activate DB
DB --> Sistema: Envía lista de reseñas
deactivate DB
Sistema --> Usuario: Muestra lista de reseñas
Usuario -> Sistema: Selecciona una reseña para editar
Sistema --> Usuario: Muestra el contenido actual de la reseña
Usuario -> Sistema: Modifica el contenido (calificación, comentario)
Usuario -> Sistema: Guarda los cambios
Sistema -> DB: Actualiza la reseña en la base de datos
activate DB
DB --> Sistema: Confirmación de actualización
deactivate DB
Sistema --> Usuario: Mensaje de reseña actualizada exitosamente
deactivate Sistema

@enduml
```