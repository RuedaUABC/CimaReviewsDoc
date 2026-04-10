---
epoch: 1775754418468
modelKey: "gemini-2.5-flash|google"
topic: "Diagrama de Caso de Uso PlantUML"



tags:
  - copilot-conversation
---

**user**: podrias implementar un diagrama de caso de uso del  de esta nota mediante PlantUML
[Context: Notes: Casos de uso/Buscar y Ordenar Negocios.md]
[Timestamp: 2026/04/09 10:06:58]

**ai**: 
<errorChunk>Model request failed: API key is not provided for the model: google/gemini-2.5-flash|openrouterai.</errorChunk>
[Timestamp: 2026/04/09 10:06:58]

**user**: podrias implementar un diagrama de caso de uso del  de esta nota mediante PlantUML
[Context: Notes: Casos de uso/Buscar y Ordenar Negocios.md]
[Timestamp: 2026/04/09 10:07:20]

**ai**: Claro, aquí tienes un diagrama de caso de uso en PlantUML basado en la nota [[Buscar y Ordenar Negocios]]:

```plantuml
@startuml
left to right direction

actor "Usuario" as user

rectangle "Sistema" {
  usecase "Buscar y Ordenar Negocios" as search_sort
}

user --> search_sort

@enduml
```

**Explicación:**

- `actor "Usuario" as user`: Define al actor principal "Usuario".
- `rectangle "Sistema"`: Agrupa el caso de uso dentro de un subsistema llamado "Sistema".
- `usecase "Buscar y Ordenar Negocios" as search_sort`: Define el caso de uso principal.
- `user --> search_sort`: Muestra la relación de que el "Usuario" inicia o participa en el caso de uso "Buscar y Ordenar Negocios".
[Timestamp: 2026/04/09 10:07:23]

**user**: necesito que el diagrama sea mas detallado al  contenido del caso de uso en cuestion
[Context: Notes: Casos de uso/Buscar y Ordenar Negocios.md]
[Timestamp: 2026/04/09 10:08:55]

**ai**: ¡Claro! Para hacer el diagrama más detallado, podemos desglosar el caso de uso principal en las acciones específicas que el usuario puede realizar, tal como se describe en la nota.

Aquí tienes un diagrama de caso de uso en PlantUML que refleja el contenido de la nota [[Buscar y Ordenar Negocios]] con más detalle:

```plantuml
@startuml
left to right direction

actor "Usuario" as user

package "Buscar y Ordenar Negocios" {
  usecase "Buscar Negocio por Nombre" as search_name
  usecase "Ordenar Negocios por Calificación" as sort_rating
  usecase "Mostrar Lista de Negocios" as show_list

  note top of "Buscar y Ordenar Negocios" : Precondición:\nSistema debe tener negocios registrados.
}

user --> search_name
user --> sort_rating

search_name .> show_list : <<includes>>
sort_rating .> show_list : <<includes>>

' Notas para flujos alternativos y postcondiciones
note right of search_name : Flujo Alternativo:\nNo se encuentran negocios.
note right of show_list : Postcondición:\nUsuario visualiza resultados esperados.

@enduml
```

**Explicación de los detalles:**

-   **`package "Buscar y Ordenar Negocios"`**: Agrupa los casos de uso relacionados bajo el nombre del caso de uso principal de la nota, indicando que estas acciones forman parte de esa funcionalidad general.
-   **`actor "Usuario" as user`**: El actor principal.
-   **`usecase "Buscar Negocio por Nombre" as search_name`**: Representa la acción de buscar un negocio por su nombre, como se menciona en la descripción y el flujo principal.
-   **`usecase "Ordenar Negocios por Calificación" as sort_rating`**: Representa la acción de ordenar los negocios por calificación, también mencionada en la descripción y el flujo principal.
-   **`usecase "Mostrar Lista de Negocios" as show_list`**: Este caso de uso es incluido por las dos acciones anteriores, ya que el resultado de buscar o ordenar es siempre mostrar una lista de negocios.
-   **`user --> search_name`** y **`user --> sort_rating`**: Muestran que el "Usuario" puede iniciar directamente cualquiera de estas dos acciones.
-   **`search_name .> show_list : <<includes>>`** y **`sort_rating .> show_list : <<includes>>`**: Indican que, una vez que el usuario busca por nombre u ordena por calificación, el sistema *incluye* la acción de "Mostrar Lista de Negocios" como parte de su proceso.
-   **`note top of "Buscar y Ordenar Negocios" : Precondición:\nSistema debe tener negocios registrados.`**: Añade la precondición del caso de uso.
-   **`note right of search_name : Flujo Alternativo:\nNo se encuentran negocios.`**: Detalla el flujo alternativo específico para la búsqueda.
-   **`note right of show_list : Postcondición:\nUsuario visualiza resultados esperados.`**: Añade la postcondición del caso de uso.

Este diagrama proporciona una vista más granular de las interacciones y resultados descritos en tu nota.
[Timestamp: 2026/04/09 10:09:25]

**user**: aplica las mismas instrucciones a la nota actual
[Context: Notes: Casos de uso/Calificar Negocio.md]
[Timestamp: 2026/04/09 10:11:27]

**ai**: ¡Por supuesto! Aquí tienes un diagrama de caso de uso en PlantUML basado en la nota [[Calificar Negocio]], con un nivel de detalle similar al anterior:

```plantuml
@startuml
left to right direction

actor "Usuario registrado" as registered_user

package "Calificar Negocio" {
  usecase "Ingresar al Perfil del Negocio" as view_profile
  usecase "Seleccionar Opción de Calificar" as select_rate_option
  usecase "Asignar Calificación (1-5 estrellas)" as assign_rating
  usecase "Confirmar Calificación" as confirm_rating
  usecase "Registrar y Promediar Calificación" as update_rating_system

  note top of "Calificar Negocio" : Precondiciones:\n- Usuario debe haber iniciado sesión.\n- Negocio debe existir en el catálogo.
}

registered_user --> view_profile
view_profile --> select_rate_option
select_rate_option --> assign_rating
assign_rating --> confirm_rating

confirm_rating .> update_rating_system : <<includes>>

' Notas para flujos alternativos y postcondiciones
note right of confirm_rating : Flujo Alternativo:\n- Usuario cancela la acción.\n- Usuario ya había calificado (se actualiza su calificación anterior).
note right of update_rating_system : Postcondición:\nLa calificación general del negocio se actualiza en el sistema.

@enduml
```

**Explicación de los detalles:**

-   **`actor "Usuario registrado" as registered_user`**: Define al actor principal, "Usuario registrado", como se especifica en la nota.
-   **`package "Calificar Negocio"`**: Agrupa todos los casos de uso relacionados bajo el nombre del caso de uso principal.
-   **`usecase "Ingresar al Perfil del Negocio" as view_profile`**: Representa el primer paso del flujo principal.
-   **`usecase "Seleccionar Opción de Calificar" as select_rate_option`**: Representa el segundo paso.
-   **`usecase "Asignar Calificación (1-5 estrellas)" as assign_rating`**: Representa la acción clave del usuario de elegir la calificación.
-   **`usecase "Confirmar Calificación" as confirm_rating`**: Representa la acción final del usuario para enviar su calificación.
-   **`usecase "Registrar y Promediar Calificación" as update_rating_system`**: Representa la acción del sistema que se ejecuta después de que el usuario confirma la calificación.
-   **`registered_user --> view_profile`**: Muestra que el "Usuario registrado" inicia el proceso ingresando al perfil.
-   Las flechas subsiguientes (`view_profile --> select_rate_option`, etc.) muestran la secuencia del flujo principal.
-   **`confirm_rating .> update_rating_system : <<includes>>`**: Indica que el caso de uso "Registrar y Promediar Calificación" es *incluido* por "Confirmar Calificación", ya que es una acción interna del sistema que ocurre como resultado de la confirmación.
-   **`note top of "Calificar Negocio" : Precondiciones:\n- Usuario debe haber iniciado sesión.\n- Negocio debe existir en el catálogo.`**: Añade las precondiciones del caso de uso.
-   **`note right of confirm_rating : Flujo Alternativo:\n- Usuario cancela la acción.\n- Usuario ya había calificado (se actualiza su calificación anterior).`**: Detalla los flujos alternativos.
-   **`note right of update_rating_system : Postcondición:\nLa calificación general del negocio se actualiza en el sistema.`**: Añade la postcondición del caso de uso.

Este diagrama visualiza de manera clara las interacciones del usuario y las respuestas del sistema, junto con las condiciones y flujos alternativos descritos en tu nota.
[Timestamp: 2026/04/09 10:11:36]

**user**: limitate a darme meramente el diagrama de este en cuestion
[Context: Notes: Casos de uso/Consultar Eventos.md]
[Timestamp: 2026/04/09 10:13:08]

**ai**: ```plantuml
@startuml
left to right direction

actor "Usuario" as user

package "Consultar Eventos" {
  usecase "Ingresar a Sección de Eventos" as enter_section
  usecase "Consultar Eventos Vigentes" as query_events
  usecase "Mostrar Lista/Calendario de Eventos Activos" as display_events

  note top of "Consultar Eventos" : Precondiciones:\nN/A
}

user --> enter_section
enter_section --> query_events
query_events .> display_events : <<includes>>

note right of display_events : Flujo Alternativo:\nNo hay eventos activos.
note right of display_events : Postcondición:\nEl usuario visualiza la información de los eventos.

@enduml
```
[Timestamp: 2026/04/09 10:13:11]

**user**: hazlo de nuevo con este
[Context: Notes: Casos de uso/Gestionar Negocio.md]
[Timestamp: 2026/04/09 10:13:52]

**ai**: ```plantuml
@startuml
left to right direction

actor "Vendedor" as seller

package "Gestionar Negocio" {
  usecase "Acceder al Panel de Mis Negocios" as access_panel
  usecase "Seleccionar Negocio" as select_business
  usecase "Editar Información del Negocio" as edit_info
  usecase "Eliminar Negocio" as delete_business
  usecase "Aplicar Cambios al Negocio" as apply_changes

  note top of "Gestionar Negocio" : Precondición:\nEl vendedor debe ser el creador/propietario del negocio en el sistema.
}

seller --> access_panel
access_panel --> select_business

select_business --> edit_info
select_business --> delete_business

edit_info .> apply_changes : <<includes>>
delete_business .> apply_changes : <<includes>>

note right of edit_info : Flujo Alternativo:\nEl vendedor cancela la acción.
note right of delete_business : Flujo Alternativo:\nEl vendedor cancela la acción.
note right of apply_changes : Postcondición:\nLa información del negocio se actualiza o este deja de estar disponible en el sistema.

@enduml
```
[Timestamp: 2026/04/09 10:13:55]

**user**: hazlo de nuevo con este
[Context: Notes: Casos de uso/Gestionar Reseña y Calificación.md]
[Timestamp: 2026/04/09 10:14:22]

**ai**: ```plantuml
@startuml
left to right direction

actor "Usuario registrado" as registered_user

package "Gestionar Reseña y Calificación" {
  usecase "Acceder a Historial o Perfil del Negocio" as access_history_profile
  usecase "Seleccionar Reseña/Calificación" as select_review_rating
  usecase "Editar Reseña/Calificación" as edit_review_rating
  usecase "Eliminar Reseña/Calificación" as delete_review_rating
  usecase "Actualizar Base de Datos" as update_database

  note top of "Gestionar Reseña y Calificación" : Precondición:\nEl usuario debe tener al menos una reseña o calificación previamente publicada.
}

registered_user --> access_history_profile
access_history_profile --> select_review_rating

select_review_rating --> edit_review_rating
select_review_rating --> delete_review_rating

edit_review_rating .> update_database : <<includes>>
delete_review_rating .> update_database : <<includes>>

note right of edit_review_rating : Flujo Alternativo:\nEl usuario cancela la edición.
note right of delete_review_rating : Flujo Alternativo:\nEl usuario cancela la eliminación.
note right of update_database : Postcondición:\nLa reseña o calificación es modificada o eliminada permanentemente.

@enduml
```
[Timestamp: 2026/04/09 10:14:28]

**user**: hazlo de nuevo con este
[Context: Notes: Casos de uso/Inicio de Sesion.md]
[Timestamp: 2026/04/09 10:15:07]

**ai**: ```plantuml
@startuml
left to right direction

actor "Usuario registrado" as registered_user

package "Inicio de Sesión" {
  usecase "Seleccionar Opción de Iniciar Sesión" as select_login_option
  usecase "Mostrar Formulario de Inicio de Sesión" as show_login_form
  usecase "Ingresar Credenciales (Correo y Contraseña)" as enter_credentials
  usecase "Presionar Botón de Confirmar" as confirm_button
  usecase "Validar Credenciales" as validate_credentials
  usecase "Redirigir a Página Principal" as redirect_to_home

  note top of "Inicio de Sesión" : Precondición:\nEl usuario debe estar registrado en el sistema.
}

registered_user --> select_login_option
select_login_option --> show_login_form
show_login_form --> enter_credentials
enter_credentials --> confirm_button

confirm_button .> validate_credentials : <<includes>>
validate_credentials .> redirect_to_home : <<extends>>

note right of validate_credentials : Flujos Alternativos:\n- Credenciales incorrectas.\n- El usuario no existe.
note right of redirect_to_home : Postcondición:\nEl usuario obtiene acceso a su cuenta con una sesión activa.

@enduml
```
[Timestamp: 2026/04/09 10:15:10]

**user**: hazlo
[Context: Notes: Casos de uso/Moderar Solicitudes de Eventos.md]
[Timestamp: 2026/04/09 10:16:13]

**ai**: ```plantuml
@startuml
left to right direction

actor "Moderador" as moderator

package "Moderar Solicitudes de Eventos" {
  usecase "Acceder al Panel Administrativo de Eventos" as access_panel
  usecase "Visualizar Solicitudes Pendientes" as view_requests
  usecase "Aprobar Solicitud" as approve_request
  usecase "Rechazar Solicitud" as reject_request
  usecase "Actualizar Estado y Notificar Vendedor" as update_notify

  note top of "Moderar Solicitudes de Eventos" : Precondición:\nDebe haber solicitudes pendientes enviadas por los vendedores.
}

moderator --> access_panel
access_panel --> view_requests

view_requests --> approve_request
view_requests --> reject_request

approve_request .> update_notify : <<includes>>
reject_request .> update_notify : <<includes>>

note right of update_notify : Postcondición:\nEl negocio queda inscrito en el evento o su participación es denegada.

@enduml
```
[Timestamp: 2026/04/09 10:16:20]

**user**: hazlo
[Context: Notes: Casos de uso/Publicar Reseña.md]
[Timestamp: 2026/04/09 10:17:02]

**ai**: ```plantuml
@startuml
left to right direction

actor "Usuario registrado" as registered_user

package "Publicar Reseña" {
  usecase "Ingresar al Perfil del Negocio" as enter_business_profile
  usecase "Seleccionar Opción de Escribir Reseña" as select_write_review
  usecase "Redactar Reseña" as write_review
  usecase "Presionar Enviar" as press_send
  usecase "Guardar y Publicar Reseña" as save_publish_review

  note top of "Publicar Reseña" : Precondición:\nEl usuario debe haber iniciado sesión.
}

registered_user --> enter_business_profile
enter_business_profile --> select_write_review
select_write_review --> write_review
write_review --> press_send

press_send .> save_publish_review : <<includes>>

note right of write_review : Flujo Alternativo:\nEl texto excede el límite de caracteres (RE-003).
note right of press_send : Flujo Alternativo:\nEl usuario cancela la publicación.
note right of save_publish_review : Postcondición:\nLa reseña es visible públicamente en el perfil del negocio.

@enduml
```
[Timestamp: 2026/04/09 10:17:05]

**user**: haz
[Context: Notes: Casos de uso/Registrar Negocio.md]
[Timestamp: 2026/04/09 10:18:51]

**ai**: ```plantuml
@startuml
left to right direction

actor "Vendedor" as seller

package "Registrar Negocio" {
  usecase "Seleccionar Opción de Agregar Negocio" as select_add_option
  usecase "Mostrar Formulario de Registro" as show_form
  usecase "Ingresar Información del Negocio" as enter_info
  usecase "Guardar Datos" as save_data
  usecase "Registrar Negocio en Base de Datos" as register_business

  note top of "Registrar Negocio" : Precondición:\nEl usuario debe tener el rol de Vendedor y haber iniciado sesión.
}

seller --> select_add_option
select_add_option --> show_form
show_form --> enter_info
enter_info --> save_data

save_data .> register_business : <<includes>>

note right of enter_info : Flujo Alternativo:\nFaltan campos obligatorios por llenar.
note right of save_data : Flujo Alternativo:\nEl vendedor cancela el registro.
note right of register_business : Postcondición:\nEl negocio es creado y queda listado en el catálogo del sistema.

@enduml
```
[Timestamp: 2026/04/09 10:18:54]

**user**: haz
[Context: Notes: Casos de uso/Registro de Usuarios.md]
[Timestamp: 2026/04/09 10:19:34]

**ai**: ```plantuml
@startuml
left to right direction

actor "Usuario" as user

package "Registro de Usuarios" {
  usecase "Seleccionar Opción de Registrarse" as select_register_option
  usecase "Mostrar Formulario de Registro" as show_register_form
  usecase "Ingresar Datos (Nombre, Correo, Rol, Contraseña)" as enter_data
  usecase "Presionar Botón de Confirmar" as confirm_button
  usecase "Registrar Usuario en Base de Datos" as register_user_db
  usecase "Mostrar Mensaje de Registro Exitoso" as show_success_message

  note top of "Registro de Usuarios" : Precondiciones:\n- El usuario no debe estar registrado.\n- El usuario debe contar con un correo electrónico válido.
}

user --> select_register_option
select_register_option --> show_register_form
show_register_form --> enter_data
enter_data --> confirm_button

confirm_button .> register_user_db : <<includes>>
register_user_db .> show_success_message : <<includes>>

note right of enter_data : Flujos Alternativos:\n- Credenciales erróneas.\n- Correo ya se encuentra registrado.
note right of confirm_button : Flujo Alternativo:\n- Cancelar.
note right of show_success_message : Postcondiciones:\n- El usuario queda registrado en la base de datos del sistema.\n- Se crea un perfil de usuario activo.

@enduml
```
[Timestamp: 2026/04/09 10:19:39]

**user**: haz
[Context: Notes: Casos de uso/Reportar Reseña.md]
[Timestamp: 2026/04/09 10:20:05]

**ai**: ```plantuml
@startuml
left to right direction

actor "Usuario registrado" as registered_user
actor "Moderador" as moderator

package "Reportar Reseña" {
  usecase "Visualizar Reseña Específica" as view_review
  usecase "Seleccionar Opción de Reportar" as select_report_option
  usecase "Proporcionar Motivo del Reporte" as provide_reason
  usecase "Registrar Reporte y Notificar Moderadores" as register_notify

  note top of "Reportar Reseña" : Precondición:\nEl usuario debe haber iniciado sesión.
}

registered_user --> view_review
view_review --> select_report_option
select_report_option --> provide_reason

provide_reason .> register_notify : <<includes>>

register_notify --> moderator

note right of provide_reason : Flujo Alternativo:\nEl usuario cancela el proceso.
note right of register_notify : Postcondición:\nLa reseña queda marcada en el sistema para revisión administrativa.

@enduml
```
[Timestamp: 2026/04/09 10:20:09]

**user**: haz
[Context: Notes: Casos de uso/Solicitar Unión a Evento.md]
[Timestamp: 2026/04/09 10:20:28]

**ai**: ```plantuml
@startuml
left to right direction

actor "Vendedor" as seller
actor "Moderador" as moderator

package "Solicitar Unión a Evento" {
  usecase "Consultar Eventos Activos" as consult_events
  usecase "Seleccionar Evento y Solicitar Participación" as select_request_participation
  usecase "Generar Petición y Enviar a Moderación" as generate_send_request

  note top of "Solicitar Unión a Evento" : Precondiciones:\n- Debe existir un evento activo.\n- El vendedor debe tener un negocio registrado.
}

seller --> consult_events
consult_events --> select_request_participation

select_request_participation .> generate_send_request : <<includes>>

generate_send_request --> moderator : Notifica

note right of select_request_participation : Flujos Alternativos:\n- El evento ya cerró sus inscripciones.\n- El negocio ya había enviado una solicitud.
note right of generate_send_request : Postcondición:\nSe genera una solicitud en estado pendiente de aprobación.

@enduml
```
[Timestamp: 2026/04/09 10:20:33]

**user**: haz
[Context: Notes: Casos de uso/Ver Perfil de Negocio.md]
[Timestamp: 2026/04/09 10:20:53]

**ai**: ```plantuml
@startuml
left to right direction

actor "Usuario" as user

package "Ver Perfil de Negocio" {
  usecase "Seleccionar Negocio del Catálogo o Búsqueda" as select_business
  usecase "Consultar Base de Datos" as query_database
  usecase "Desplegar Perfil Completo (Información, Reseñas, Calificaciones)" as display_profile

  note top of "Ver Perfil de Negocio" : Precondición:\nEl negocio debe estar activo en el sistema.
}

user --> select_business
select_business --> query_database
query_database .> display_profile : <<includes>>

note right of query_database : Flujo Alternativo:\nEl negocio fue eliminado o se encuentra inactivo.
note right of display_profile : Postcondición:\nEl usuario visualiza toda la información pública del negocio.

@enduml
```
[Timestamp: 2026/04/09 10:20:57]