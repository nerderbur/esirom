from rest_framework import serializers
from . import models


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'description',
            'website',
            'created_on',
        )
        model = models.Brand


class NewspaperSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'created_on',
        )
        model = models.Newspaper


class PurchasedAdSerializer(serializers.ModelSerializer):
    brand = BrandSerializer(read_only=True)
    newspaper = NewspaperSerializer(read_only=True)

    class Meta:
        fields = (
            'id',
            'brand',
            'package',
            'newspaper',
            'cost',
            'objective',
            'ad_date',
            'created_on',
        )
        model = models.PurchasedAd
