from django.shortcuts import render
from apps.noticia.models import Noticia
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView;
from apps.noticia.forms import UserRegisterForm
from django.urls import reverse_lazy


# def index(request):
#     return render(request,'index.html')

# def nosotros(request):
#     return render(request, 'nosotros.html') 


class NoticiaListview(ListView):
    model = Noticia
    template_name = 'index.html'

class SignUpView(CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"