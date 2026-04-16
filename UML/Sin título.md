
### 1. WelcomeScreen

```plantuml
@startuml
package "Screens (Widgets)" {
    class WelcomeScreen <<Stateless>>
}
' No hay relaciones explícitas con modelos en el contexto dado para esta pantalla.
@enduml
```

### 2. LoginScreen

```plantuml
@startuml
package "Screens (Widgets)" {
    class LoginScreen <<Stateful>>
}
' No hay relaciones explícitas con modelos en el contexto dado para esta pantalla.
@enduml
```

### 3. HomeScreen

```plantuml
@startuml
package "Modelos" {
    class Business {
        +String id
        +String name
        +double avgRating
        +String category
        +String schedule
        +String locationInfo
        +String imageUrl
    }
}

package "Screens (Widgets)" {
    class HomeScreen <<Stateless>>
}

' Relaciones
HomeScreen ..> Business : muestra lista
@enduml
```

### 4. PlaceDetailsScreen

```plantuml
@startuml
package "Modelos" {
    class Business {
        +String id
        +String name
        +double avgRating
        +String category
        +String schedule
        +String locationInfo
        +String imageUrl
    }

    class Review {
        +String id
        +String authorName
        +double rating
        +String comment
        +DateTime date
    }
}

package "Screens (Widgets)" {
    class PlaceDetailsScreen <<Stateless>>
}

' Relaciones
PlaceDetailsScreen ..> Business : muestra detalle
PlaceDetailsScreen ..> Review : muestra lista
@enduml
```

### 5. CampusMapScreen

```plantuml
@startuml
package "Screens (Widgets)" {
    class CampusMapScreen <<Stateless>>
}
' No hay relaciones explícitas con modelos en el contexto dado para esta pantalla.
@enduml
```

### 6. ReviewsListScreen

```plantuml
@startuml
package "Screens (Widgets)" {
    class ReviewsListScreen <<Stateless>>
}
' Aunque PlaceDetailsScreen muestra una lista de Reviews, ReviewsListScreen no tiene una relación directa con el modelo Review en el contexto proporcionado.
@enduml
```

### 7. WriteReviewScreen

```plantuml
@startuml
package "Modelos" {
    class Review {
        +String id
        +String authorName
        +double rating
        +String comment
        +DateTime date
    }
}

package "Screens (Widgets)" {
    class WriteReviewScreen <<Stateful>>
}

' Relaciones
WriteReviewScreen ..> Review : crea
@enduml
```

### 8. UserProfileScreen

```plantuml
@startuml
package "Modelos" {
    class User {
        +String id
        +String name
        +String email
        +String profilePicUrl
        +List<Review> myReviews
    }
}

package "Screens (Widgets)" {
    class UserProfileScreen <<Stateless>>
}

' Relaciones
UserProfileScreen ..> User : muestra info
@enduml
```

### 9. EventsScreen

```plantuml
@startuml
package "Modelos" {
    class Event {
        +String id
        +String title
        +DateTime date
        +String location
        +List<Business> participants
    }
}

package "Screens (Widgets)" {
    class EventsScreen <<Stateless>>
}

' Relaciones
EventsScreen ..> Event : muestra lista
@enduml
```

### 10. EventDetailsScreen

```plantuml
@startuml
package "Screens (Widgets)" {
    class EventDetailsScreen <<Stateless>>
}
' Aunque EventsScreen muestra una lista de Eventos, EventDetailsScreen no tiene una relación directa con el modelo Event en el contexto proporcionado.
@enduml
```