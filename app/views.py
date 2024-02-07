from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View,TemplateView
from app.forms import *

# Create your views here.
def  fbv(request):
    return HttpResponse('fbv are done')

class cbv(View):
    def get(self,request):
        return HttpResponse('cbv are done')
    



def fbv_render(request):
    return render(request,'fbv_render.html')


class cbv_render(View):
    def get(self,request):
        return render(request,'cbv_render.html')


def fbv_movies(request):
    EMFO=MoviesForm()
    d={'EMFO':EMFO}
    if request.method=='POST':
        DMFO=MoviesForm(request.POST)
        if DMFO.is_valid():
            DMFO.save()
            return HttpResponse('data inserted successfully....')
    return render(request,'MoviesForm.html',d)


class cbv_movies(View):
    def get(self,request):
        MFO=MoviesForm()
        d={'MFO':MFO}
        return render(request,'cbv_movies.html',d)
    
    def post(self,request):
        DMFO=MoviesForm(request.POST)
        if DMFO.is_valid():
            DMFO.save()
            return HttpResponse('data inserted successfully....')
        

class cbv_templates(TemplateView):
    class_template='cbv_templates.html'

