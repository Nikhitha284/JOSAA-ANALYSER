from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('josaapp.urls')),
    path('', include('josaapp.urls')),  # Add this line if you want to include URLs for the josaapp application on the project's root URL
]
