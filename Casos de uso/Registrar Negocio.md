---
id: CU-009
actores_primarios: "Vendedor"
actores_secundarios: "N/A"
tipo: caso_de_uso
---

# Registrar Negocio

## Descripción
Permite a los vendedores agregar la información de sus negocios al sistema (RF-014).

## Condiciones
**Precondiciones:**
El usuario debe tener el rol de Vendedor y haber iniciado sesión.

**Postcondiciones:**
El negocio es creado y queda listado en el catálogo del sistema.

## Flujo Principal
1.- El vendedor selecciona la opción de agregar negocio.
2.- El sistema muestra el formulario de registro.
3.- El vendedor ingresa la información solicitada (nombre, descripción, etc.).
4.- El vendedor guarda los datos.
5.- El sistema registra el negocio en la base de datos.

## Flujos Alternativos
Faltan campos obligatorios por llenar.
El vendedor cancela el registro.

# UML
```plantuml
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
