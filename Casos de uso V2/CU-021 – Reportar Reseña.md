**Nombre:** Reportar Usuario o Reseña  
**ID:** CU-021  
**Descripción:** Permite al usuario reportar contenido inapropiado.  
**Actor:** Usuario  

**Precondiciones:**

- Usuario autenticado.

**Flujo principal:**

1. El usuario selecciona reportar.
2. El sistema muestra formulario.
3. El usuario selecciona motivo.
4. El usuario agrega un comentario con detalles del reporte.
5. Envía reporte.
6. El sistema guarda el reporte.

**Postcondiciones:**

- Reporte registrado.

**Excepciones:**

- Cancelación.



```plantuml
@startuml

actor Usuario
participant "Sistema" as Sistema
database "Base de Datos" as DB

Usuario -> Sistema: 1. Seleccionar opción "Reportar"
activate Sistema
Sistema --> Usuario: 2. Mostrar formulario de reporte (motivos, comentario)
deactivate Sistema

Usuario -> Sistema: 3. Seleccionar motivo de reporte
activate Sistema
Usuario -> Sistema: 4. Agregar comentario con detalles
Usuario -> Sistema: 5. Enviar reporte
Sistema -> DB: 6. Guardar reporte
activate DB
DB --> Sistema: 7. Reporte guardado
deactivate DB
Sistema --> Usuario: 8. Confirmar reporte registrado
deactivate Sistema

@enduml
```

