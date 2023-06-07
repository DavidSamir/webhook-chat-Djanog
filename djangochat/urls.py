from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', include('core.urls')),
    path('rooms/', include('room.urls')),
    path('create/', views.createRoom, name='room'),
    path('admin/', admin.site.urls),
]
