**Nombre:** Ver Menú  
**ID:** CU-011  
**Descripción:** Permite al usuario visualizar el menú de un negocio.  
**Actor:** Usuario  

**Precondiciones:**

- El usuario ha iniciado sesión.
- El negocio tiene productos registrados.

**Flujo principal:**

1. El usuario accede a un negocio.
2. El sistema muestra la lista de productos.
3. El usuario navega por las categorías y productos.

**Postcondiciones:**

- El usuario visualiza el menú del negocio.

**Excepciones:**

- No hay productos disponibles.


```plantuml
@startuml

actor Usuario
participant "Sistema" as Sistema
database "Base de Datos" as DB

Usuario -> Sistema: Accede a un negocio
activate Sistema
Sistema -> DB: Solicita la lista de productos del negocio
activate DB
alt Negocio tiene productos registrados
    DB --> Sistema: Envía lista de productos y categorías
    deactivate DB
    Sistema --> Usuario: Muestra la lista de productos (menú)
    Usuario <-> Sistema: Navega por categorías y productos
else No hay productos disponibles
    DB --> Sistema: No se encontraron productos
    deactivate DB
    Sistema --> Usuario: Muestra mensaje "No hay productos disponibles"
end
deactivate Sistema

@enduml
```