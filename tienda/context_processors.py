from .models import Categorias

def extras(request):
	lista_categorias = Categorias.objects.all().order_by('nombre')
	return {'categorias':lista_categorias}