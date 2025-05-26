from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, UpdateView, DeleteView
from .models import Mesin

class Dashboard(TemplateView):
    template_name = 'index.html'

class RegisterMesin(CreateView):
    template_name = 'register-mesin.html'
    model = Mesin
    fields = ['code_machine', 'no_machine', 'description']
    success_url = '/'

class UpdateMesin(UpdateView):
    model = Mesin
    fields = ['code_machine', 'no_machine', 'description']
    template_name = 'update-mesin.html'
    success_url = '/'

class DeleteMesin(DeleteView):
    model = Mesin
    success_url = '/'

def AsyncMesin(request):
    list_mesin = Mesin.objects.all()
    return render(request, 'mesin-partial.html', {'list_mesin': list_mesin})
# Create your views here.
