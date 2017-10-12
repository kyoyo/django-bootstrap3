from django.conf.urls import url
from .views import LoginView,RegisterView
from . import views

#url(r'', views.index,name='index'),

urlpatterns = [
    url(r'^login/',LoginView.as_view(),name='login'),
    url(r'^register/',RegisterView.as_view(),name='register'),
]