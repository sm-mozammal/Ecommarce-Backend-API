from django.urls import path
from .views import AddressesView


urlpatterns =[
    path('', AddressesView.as_view(), name='addresses'),
    path('<int:pk>/', AddressesView.as_view(), name='address-detail'),
]