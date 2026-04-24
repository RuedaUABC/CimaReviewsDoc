**Nombre:** Gestionar Menú  
**ID:** CU-007  
**Descripción:** Permite al vendedor administrar los productos de su negocio.  
**Actor:** Vendedor  

**Precondiciones:**

- El vendedor posee al menos un negocio.

**Flujo principal:**

1. El vendedor accede a uno de sus negocios.
2. Selecciona “Gestionar menú”.
3. El sistema muestra los productos.
4. El vendedor puede:
    - Agregar producto
    - Editar producto
    - Eliminar producto

**Postcondiciones:**

- El menú queda actualizado.

**Excepciones:**

- N/A.



```plantuml
@startuml

actor Vendedor
participant "Sistema" as Sistema
database "Base de Datos" as DB

Vendedor -> Sistema: Accede a uno de sus negocios
activate Sistema
Vendedor -> Sistema: Selecciona "Gestionar menú"
Sistema --> Vendedor: Muestra los productos del negocio
alt Agregar producto
    Vendedor -> Sistema: Selecciona "Agregar producto"
    Sistema --> Vendedor: Muestra formulario para nuevo producto
    Vendedor -> Sistema: Ingresa detalles del producto
    Vendedor -> Sistema: Confirma adición
    Sistema -> DB: Guarda nuevo producto
    activate DB
    DB --> Sistema: Confirmación de guardado
    deactivate DB
    Sistema --> Vendedor: Mensaje de producto agregado
else Editar producto
    Vendedor -> Sistema: Selecciona un producto para editar
    Sistema --> Vendedor: Muestra formulario con datos del producto
    Vendedor -> Sistema: Modifica detalles del producto
    Vendedor -> Sistema: Confirma edición
    Sistema -> DB: Actualiza producto existente
    activate DB
    DB --> Sistema: Confirmación de actualización
    deactivate DB
    Sistema --> Vendedor: Mensaje de producto actualizado
else Eliminar producto
    Vendedor -> Sistema: Selecciona un producto para eliminar
    Sistema --> Vendedor: Pide confirmación de eliminación
    Vendedor -> Sistema: Confirma eliminación
    Sistema -> DB: Elimina producto
    activate DB
    DB --> Sistema: Confirmación de eliminación
    deactivate DB
    Sistema --> Vendedor: Mensaje de producto eliminado
end
deactivate Sistema

@enduml
```