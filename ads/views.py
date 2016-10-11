from rest_framework import generics
from . import models
from . import serializers


class ListBrand(generics.ListAPIView):
    queryset = models.Brand.objects.all()
    serializer_class = serializers.BrandSerializer


class ListAds(generics.ListAPIView):
    queryset = models.PurchasedAd.objects.all()
    serializer_class = serializers.PurchasedAdSerializer


class ListSearchedAds(generics.ListAPIView):
    serializer_class = serializers.PurchasedAdSerializer

    def get_queryset(self):
        brand = self.kwargs['brand_pk']
        fromDate = self.kwargs['from_date']
        toDate = self.kwargs['to_date']

        return models.PurchasedAd.objects.filter(brand=brand, ad_date__range=(fromDate, toDate))


class ListSpecificAd(generics.ListAPIView):
    serializer_class = serializers.PurchasedAdSerializer

    def get_queryset(self):
        ad = self.kwargs['ad_pk']

        return models.PurchasedAd.objects.filter(id=ad)
