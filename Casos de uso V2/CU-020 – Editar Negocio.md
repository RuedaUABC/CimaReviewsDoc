**Nombre:** Editar Negocio  
**ID:** CU-020  
**Descripción:** Permite al vendedor modificar la información de su negocio.  
**Actor:** Vendedor  
**Relación:** Incluye: Ver Mis Negocios

**Precondiciones:**

- El negocio pertenece al vendedor.

**Flujo principal:**

1. El vendedor selecciona un negocio.
2. Modifica los datos.
3. Guarda cambios.
4. El sistema actualiza el negocio.

**Postcondiciones:**

- Negocio actualizado.

**Excepciones:**

-  N/A

```plantuml
@startuml

actor Usuario
participant "Sistema" as Sistema
database "Base de Datos" as DB

Usuario -> Sistema: Accede a "Mis negocios"
activate Sistema
Sistema -> DB: Solicita negocios del usuario
activate DB
DB --> Sistema: Envía lista de negocios
deactivate DB
Sistema --> Usuario: Muestra lista de negocios
Usuario -> Sistema: Selecciona una negocio para editar
Sistema --> Usuario: Muestra el contenido actual de la negocio
Usuario -> Sistema: Modifica el contenido (nombre, descripcion)
Usuario -> Sistema: Guarda los cambios
Sistema -> DB: Actualiza la negocio en la base de datos
activate DB
DB --> Sistema: Confirmación de actualización
deactivate DB
Sistema --> Usuario: Mensaje de negocio actualizada exitosamente
deactivate Sistema

@enduml
```
