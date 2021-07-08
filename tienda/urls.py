from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name='tienda'

urlpatterns = [
    # paths menú
    path('', views.index, name='index'),
    path('categorias/', views.listCategorias, name='categorias'),
    path('contacto/', views.contacto, name='contacto'),
    path('garantia/', views.garantia, name='garantia'),
    path('devoluciones/', views.devoluciones, name='devoluciones'),
    path('nosotros/', views.nosotros, name='nosotros'),

    path('producto/', views.detalleProducto, name='producto'),
    path('addproducto/', views.addProducto, name='addproducto'),
    path('detalleproducto/<id>/', views.detalleProducto, name='detalleproducto'),
    path('productocategoria/<id>/', views.productoxCategoria, name='productocategoria'),
    path('editproducto/<id>/', views.editarProducto, name='editproducto'),
    path('deleteProducto/<id>/', views.deleteProducto, name='deleteProducto'),
    path('listarproductos/', views.listarProductos, name='listarproductos'),
    path('addcategoria/', views.addCategoria, name='addcategoria'),
    path('editcategoria/<id>/', views.modificarCategoria, name='editcategoria'),
    path('deleteCategoria/<id>/', views.deleteCategoria, name='deleteCategoria'),
        
    # paths de autenticacion
    path('registrar/', views.registrar, name='registrar'),
    path('login/', LoginView.as_view(template_name='auth/login.html'), name='login'),
    
    #Paths del carrito
    path('viewcart/', views.viewcart, name="viewcart"),

    path('addcart/<producto_id>/', views.agregar_producto, name="addcart"),

    path('delcart/<producto_id>/', views.eliminar_producto, name="delcart"),

    path('restarcart/<producto_id>/', views.restar_producto, name="restarcart"),

    path('cleancart/', views.limpiar_carro, name="cleancart"),
    
]
