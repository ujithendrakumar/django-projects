from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
from basic_app.models import School, Student


class SchoolListView(ListView):
    context_object_name = 'schools'
    model = School

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = School
    template_name = 'basic_app/school_details.html'


class CBView(View):
    def get(self,request):
        return render(request,'basic_app/index.html')

class IndexView(TemplateView):
    template_name = 'basic_app/cbv.html'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = "SAMPLE INJECTION"
        return context


def index(request):
    context ={}
    return render(request,'basic_app/index.html',context)
