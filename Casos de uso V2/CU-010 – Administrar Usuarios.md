**Nombre:** Administrar Usuarios  
**ID:** CU-010  
**Descripción:** Permite al administrador gestionar usuarios del sistema.  
**Actor:** Administrador  

**Precondiciones:**

- Usuario con rol administrador.

**Flujo principal:**

1. El administrador accede al dashboard.
2. Selecciona la sección de usuarios.
3. El sistema muestra la lista.
4. El administrador puede editar o eliminar usuarios.

**Postcondiciones:**

- Cambios aplicados en usuarios.

**Excepciones:**

- Error al actualizar datos.


```plantuml
@startuml

actor Administrador
participant "Sistema" as Sistema
database "Base de Datos" as DB

Administrador -> Sistema: Accede al dashboard
activate Sistema
Administrador -> Sistema: Selecciona la sección de usuarios
Sistema -> DB: Solicita lista de usuarios
activate DB
DB --> Sistema: Envía lista de usuarios
deactivate DB
Sistema --> Administrador: Muestra la lista de usuarios
alt Editar usuario
    Administrador -> Sistema: Selecciona un usuario para editar
    Sistema --> Administrador: Muestra formulario con datos del usuario
    Administrador -> Sistema: Modifica datos del usuario
    Administrador -> Sistema: Confirma edición
    Sistema -> DB: Actualiza datos del usuario
    activate DB
    DB --> Sistema: Confirmación de actualización
    deactivate DB
    Sistema --> Administrador: Mensaje de usuario actualizado
else Eliminar usuario
    Administrador -> Sistema: Selecciona un usuario para eliminar
    Sistema --> Administrador: Pide confirmación de eliminación
    Administrador -> Sistema: Confirma eliminación
    Sistema -> DB: Elimina usuario
    activate DB
    DB --> Sistema: Confirmación de eliminación
    deactivate DB
    Sistema --> Administrador: Mensaje de usuario eliminado
end
deactivate Sistema

@enduml
```