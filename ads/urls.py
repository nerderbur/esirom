from django.conf.urls import url
from . import views

app_name = 'ads'
urlpatterns = [
    # ex: /ads/
    url(r'^$', views.index, name='index'),
]
