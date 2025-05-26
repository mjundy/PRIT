from django.forms import BaseModelForm
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.timezone import now

# Create your views here.
from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView, View
from .models import PR, StatusPR
from .forms import PRForm, StatusPRForm
from django.db import models
from django.utils.timezone import now
from django.db.models import Q
from CatatPRApp.resources import PRResource, ReceivedPRResource


#export data PR yang masih open/Outstanding
def export_os_pr_xls(request):
    pr = PRResource()
    dataset = pr.export()
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    response['Content-Disposition']= 'attachment; filename=os_pr.xlsx'
    return response

#export data PR yang sudah selesai/Received
def export_received_pr_xls(request):
    pr = ReceivedPRResource()
    dataset = pr.export()
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    response['Content-Disposition']= 'attachment; filename=received_pr.xlsx'
    return response

class ListPR(ListView):
    template_name = 'crud_pr/tables.html'
    model = PR
    context_object_name = "list_pr"

    def get_context_data(self, **kwargs):
        # Memanggil context default dari superclass
        context = super().get_context_data(**kwargs)
        
        # Memfilter item yang tidak memiliki status "Received"
        filtered_list_pr = self.model.objects.filter(
            Q(status__status="Waiting Approval") | Q(status__status="Sent to Purchase")
        )

        for item in filtered_list_pr:

            # Logika untuk 'tgl_pr'
            if item.tgl_sent_to_purchase:
                # Menghitung umur dalam hari
                item.age = (now().date() - item.tgl_sent_to_purchase).days
                
                # Menentukan apakah expired
                item.expired = item.age > 30
            else:
                # Set nilai default jika tgl_pr tidak ada
                item.age = None
                item.expired = False

        # Menambahkan filtered_list_pr ke context
        context['list_pr'] = filtered_list_pr

        return context
    
    def form_valid(self, form):
        status = form.cleaned_data['status']  # Akses cleaned_data dengan bracket
        id_status = get_object_or_404(StatusPR, status=status)  # Ambil status dari model
        
        if id_status.status == "Sent to Purchase":
            form.instance.tgl_sent_to_purchase = now()
            return super().form_valid(form)
    
class ListReceivedPR(ListView):
    template_name = 'crud_pr/received_tables.html'
    model = PR
    context_object_name = "list_received_pr"

    def get_context_data(self, **kwargs):
        # Memanggil context default dari superclass
        context = super().get_context_data(**kwargs)
        
        # Memfilter item yang hanya memiliki status "Received"
        filtered_received_list_pr = self.model.objects.filter(status__status="Received")

        # Menambahkan filtered_list_pr ke context
        context['list_received_pr'] = filtered_received_list_pr

        return context   
    
class ListCanceledPR(ListView):
    template_name = 'crud_pr/canceled_tables.html'
    model = PR
    context_object_name = "list_canceled_pr"

    def get_context_data(self, **kwargs):
        # Memanggil context default dari superclass
        context = super().get_context_data(**kwargs)
        
        # Memfilter item yang hanya memiliki status "Received"
        filtered_canceled_list_pr = self.model.objects.filter(status__status="Canceled")

        # Menambahkan filtered_list_pr ke context
        context['list_canceled_pr'] = filtered_canceled_list_pr

        return context   

class RegisterPR(CreateView):
    template_name = 'crud_pr/register.html'
    model = PR
    #fields = ['tgl_pr', 'partnumber', 'partname', 'qty', 'status', 'delete']
    form_class = PRForm
    success_url = '/'

class UpdatePR(UpdateView):
    template_name = 'crud_pr/register.html'
    model = PR
    #fields = ['tgl_pr', 'partnumber', 'partname', 'qty', 'status', 'delete']
    form_class = PRForm
    success_url = '/'

    def form_valid(self, form):
        status = form.cleaned_data['status']  # Akses cleaned_data dengan bracket
        id_status = get_object_or_404(StatusPR, status=status)  # Ambil status dari model
        
        if id_status.status == "Sent to Purchase":
            form.instance.tgl_sent_to_purchase = now()
        elif id_status.status == "Received":
            form.instance.tgl_terima = now()

        return super().form_valid(form)

class DeletePR(DeleteView):
    #template_name = 'register.html'
    model = PR
    #fields = ['tgl_pr', 'partnumber', 'partname', 'qty', 'status', 'delete']
    #form_class = PRForm
    success_url = '/'

#Class untuk Status    

class ListStatusPR(ListView):
    template_name = 'crud_status_pr/tables.html'
    model = StatusPR
    context_object_name = "list_status_pr"

class RegisterStatusPR(CreateView):
    template_name = 'crud_status_pr/register.html'
    model = StatusPR
    #fields = ['tgl_pr', 'partnumber', 'partname', 'qty', 'status', 'delete']
    form_class = StatusPRForm
    success_url = reverse_lazy('list_status_pr')

class UpdateStatusPR(UpdateView):
    template_name = 'crud_status_pr/register.html'
    model = StatusPR
    #fields = ['tgl_pr', 'partnumber', 'partname', 'qty', 'status', 'delete']
    form_class = StatusPRForm
    success_url = reverse_lazy('list_status_pr')

class DeleteStatusPR(DeleteView):
    #template_name = 'register.html'
    #template_name = 'crud_status_pr/register.html'
    model = StatusPR
    #fields = ['tgl_pr', 'partnumber', 'partname', 'qty', 'status', 'delete']
    #form_class = PRForm
    success_url = reverse_lazy('list_status_pr')
