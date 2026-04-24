**Nombre:** Editar Producto  
**ID:** CU-013  
**Descripción:** Permite al vendedor modificar un producto existente.  
**Actor:** Vendedor  

**Precondiciones:**

- El producto existe.

**Flujo principal:**

1. El vendedor selecciona un producto.
2. El sistema muestra los datos actuales.
3. El vendedor modifica la información.
4. Guarda los cambios.
5. El sistema actualiza el producto.

**Postcondiciones:**

- Producto actualizado.

**Excepciones:**

- N/A.

```plantuml
@startuml

actor Vendedor
participant "Sistema" as Sistema
database "Base de Datos" as DB

Vendedor -> Sistema: Selecciona un producto para editar
activate Sistema
Sistema --> Vendedor: Muestra los datos actuales del producto
Vendedor -> Sistema: Modifica la información del producto
Vendedor -> Sistema: Guarda los cambios
Sistema -> DB: Actualiza el producto en la base de datos
activate DB
DB --> Sistema: Confirmación de actualización
deactivate DB
Sistema --> Vendedor: Mensaje de producto actualizado exitosamente
deactivate Sistema

@enduml
```