**Nombre:** Agregar Categoría  
**ID:** CU-015  
**Descripción:** Permite al vendedor agregar o seleccionar categorías para su menú.  
**Actor:** Vendedor  

**Precondiciones:**

- El vendedor tiene un negocio.

**Flujo principal:**

1. El vendedor accede a “Agregar categoría”.
2. El sistema muestra categorías existentes.
3. El vendedor selecciona una categoría.
4. Confirma la selección.
5. El sistema agrega las categorías al menú.

**Postcondiciones:**

- Categorías asociadas al negocio.

**Excepciones:**

- Opcionalmente crea una nueva categoría personalizada.

```plantuml
@startuml

actor Vendedor
participant "Sistema" as Sistema
database "Base de Datos" as DB

Vendedor -> Sistema: Accede a "Agregar categoría"
activate Sistema
Sistema -> DB: Solicita categorías existentes
activate DB
DB --> Sistema: Envía lista de categorías
deactivate DB
Sistema --> Vendedor: Muestra categorías existentes
alt Selecciona categoría existente
    Vendedor -> Sistema: Selecciona una categoría
    Vendedor -> Sistema: Confirma la selección
    Sistema -> DB: Asocia categoría al menú del negocio
    activate DB
    DB --> Sistema: Confirmación de asociación
    deactivate DB
    Sistema --> Vendedor: Mensaje de categoría agregada
else Crea nueva categoría personalizada
    Vendedor -> Sistema: Selecciona opción "Crear nueva categoría"
    Sistema --> Vendedor: Muestra formulario para nueva categoría
    Vendedor -> Sistema: Ingresa nombre de la nueva categoría
    Vendedor -> Sistema: Confirma creación
    Sistema -> DB: Guarda nueva categoría y la asocia al menú
    activate DB
    DB --> Sistema: Confirmación de creación y asociación
    deactivate DB
    Sistema --> Vendedor: Mensaje de nueva categoría creada y agregada
end
deactivate Sistema

@enduml
```