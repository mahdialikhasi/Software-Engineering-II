from django.urls import path, include


urlpatterns = [
    path('auth/', include('auth.urls')),
    path('user/', include('user.urls')),
    path('education/', include('education.urls'))
]
