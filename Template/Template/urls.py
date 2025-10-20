from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),   # superusuário cria contas e usuários
    path('', include('core.urls')),    # login e dashboard
]
