from django.urls import path

from .views import home, catalog, textarea

# регистрация представлений в приложении с указанием маршрутов
urlpatterns = [
    path('', home, name='home'),
    path('catalog/', catalog, name='catalog'),
    path('textarea/', textarea, name='textarea'),
]