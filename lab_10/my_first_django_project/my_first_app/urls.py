from django.urls import path
from .views import hello_world, redirect_example, json_example, show_cookies

# регистрация представлений в приложении с указанием маршрутов
urlpatterns = [
    path('hello/', hello_world, name='hello_world'),
    path('redirect/', redirect_example, name='redirect_example'),
    path('json/', json_example, name='json_example'),
    path('show_cookies/', show_cookies, name='show_cookies'),
]
