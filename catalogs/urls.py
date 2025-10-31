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
]
