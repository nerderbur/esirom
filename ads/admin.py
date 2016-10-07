from django.contrib import admin
from .models import Brand, PurchasedAd, Newspaper

# Register your models here.
admin.site.register(Brand)
admin.site.register(Newspaper)
admin.site.register(PurchasedAd)
