from django.shortcuts import render

from .models import Curso

# Create your views here.
def home(request):
    return render(request, 'aplicacion/home.html')

def cursos(request):
    contexto = {'cursos': Curso.objects.all(), 'titulo': 'Reporte de Cursos', 'comisiones': ['55630', '55640'] }
    return render(request, 'aplicacion/cursos.html', contexto)

def profesores(request):
    return render(request, 'aplicacion/profesores.html')

def estudiantes(request):
    return render(request, 'aplicacion/estudiantes.html')

def entregables(request):
    return render(request, 'aplicacion/entregables.html')