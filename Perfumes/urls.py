from django.urls import path
from . import views

urlpatterns = [
    path('', views.Secion, name='Secion'),
    path('index/', views.index, name='index'),
    path('Registrarce/', views.Registrarce, name='Registrarce'),
    path('Principal/', views.Principal, name='Principal'),
    path('agregar_al_carrito/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('eliminar_del_carrito/<int:item_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('logout/', views.cerrar_sesion, name='logout'),
    path('productos/', views.listar_productos, name='listar_productos'),
    path('productos/agregar/', views.agregar_producto, name='agregar_producto'),
    path('productos/editar/<int:pk>/', views.editar_producto, name='editar_producto'),
    path('productos/eliminar/<int:pk>/', views.eliminar_producto, name='eliminar_producto'),
]
