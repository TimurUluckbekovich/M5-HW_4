from django.urls import path
from .views import (
    PostListCreateAPIView,
    PostDetailAPIView,
    ClientListCreateAPIView,
    ClientDetailAPIView,
)

urlpatterns = [
    path('posts/', PostListCreateAPIView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostDetailAPIView.as_view(), name='post-detail'),

    path('clients/', ClientListCreateAPIView.as_view(), name='client-list-create'),
    path('clients/<int:pk>/', ClientDetailAPIView.as_view(), name='client-detail'),
]