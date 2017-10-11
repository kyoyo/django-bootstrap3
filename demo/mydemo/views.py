from django.views.generic import TemplateView,FormView
from django.http.response import HttpResponse
from .forms import IndexForm
# def index(request):
#     return HttpResponse('hello,test')

class IndexView(FormView):
    template_name = 'mydemo/index.html'
    form_class = IndexForm

