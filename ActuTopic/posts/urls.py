from django.urls import path
from .views import (PostListView, PostDetailView, PostUpdateView, PostDeleteView, MyPostListView, post_create)


urlpatterns =[
    path('', PostListView.as_view(), name='post_list'),
    path('<slug:slug>', PostDetailView.as_view(), name='post_detail'),
    path('mes-publications/', MyPostListView.as_view(), name='my_posts'),
    path('mes-publications/<slug:slug>', PostDetailView.as_view(), name='my_posts_detail'),
    path('nouveau-post/', post_create, name='create'),
    path('modifier/<int:pk>', PostUpdateView.as_view(), name='update'),
    path('supprimer/<int:pk>', PostDeleteView.as_view(), name='delete'),
]