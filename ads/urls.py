from django.conf.urls import url
from . import views

app_name = 'ads'
urlpatterns = [
    # ex: /ads/
    url(r'^$', views.ListBrand.as_view(), name='brand_list'),
    url(r'^viewall/', views.ListAds.as_view(), name='ads_list'),
]
