from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Perfumes.urls')),  # Incluye las URLs de tu aplicación
]
