from django.conf.urls import url
from .import views

urlpatterns = [
   
    url(' ', views.index, name = 'index'), #localhost:8000/Music/''
    url(r'^(?P<var>[0-9])', views.detail, name='detail')
    
]