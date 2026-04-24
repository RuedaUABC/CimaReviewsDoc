**Nombre:** Eliminar Producto  
**ID:** CU-014  
**Descripción:** Permite al vendedor eliminar un producto del menú.  
**Actor:** Vendedor  

**Precondiciones:**

- El producto existe.

**Flujo principal:**

1. El vendedor selecciona eliminar producto.
2. El sistema solicita confirmación.
3. El vendedor confirma.
4. El sistema elimina el producto.

**Postcondiciones:**

- Producto eliminado del sistema.

**Excepciones:**

- N/A.

```plantuml
@startuml

actor Vendedor
participant "Sistema" as Sistema
database "Base de Datos" as DB

Vendedor -> Sistema: 1. Selecciona eliminar producto
activate Sistema
Sistema --> Vendedor: 2. Solicita confirmación
Vendedor -> Sistema: 3. Confirma eliminación
Sistema -> DB: 4. Elimina el producto
activate DB
DB --> Sistema: Confirmación de eliminación
deactivate DB
Sistema --> Vendedor: Mensaje de producto eliminado exitosamente
deactivate Sistema

@enduml
```