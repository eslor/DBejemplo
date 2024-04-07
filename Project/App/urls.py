from django.urls import path
from .views import ListCatAPIView, CreateCatAPIView, UpdateCatAPIView, DeleteCatAPIView

urlpatterns = [
    path('cat/', ListCatAPIView.as_view(), name='cat-list'),
    path('cat/create/', CreateCatAPIView.as_view(), name='cat-create'),
    path('cat/<int:pk>/', UpdateCatAPIView.as_view(), name='cat-update'),
    path('cat/<int:pk>/delete/', DeleteCatAPIView.as_view(), name='cat-delete'),
]

