from django.urls import path
from . import views

app_name = 'catalogs'

urlpatterns = [
    path('clients/', views.ClientListView.as_view(), name='client_list'),
    path('clients/create/', views.ClientCreateView.as_view(), name='client_create'),
    path('clients/<int:pk>/update/', views.ClientUpdateView.as_view(), name='client_update'),
    path('clients/<int:pk>/delete/', views.ClientDeleteView.as_view(), name='client_delete'),
    path('mechanics/create/', views.MechanicCreateView.as_view(), name='mechanic_create'),
    path('mechanics/', views.MechanicListView.as_view(), name='mechanic_list'),
    path('mechanics/<int:pk>/update/', views.MechanicUpdateView.as_view(), name='mechanic_update'),
    path('mechanics/<int:pk>/delete/', views.MechanicDeleteView.as_view(), name='mechanic_delete'),
    path('service_order/<int:pk>/update_payment/', views.ServiceOrderPaymentUpdateView.as_view(), name='service_order_update_payment'),
    path('sparepart/', views.SparePartListView.as_view(), name='sparepart_list'),
    path('sparepart/create/', views.SparePartCreateView.as_view(), name='sparepart_create'),
    path('sparepart/<int:pk>/update/', views.SparePartUpdateView.as_view(), name='sparepart_update'),
    path('sparepart/<int:pk>/delete/', views.SparePartDeleteView.as_view(), name='sparepart_delete'),
]
