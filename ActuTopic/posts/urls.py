from django.urls import path
from .views import (PostListView, PostDetailView, PostUpdateView, PostDeleteView, MyPostListView, PostCreateView)


urlpatterns =[
    path('', PostListView.as_view(), name='post_list'),
    path('<int:pk>-<str:slug>', PostDetailView.as_view(), name='post_detail'),
    path('mes-publications/', MyPostListView.as_view(), name='my_posts'),
    path('mes-publications/<int:pk>-<str:slug>/', PostDetailView.as_view(), name='my_posts_detail'),
    path('nouveau-post/', PostCreateView.as_view(), name='create'),
    path('modifier/<int:pk>', PostUpdateView.as_view(), name='update'),
    path('supprimer/<int:pk>', PostDeleteView.as_view(), name='delete'),
]