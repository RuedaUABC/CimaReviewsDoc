

```mermaid
classDiagram
    direction TB
    
    %% ============================
    %% MODELS (Dominio)
    %% ============================
    class User {
        +String id
        +String name
        +String email
        +List~Role~ roles
        +DateTime createdAt
        +toJson() Map
        +fromJson() User
    }
    
    class Business {
        +String id
        +String name
        +String ownerId
        +LatLng location
        +double avgRating
        +List~Category~ categories
        +List~Product~ products
        +List~Review~ reviews
        +toJson() Map
        +fromJson() Business
    }
    
    class Review {
        +String id
        +String businessId
        +String userId
        +double rating
        +String comment
        +List~String~ images
        +DateTime createdAt
        +toJson() Map
        +fromJson() Review
    }
    
    class Report {
        +String id
        +String reason
        +String reporterId
        +String reportedUserId
        +String? businessId
        +String? reviewId
        +ReportStatus status
        +DateTime createdAt
    }
    
    class Event {
        +String id
        +String title
        +String description
        +DateTime date
        +List~String~ businessIds
        +String imageUrl
    }
    
    class Session {
        +String token
        +User user
        +DateTime expiresAt
        +bool isValid()
    }
    
    class Product {
        +String name
        +double price
        +String? description
    }
    
    class Role {
        <<enumeration>>
        ADMIN
        MODERATOR
        SELLER
        CUSTOMER
    }
    
    class Category {
        <<enumeration>>
        VEGANO
        CAFETERIA
        ASIATICA
        RAMEN
        MEXICANA
        DESAYUNOS
        PANADERIA
        SUSHI
        PIZZA
        HAMBURGUESAS
        TACOS
        ITALIANA
        ENSALADAS
        POSTRES
    }
    
    class Permission {
        <<enumeration>>
        DELETE_ANY_REVIEW
        CREATE_BUSINESS
        EDIT_ANY_BUSINESS
        DELETE_ANY_BUSINESS
        BAN_USER
        VIEW_ANALYTICS
    }
    
    class ReportStatus {
        <<enumeration>>
        PENDING
        REVIEWED
        RESOLVED
        REJECTED
    }
    
    %% ============================
    %% SERVICES (Capa técnica)
    %% ============================
    class ApiService {
        -http.Client _client
        -String _baseUrl
        -String? _token
        +get(String endpoint) Future~Response~
        +post(String endpoint, dynamic body) Future~Response~
        +put(String endpoint, dynamic body) Future~Response~
        +delete(String endpoint) Future~Response~
        +setToken(String token) void
        -_buildHeaders() Map
        -_handleResponse(Response) dynamic
    }
    
    class DatabaseService {
        -Database _db
        +getBusinesses() Future~List~Business~~
        +getBusiness(String id) Future~Business?~
        +saveBusiness(Business business) Future~void~
        +saveBusinesses(List~Business~ businesses) Future~void~
        +deleteBusiness(String id) Future~void~
        +getReviewsByBusiness(String businessId) Future~List~Review~~
        +saveReview(Review review) Future~void~
        +deleteReview(String id) Future~void~
        +getUser(String id) Future~User?~
        +saveUser(User user) Future~void~
        +clearAll() Future~void~
        -_initDatabase() Future~void~
        -_onCreate(Database db, int version) Future~void~
    }
    
    class CacheService {
        -SharedPreferences _prefs
        +setToken(String token) Future~void~
        +getToken() String?
        +setUser(User user) Future~void~
        +getUser() User?
        +setLastSync(DateTime date) Future~void~
        +getLastSync() DateTime?
        +setPreferences(String key, dynamic value) Future~void~
        +getPreferences(String key) dynamic
        +clear() Future~void~
        -_init() Future~void~
    }
    
    class LocationService {
        -GeolocatorPlatform _geolocator
        +getCurrentPosition() Future~Position~
        +getCurrentAddress() Future~String~
        +calculateDistance(double lat1, double lon1, double lat2, double lon2) double
        +searchAddress(String query) Future~List~Address~~
        +getAddressFromCoordinates(double lat, double lon) Future~String~
        +checkPermissions() Future~bool~
        +requestPermissions() Future~bool~
    }
    
    class AuthService {
        -ApiService _api
        -CacheService _cache
        +login(String email, String password) Future~Session~
        +register(User user, String password) Future~User~
        +logout() Future~void~
        +refreshToken() Future~String~
        +isAuthenticated() bool
        +getCurrentSession() Session?
        -_saveSession(Session session) Future~void~
    }
    
    %% ============================
    %% REPOSITORIES (Orquestadores)
    %% ============================
    class BusinessRepository {
        -ApiService _apiService
        -DatabaseService _databaseService
        -CacheService _cacheService
        +getBusinesses() Future~List~Business~~
        +getBusiness(String id) Future~Business~
        +createBusiness(Business business) Future~void~
        +updateBusiness(Business business) Future~void~
        +deleteBusiness(String id) Future~void~
        +searchBusinesses(String query) Future~List~Business~~
        +getBusinessesByCategory(Category category) Future~List~Business~~
        +getNearbyBusinesses(LatLng center, double radius) Future~List~Business~~
        -_syncWithServer() Future~void~
        -_refreshInBackground() Future~void~
    }
    
    class UserRepository {
        -ApiService _apiService
        -CacheService _cacheService
        -DatabaseService _databaseService
        +getCurrentUser() User?
        +updateProfile(User user) Future~void~
        +changePassword(String oldPass, String newPass) Future~void~
        +getUserById(String id) Future~User~
        +getUserReviews(String userId) Future~List~Review~~
        +isLoggedIn() bool
        -_syncUserToLocal(User user) Future~void~
    }
    
    class ReviewRepository {
        -ApiService _apiService
        -DatabaseService _databaseService
        +createReview(Review review) Future~void~
        +getReviewsByBusiness(String businessId) Future~List~Review~~
        +getReviewsByUser(String userId) Future~List~Review~~
        +deleteReview(String id) Future~void~
        +updateReview(Review review) Future~void~
        +reportReview(String reviewId, String reason) Future~void~
        +getAverageRating(String businessId) Future~double~
    }
    
    class ReportRepository {
        -ApiService _apiService
        +createReport(Report report) Future~void~
        +getReports() Future~List~Report~~
        +updateReportStatus(String id, ReportStatus status) Future~void~
        +getReportsByUser(String userId) Future~List~Report~~
        +resolveReport(String id, String resolution) Future~void~
    }
    
    class EventRepository {
        -ApiService _apiService
        -DatabaseService _databaseService
        +getEvents() Future~List~Event~~
        +getEvent(String id) Future~Event~
        +getUpcomingEvents() Future~List~Event~~
        +getEventsByBusiness(String businessId) Future~List~Event~~
        +createEvent(Event event) Future~void~
        +registerBusinessToEvent(String eventId, String businessId) Future~void~
    }
    
    %% ============================
    %% VIEWMODELS (Lógica de UI)
    %% ============================
    class DashboardViewModel {
        -BusinessRepository _businessRepository
        -UserRepository _userRepository
        +List~Business~ businesses
        +bool isLoading
        +String? error
        +User? currentUser
        +loadBusinesses() Future~void~
        +refresh() Future~void~
        +loadUserData() Future~void~
        +searchBusinesses(String query) Future~void~
        +dispose() void
    }
    
    class BusinessDetailsViewModel {
        -BusinessRepository _businessRepository
        -ReviewRepository _reviewRepository
        -UserRepository _userRepository
        +Business? business
        +List~Review~ reviews
        +double averageRating
        +bool isLoading
        +bool isOwner
        +String? error
        +loadDetails(String businessId) Future~void~
        +submitReview(Review review) Future~bool~
        +deleteReview(String reviewId) Future~void~
        +reportReview(String reviewId, String reason) Future~void~
        +checkIfOwner() Future~bool~
        +dispose() void
    }
    
    class MapViewModel {
        -BusinessRepository _businessRepository
        -LocationService _locationService
        +List~Business~ nearbyBusinesses
        +GeoPoint? currentLocation
        +bool isLoading
        +double? currentZoom
        +loadNearbyBusinesses() Future~void~
        +getCurrentLocation() Future~void~
        +searchLocation(String query) Future~GeoPoint?~
        +getMarkers() Future~List~MarkerIcon~~
        +centerOnBusiness(Business business) Future~void~
        +calculateRouteToBusiness(Business business) Future~RoadInfo?~
        +dispose() void
    }
    
    class LoginViewModel {
        -AuthService _authService
        -UserRepository _userRepository
        +String email
        +String password
        +bool isLoading
        +bool rememberMe
        +String? errorMessage
        +setEmail(String value) void
        +setPassword(String value) void
        +toggleRememberMe() void
        +login() Future~bool~
        +validateForm() bool
        +loginWithBiometrics() Future~bool~
        +clearError() void
        +dispose() void
    }
    
    class RegisterViewModel {
        -AuthService _authService
        +String name
        +String email
        +String password
        +String confirmPassword
        +bool isLoading
        +List~String~ errors
        +setName(String value) void
        +setEmail(String value) void
        +setPassword(String value) void
        +setConfirmPassword(String value) void
        +register() Future~bool~
        +validateForm() List~String~
        +dispose() void
    }
    
    class UserProfileViewModel {
        -UserRepository _userRepository
        -ReviewRepository _reviewRepository
        +User? user
        +List~Review~ userReviews
        +bool isLoading
        +bool isEditing
        +loadUserProfile(String userId) Future~void~
        +updateProfile(User updatedUser) Future~bool~
        +changePassword(String oldPass, String newPass) Future~bool~
        +loadUserReviews() Future~void~
        +toggleEditMode() void
        +dispose() void
    }
    
    class WriteReviewViewModel {
        -ReviewRepository _reviewRepository
        +String businessId
        +double rating
        +String comment
        +List~String~ images
        +bool isLoading
        +setRating(double value) void
        +setComment(String value) void
        +addImage(String imagePath) void
        +removeImage(int index) void
        +submitReview() Future~bool~
        +validateForm() bool
        +clearForm() void
        +dispose() void
    }
    
    class EventsViewModel {
        -EventRepository _eventRepository
        +List~Event~ events
        +bool isLoading
        +String? error
        +loadEvents() Future~void~
        +registerToEvent(String eventId, String businessId) Future~bool~
        +getEventsByDate(DateTime date) List~Event~
        +refresh() Future~void~
        +dispose() void
    }
    
    class RegisterBusinessViewModel {
        -BusinessRepository _businessRepository
        -LocationService _locationService
        +String name
        +String description
        +LatLng? location
        +List~Category~ selectedCategories
        +bool isLoading
        +setName(String value) void
        +setDescription(String value) void
        +setLocation(LatLng value) void
        +toggleCategory(Category category) void
        +registerBusiness() Future~bool~
        +searchLocation(String query) Future~void~
        +validateForm() bool
        +dispose() void
    }
    
    %% ============================
    %% VIEWS (UI)
    %% ============================
    class DashboardView {
        +build() Widget
        -_buildBusinessList() Widget
        -_buildAppBar() Widget
        -_onBusinessTap(Business) void
        -_onRefresh() Future~void~
    }
    
    class BusinessDetailsView {
        +String businessId
        +build() Widget
        -_buildHeader() Widget
        -_buildRatingSection() Widget
        -_buildReviewsList() Widget
        -_buildWriteReviewButton() Widget
        -_onWriteReview() void
    }
    
    class MapView {
        +build() Widget
        -_onMapCreated(MapController) void
        -_addMarkers() void
        -_onMarkerTap(Business) void
        -_onMyLocationTap() void
        -_showBusinessBottomSheet(Business) void
    }
    
    class LoginView {
        +build() Widget
        -_buildEmailField() Widget
        -_buildPasswordField() Widget
        -_buildLoginButton() Widget
        -_onLoginPressed() void
        -_onRegisterPressed() void
        -_showError(String message) void
    }
    
    class RegisterView {
        +build() Widget
        -_buildNameField() Widget
        -_buildEmailField() Widget
        -_buildPasswordFields() Widget
        -_onRegisterPressed() void
        -_showErrors(List~String~ errors) void
    }
    
    class UserProfileView {
        +String userId
        +build() Widget
        -_buildProfileHeader() Widget
        -_buildUserReviews() Widget
        -_buildEditButton() Widget
        -_onEditProfile() void
        -_onChangePassword() void
    }
    
    class WriteReviewView {
        +String businessId
        +build() Widget
        -_buildRatingBar() Widget
        -_buildCommentField() Widget
        -_buildImagePicker() Widget
        -_onSubmit() void
    }
    
    class EventsView {
        +build() Widget
        -_buildEventList() Widget
        -_buildEventCard(Event) Widget
        -_onEventTap(Event) void
        -_onRegisterTap(Event) void
    }
    
    class RegisterBusinessView {
        +build() Widget
        -_buildBusinessForm() Widget
        -_buildCategorySelector() Widget
        -_buildLocationPicker() Widget
        -_onSubmit() void
        -_onLocationSelected(LatLng) void
    }
    
    %% ============================
    %% WIDGETS REUTILIZABLES
    %% ============================
    class RatingStars {
        +double rating
        +double size
        +bool interactive
        +Function(double)? onRatingUpdate
        +build() Widget
    }
    
    class BusinessCard {
        +Business business
        +VoidCallback? onTap
        +build() Widget
    }
    
    class LoadingIndicator {
        +String? message
        +build() Widget
    }
    
    class CustomAppBar {
        +String title
        +List~Widget~? actions
        +bool showBackButton
        +build() Widget
    }
    
    class ErrorWidget {
        +String message
        +VoidCallback? onRetry
        +build() Widget
    }
    
    class CustomBottomNavBar {
        +int currentIndex
        +Function(int) onTap
        +build() Widget
    }
    
    %% ============================
    %% RELACIONES MODELOS
    %% ============================
    User "1" *-- "many" Role : tiene
    Role "many" *-- "many" Permission : contiene
    User "1" o-- "1" Session : posee
    Business "1" *-- "many" Product : tiene
    Business "1" *-- "many" Review : recibe
    Business "many" *-- "1" User : pertenece a
    Business "many" *-- "many" Category : categorizado por
    Review "1" --> "1" User : escrito por
    Review "1" --> "1" Business : pertenece a
    Report "1" --> "1" User : reportado por
    Report "1" --> "1" User : reporta a
    Report "1" --> "1" Business : referencia a
    Report "1" --> "1" Review : referencia a
    Event "1" *-- "many" Business : incluye
    
    %% ============================
    %% RELACIONES SERVICES → REPOSITORIES
    %% ============================
    BusinessRepository --> ApiService : usa
    BusinessRepository --> DatabaseService : usa
    BusinessRepository --> CacheService : usa
    
    UserRepository --> ApiService : usa
    UserRepository --> CacheService : usa
    UserRepository --> DatabaseService : usa
    
    ReviewRepository --> ApiService : usa
    ReviewRepository --> DatabaseService : usa
    
    ReportRepository --> ApiService : usa
    
    EventRepository --> ApiService : usa
    EventRepository --> DatabaseService : usa
    
    AuthService --> ApiService : usa
    AuthService --> CacheService : usa
    
    %% ============================
    %% RELACIONES REPOSITORIES → VIEWMODELS
    %% ============================
    DashboardViewModel ..> BusinessRepository : usa
    DashboardViewModel ..> UserRepository : usa
    
    BusinessDetailsViewModel ..> BusinessRepository : usa
    BusinessDetailsViewModel ..> ReviewRepository : usa
    BusinessDetailsViewModel ..> UserRepository : usa
    
    MapViewModel ..> BusinessRepository : usa
    MapViewModel ..> LocationService : usa
    
    LoginViewModel ..> AuthService : usa
    LoginViewModel ..> UserRepository : usa
    
    RegisterViewModel ..> AuthService : usa
    
    UserProfileViewModel ..> UserRepository : usa
    UserProfileViewModel ..> ReviewRepository : usa
    
    WriteReviewViewModel ..> ReviewRepository : usa
    
    EventsViewModel ..> EventRepository : usa
    
    RegisterBusinessViewModel ..> BusinessRepository : usa
    RegisterBusinessViewModel ..> LocationService : usa
    
    %% ============================
    %% RELACIONES VIEW → VIEWMODEL
    %% ============================
    DashboardView --> DashboardViewModel : watches
    BusinessDetailsView --> BusinessDetailsViewModel : watches
    MapView --> MapViewModel : watches
    LoginView --> LoginViewModel : watches
    RegisterView --> RegisterViewModel : watches
    UserProfileView --> UserProfileViewModel : watches
    WriteReviewView --> WriteReviewViewModel : watches
    EventsView --> EventsViewModel : watches
    RegisterBusinessView --> RegisterBusinessViewModel : watches
```
