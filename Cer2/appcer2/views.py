from django.shortcuts import render
from appcer2.models import Correspondencia
from appcer2.models import Residencia
from django.db.models import Q
# Create your views here.
def home(request):
    return render(request,'appcer2/home.html')

def correspondencia(request):
    busqueda = request.GET.get("buscar")
    correspondencias = Correspondencia.objects.all()
    if busqueda:
        correspondencias = Correspondencia.objects.filter(
            Q(direccion = busqueda)
        ).distinct()
    
    return render(request,'appcer2/correspondencia.html',{"corres":correspondencias},)
