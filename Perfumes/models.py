from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=50)
    email = models.EmailField()
    contrasena = models.CharField(max_length=100)
    rol = models.CharField(max_length=50)
    nombres = models.CharField(max_length=50, null=True, blank=True)
    apellidos = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.nombre_usuario

    class Meta:
        db_table = 'Usuario'

class Proveedor(models.Model):
    nombre = models.CharField(max_length=200)
    contacto = models.CharField(max_length=200)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    direccion = models.TextField()

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'proveedores'

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(decimal_places=2, max_digits=10)
    imagen = models.ImageField(upload_to='productos/')
    proveedor = models.ForeignKey(Proveedor, on_delete=models.SET_NULL, null=True, blank=True)

    def disminuir_cantidad_disponible(self, cantidad):
        inventario = Inventario.objects.get(producto=self)
        if inventario.cantidad_disponible >= cantidad:
            inventario.cantidad_disponible -= cantidad
            inventario.save()
        else:
            raise ValueError("No hay suficiente cantidad disponible en inventario.")

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'productos'


class MateriaPrima(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    cantidad = models.DecimalField(decimal_places=2, max_digits=10)
    unidad = models.CharField(max_length=50)  # Ej: gramos, litros, etc.
    proveedor = models.ForeignKey(Proveedor, on_delete=models.SET_NULL, null=True, blank=True)

    def disminuir_cantidad(self, cantidad_usada):
        if self.cantidad >= cantidad_usada:
            self.cantidad -= cantidad_usada
            self.save()
        else:
            raise ValueError(f"No hay suficiente cantidad de {self.nombre} disponible.")

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'materia_prima'


class ProductoMateriaPrima(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    materia_prima = models.ForeignKey(MateriaPrima, on_delete=models.CASCADE)
    cantidad_requerida = models.DecimalField(decimal_places=2, max_digits=10)  # Cantidad de materia prima requerida para un producto

    def __str__(self):
        return f'{self.cantidad_requerida} de {self.materia_prima.nombre} para {self.producto.nombre}'

    class Meta:
        db_table = 'producto_materia_prima'


class Inventario(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad_disponible = models.IntegerField()
    ultima_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.producto.nombre} - {self.cantidad_disponible} en stock'

    class Meta:
        db_table = 'inventario'

class OrdenCompra(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    fecha_orden = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return f'Orden {self.id} - {self.proveedor.nombre}'

    class Meta:
        db_table = 'ordenes_compra'


class DetalleOrdenCompra(models.Model):
    orden = models.ForeignKey(OrdenCompra, related_name='detalles', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return f'{self.cantidad} x {self.producto.nombre} en Orden {self.orden.id}'

    class Meta:
        db_table = 'detalle_orden_compra'


class Venta(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha_venta = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)  # Valor por defecto de 0.00

    def __str__(self):
        return f'Venta {self.id} - {self.usuario.username}'

    class Meta:
        db_table = 'ventas'


class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, related_name='detalles', on_delete=models.CASCADE)  # Usamos 'Venta' como una cadena
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return f'{self.cantidad} x {self.producto.nombre} en Venta {self.venta.id}'

    class Meta:
        db_table = 'detalle_venta'


class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.cantidad} x {self.producto.nombre}'

    class Meta:
        db_table = 'Carrito'
