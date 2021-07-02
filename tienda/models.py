from django.db import models

# Create your models here.
class Categorias(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = "categorias"
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']


#modelo Productos
class Productos(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='imgproductos/%Y/%m/%d', blank=True)
    descripcion = models.CharField(max_length=500)
    precio = models.IntegerField()
    stock = models.IntegerField(null=True, default=0)
    categoria = models.ForeignKey(Categorias, on_delete=models.PROTECT)
    oferta = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'productos'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']


# Model Carrito
# class OrderItem(models.Model):
#     producto = models.ForeignKey(Productos, on_delete=models.PROTECT, null=True)
#     is_ordered = models.BooleanField(default=False)
#     fecha_compra = models.DateTimeField(auto_now=True)
#     cantidad = models.IntegerField(default=1)
#     def __str__(self):
#         return self.item.nombre

# class Cart(models.Model):
#     cliente = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
#     is_ordered = models.BooleanField(default=False)
#     items = models.ManyToManyField(OrderItem, default=None, blank=True)


class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre
