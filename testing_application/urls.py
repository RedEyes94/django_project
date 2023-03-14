from django.urls import path
from . import views

# il path di base qui è testing_application

# se vuoi aggiungere un livello fai 'tests/livello2'
urlpatterns = [
    path('',views.rolls, name='home'),
    # il parametro name è quello che serve per riferirsi alla view contattaci
    path('contattaci',views.contattaci, name='contattaci'),
    path('login',views.login, name='login')
]
