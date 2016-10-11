from django.conf.urls import url
from . import views

app_name = 'ads'
urlpatterns = [
    # ex: /ads/
    url(r'^view/(?P<ad_pk>\d+)/$', views.ListSpecificAd.as_view(), name='ad'),
    url(r'^brands/all/', views.ListBrand.as_view(), name='brand_list'),
    url(r'^viewall/', views.ListAds.as_view(), name='ads_list'),
    url(r'^results/(?P<brand_pk>\d+)/(?P<from_date>.+)/(?P<to_date>.+)/$', views.ListSearchedAds.as_view(), name='ads_list_query'),
]
