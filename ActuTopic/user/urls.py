from django.urls import path
from .views import sign_in, sign_up, log_out, profile_view, edit_profile, change_password

urlpatterns = [
    path('connexion/', sign_in, name='sign_in'),
    path('inscription/', sign_up, name='sign_up'),
    path('deconnexion/', log_out, name='logout'),
    path('profile/', profile_view, name='profile_view'),
    path('profile/<int:pk>', profile_view, name='profile_view_pk'),
    path('profile/edit/<int:pk>', edit_profile, name='edit_profile'),
    path('profile/password/', change_password, name='change_password'),
]