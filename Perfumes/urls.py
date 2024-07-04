from django.urls import path
from . import views

urlpatterns = [
    path('', views.Secion, name='Secion'),
    path('index/', views.index, name='index'),
    path('Registrarce/', views.Registrarce, name='Registrarce'),
    path('Principal/', views.Principal, name='Principal'),  # Esta es la URL para Principal
    path('agregar_al_carrito/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('eliminar_del_carrito/<int:item_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('logout/', views.cerrar_sesion, name='logout'),
    path('productos/', views.productos_list, name='productos_list'),
]
