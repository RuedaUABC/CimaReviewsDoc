---
id: CU-001
actores_primarios: "Usuario"
actores_secundarios: "N/A"
tipo: caso_de_uso
---

# Registro de Usuarios

## Descripción
Permite al usuario crear una cuenta en el sistema utilizando su correo electronico.

## Condiciones
**Precondiciones:**
El usuario no debe estar registrado en el sistema.
El usuario debe contar con un correo electronico valido.

**Postcondiciones:**
El usuario queda registrado en la base de datos del sistema.
Se crea un perfil de usuario activo.

## Flujo Principal
1.- El usuario selecciona la opcion de registrarse.
2.- El sistema muestra el formulario de registro.
3.- El usuario ingresa:
                  - Nombre
                  - Correo electronico
                  - Rol (Cliente/Vendedor)
                  - Contraseña
                  - Confirmacion de contraseña
4.- El usuario presiona el boton de confirmar.
5.- El sistema registra al usuario en la base de datos.
6.- El sistema muestra un mensaje de registro exitoso.

## Flujos Alternativos
Credenciales erroneas.
Cancelar.
Correo ya se encuentra registrado.

# UML

```plantuml
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
