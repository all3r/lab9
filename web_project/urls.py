from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Подключаем пути приложения lab6
    path('lab6/', include('lab6.urls')),
]