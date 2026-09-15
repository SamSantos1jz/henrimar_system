from django.shortcuts import render, redirect
from .models import Rotas


def home(request):
    return render(request, "cadastros/home.html")

def principal(request):
    return render(request, "cadastros/principal.html")

    
def rota(request):
   if request.method =="POST":
        nova_rota = Rotas()
        nova_rota.rota = request.POST.get('rota')
        nova_rota.motorista =request.POST.get('motorista')
        nova_rota.save()

        return redirect('rotas')

   todas_rotas = Rotas.objects.all()
   return render(request, 'cadastros/rotas.html', {'rotas':todas_rotas})