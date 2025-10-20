from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Usuario

@login_required
def dashboard(request):
    # Lista de usuários da mesma conta
    agentes = Usuario.objects.filter(conta=request.user.conta)
    return render(request, 'core/dashboard.html', {
        'user': request.user,
        'agentes': agentes
    })
