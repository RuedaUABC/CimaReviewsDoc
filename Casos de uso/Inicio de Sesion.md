---
id: CU-002
actores_primarios: "Usuario registrado"
actores_secundarios: "N/A"
tipo: caso_de_uso
---

# Inicio de Sesion

## Descripción
Permite al usuario iniciar sesion en el sistema.

## Condiciones
**Precondiciones:**
El usuario debe estar registrado en el sistema.

**Postcondiciones:**
El usuario obtiene acceso a su cuenta con una sesión activa.

## Flujo Principal
1.- El usuario selecciona la opcion de iniciar sesion.
2.- El sistema muestra el formulario de inicio de sesion.
3.- El usuario ingresa:
                   - Correo electronico
                   - Contraseña
4.- El usuario presiona el boton de confirmar.
5.- El sistema valida las credenciales del usuario.
6.- El sistema redirige al usuario a la pagina principal.

## Flujos Alternativos
Credenciales incorrectas.
El usuario no existe.

# UML

```plantuml
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