from django.shortcuts import render, redirect
from .models import OrdemServico
from .forms import OrdemServicoForm
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    if request.method == 'POST':
        form = OrdemServicoForm(request.POST)
        if form.is_valid():
            nova_os = form.save(commit=False)
            nova_os.status = 'aberto'
            nova_os.save()
            return redirect('index')
    else:
        form = OrdemServicoForm()

    ordens = OrdemServico.objects.all()
    return render(request, 'index.html', {'form': form, 'ordens': ordens})
