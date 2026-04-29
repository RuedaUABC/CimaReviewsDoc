**Nombre:** Ver Mis Negocios  
**ID:** CU-019  
**Descripción:** Permite al vendedor visualizar sus negocios registrados.  
**Actor:** Vendedor  

**Precondiciones:**

- El vendedor tiene negocios registrados.

**Flujo principal:**

1. El vendedor accede a su perfil.
2. Selecciona “Mis negocios”.
3. El sistema muestra la lista.

**Postcondiciones:**

- Negocios visibles.

**Excepciones:**

- No hay negocios.

```plantuml
@startuml

actor Usuario
participant "Sistema" as Sistema
database "Base de Datos" as DB

Usuario -> Sistema: El usuario accede a su perfil
activate Sistema
Sistema --> Usuario: muestra informarcion de perfil
Usuario -> Sistema: Selecciona “Mis negocios”.
Sistema -> DB: solicita reseñas del usuario
activate DB
DB --> Sistema: envia negocios del usuario
deactivate DB
Sistema --> Usuario: muestra negocios del usuario
deactivate Sistema

@enduml
```
