from rest_framework import generics
from . import models
from . import serializers


class ListBrand(generics.ListAPIView):
    queryset = models.Brand.objects.all()
    serializer_class = serializers.BrandSerializer


class ListAds(generics.ListAPIView):
    queryset = models.PurchasedAd.objects.all()
    serializer_class = serializers.PurchasedAdSerializer
