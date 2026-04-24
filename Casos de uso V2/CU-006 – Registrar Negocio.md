**Nombre:** Registrar Negocio  
**ID:** CU-006  
**Descripción:** Permite al vendedor registrar un nuevo negocio en el sistema.  
**Actor:** Vendedor  

**Precondiciones:**

- El usuario debe tener rol de vendedor.

**Flujo principal:**

1. El vendedor accede a “Registrar negocio”.
2. El sistema muestra el formulario.
3. El vendedor ingresa:
    - Nombre
    - Descripción
    - Ubicación
    - Imagen
4. El vendedor confirma.
5. El sistema registra el negocio.

**Postcondiciones:**

- El negocio queda registrado y asociado al vendedor.

**Excepciones:**

- Datos incompletos.



```plantuml
@startuml
autonumber

actor Vendedor
participant "Sistema" as Sistema
database "Base de Datos" as DB

Vendedor -> Sistema: 1. Accede a "Registrar negocio"
activate Sistema
Sistema --> Vendedor: 2. Muestra el formulario
Vendedor -> Sistema: 3. Ingresa Nombre, Descripción, Ubicación, Imagen
Vendedor -> Sistema: 4. Confirma
Sistema -> DB: 5. Registra el negocio (Nombre, Descripción, Ubicación, Imagen, ID_Vendedor)
activate DB
DB --> Sistema: Confirmación de registro
deactivate DB
Sistema --> Vendedor: Mensaje de negocio registrado exitosamente
deactivate Sistema

@enduml
```