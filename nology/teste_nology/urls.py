from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_compras_view.as_view(), name='listar_compras'),
    path('criar_compra/', views.criar_compra_view.as_view(), name='criar_compra'),
]