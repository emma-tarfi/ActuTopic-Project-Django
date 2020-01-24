from django.urls import path
from .views import sign_in, sign_up, log_out

urlpatterns = [
    path('connexion/', sign_in, name='sign_in'),
    path('inscription/', sign_up, name='sign_up'),
    path('deconnexion/', log_out, name='logout'),
]