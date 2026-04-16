
```plantuml
@startuml
package "Models" {
    class User {
        +String id
        +String name
        +String email
        +String profilePicUrl
        +List<Review> myReviews
    }

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

    class Event {
        +String id
        +String title
        +DateTime date
        +String location
        +List<Business> participants
    }
}


' Relaciones de datos
User "1" *-- "many" Review : posee
Business "1" *-- "many" Review : tiene
Event "many" o-- "many" Business : incluye

' Relaciones de las pantallas con los modelos
HomeScreen ..> Business : muestra lista
PlaceDetailsScreen ..> Business : muestra detalle
PlaceDetailsScreen ..> Review : muestra lista
EventsScreen ..> Event : muestra lista
UserProfileScreen ..> User : muestra info
WriteReviewScreen ..> Review : crea

@endum
```

```plantuml
package "Screens (Widgets)" {
    class WelcomeScreen <<Stateless>>
    class LoginScreen <<Stateful>>
    class HomeScreen <<Stateless>>
    class PlaceDetailsScreen <<Stateless>>
    class CampusMapScreen <<Stateless>>
    class ReviewsListScreen <<Stateless>>
    class WriteReviewScreen <<Stateful>>
    class UserProfileScreen <<Stateless>>
    class EventsScreen <<Stateless>>
    class EventDetailsScreen <<Stateless>>
}

' Relaciones de las pantallas con los modelos
HomeScreen ..> Business : muestra lista
PlaceDetailsScreen ..> Business : muestra detalle
PlaceDetailsScreen ..> Review : muestra lista
EventsScreen ..> Event : muestra lista
UserProfileScreen ..> User : muestra info
WriteReviewScreen ..> Review : crea

```
