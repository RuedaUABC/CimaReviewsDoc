**Nombre:** Ver Mis Reseñas  
**ID:** CU-018  
**Descripción:** Permite al usuario visualizar sus reseñas.  
**Actor:** Usuario  

**Precondiciones:**

- Usuario autenticado.

**Flujo principal:**

1. El usuario accede a su perfil.
2. Selecciona “Mis reseñas”.
3. El sistema muestra la lista.

**Postcondiciones:**

- Reseñas visibles.

**Excepciones:**

- No hay reseñas.

```plantuml 
@startuml

actor Usuario
participant "Sistema" as Sistema
database "Base de Datos" as DB

Usuario -> Sistema: El usuario accede a su perfil
activate Sistema
Sistema --> Usuario: muestra informarcion de perfil
Usuario -> Sistema: Selecciona “Mis reseñas”.
Sistema -> DB: solicita reseñas del usuario
activate DB
DB --> Sistema: envia reseñas del usuario
deactivate DB
Sistema --> Usuario: muestra reseñas del usuario
deactivate Sistema

@enduml
```
