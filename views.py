from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Reporter,Article 
from django.views import generic
from .forms import AddForm

def index(request):
    template_name = 'newsl/index.html'
    context_object_name = 'headline'
    lists = Article.objects.order_by('-pub_date')
    dicts = {'article_list':lists}
    return render(request,'newsl/index.html',dicts)
def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year=year)
    context = {'year': year, 'article_list': a_list}
    return render(request, 'newsl/year_archive.html', context)
def month_archive(request,month):
    return HttpResponse("No list")
def article_detail(request,id):
    template_name = 'newsl/content.html'
    content = Article.objects.filter(id=id)
    title = Article.objects.filter(id=id)
    c_dist = {'name': title[0].headline, 'cont': content[0].content}
    return render(request,'newsl/content.html',c_dist)

def home(request):
    return render(request, 'newsl/home.html')
def add(request):
    template_name = 'newsl/add.html'
    a = request.GET['a']
    b = request.GET['b']
    a = int(a)
    b = int(b)
    return render(request,template_name,{'sum':str(a+b)})
def lforms(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a) + int(b)))
    else:
        form = AddForm()
    return render(request,'newsl/form.html',{'form': form})
def ajax(request):
    return render(request, 'newsl/form.html')
def jax(request):
    a = request.GET['a']
    b = request.GET['b']
    a = int(a)
    b = int(b)
    return HttpResponse(str(a*b))
