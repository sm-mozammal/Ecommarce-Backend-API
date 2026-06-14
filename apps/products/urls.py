from  django.urls import path

from .views import CategoryViewSet, BrandViewSet

urlpatterns = [
    path('categories/', CategoryViewSet.as_view({'get': 'list', 'post': 'create'}), name='category-list'),
    path('categories/<int:pk>/', CategoryViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='category-detail'),
    path('brands/', BrandViewSet.as_view({'get': 'list', 'post': 'create'}), name='brand-list'),
    path('brands/<int:pk>/', BrandViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='brand-detail'),
]
