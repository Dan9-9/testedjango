from django.shortcuts import render, get_object_or_404, redirect
from .models import contato
from .forms import contatoform 

# Create your views here.


def contato_list(request):
    contatos = contato.objects.all()
    return render(request, 'contato_list.html', {'contatos':contatos})


def create(request):
    if request.method == 'POST':
        form = contatoform(request.POST)
        if form.is_valid():
            form.save()  # Call save() to persist the form data to the database
            return redirect('contato-list')  # Redirect to the list view after saving
    else:
        form = contatoform()

    return render(request, 'criar.html', {'form': form})


def update(request, pk):
    contato_obj = get_object_or_404(contato, pk=pk)  # Use 'contato' com letra minúscula
    if request.method == 'POST':
        form = contatoform(request.POST, instance=contato_obj)  # Use 'contato_obj' como a instância
        if form.is_valid():
            form.save()
            return redirect('contato-list')
    else:
        form = contatoform(instance=contato_obj)  # Inicializa o formulário com os dados de 'contato_obj'
    return render(request, 'criar.html', {'form': form})



def delete(request, pk):
    contato_obj = get_object_or_404(contato, pk=pk)  # Use get_object_or_404 para obter um único objeto
    if request.method == 'POST':
        contato_obj.delete()  # Delete a instância do objeto
        return redirect('contato-list')
    return render(request, 'delete.html', {'contato': contato_obj})