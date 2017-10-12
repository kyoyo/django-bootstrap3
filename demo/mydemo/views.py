from django.views.generic import TemplateView,FormView
from django.http.response import HttpResponse
from .forms import LoginForm,RegisterForm

# def index(request):
#     return HttpResponse('hello,test')


class RegisterView(FormView):
    template_name = 'mydemo/register.html'
    form_class = RegisterForm
    success_url = '/'

    def form_invalid(self, form):
        form = RegisterForm(data=self.request.POST)

        return self.render_to_response({
            'form':form
        })

class LoginView(FormView):
    template_name = 'mydemo/login.html'
    form_class = LoginForm
    success_url = '/'

    def form_invalid(self, form):
        form = LoginForm(data=self.request.POST)

        return self.render_to_response({
            'form':form
        })



