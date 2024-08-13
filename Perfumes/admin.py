from django.contrib import admin
from .models import Proveedor, Producto, MateriaPrima, Inventario, OrdenCompra, DetalleOrdenCompra, Venta, DetalleVenta, Carrito

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'contacto', 'email', 'telefono')
    search_fields = ('nombre',)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'proveedor')
    search_fields = ('nombre',)
    list_filter = ('proveedor',)

@admin.register(MateriaPrima)
class MateriaPrimaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cantidad', 'unidad', 'proveedor')
    search_fields = ('nombre',)
    list_filter = ('proveedor',)

@admin.register(Inventario)
class InventarioAdmin(admin.ModelAdmin):
    list_display = ('producto', 'cantidad_disponible', 'ultima_actualizacion')
    list_filter = ('producto',)

@admin.register(OrdenCompra)
class OrdenCompraAdmin(admin.ModelAdmin):
    list_display = ('proveedor', 'fecha_orden', 'total')
    list_filter = ('fecha_orden', 'proveedor')

@admin.register(DetalleOrdenCompra)
class DetalleOrdenCompraAdmin(admin.ModelAdmin):
    list_display = ('orden', 'producto', 'cantidad', 'precio_unitario')

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'cantidad', 'fecha_venta', 'total')
    list_filter = ('fecha_venta', 'usuario')

@admin.register(DetalleVenta)
class DetalleVentaAdmin(admin.ModelAdmin):
    list_display = ('venta', 'producto', 'cantidad', 'precio_unitario')

@admin.register(Carrito)
class CarritoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'producto', 'cantidad')
    list_filter = ('usuario',)
