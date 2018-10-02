# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.

from django import forms
from django.contrib import admin
from django.core.files.images import get_image_dimensions
from stores.models import Product, Unity, Version, Category, Store, ProductInStore


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def clean_imagen(self):
        image = self.cleaned_data.get("image")

        if not imagen:
            # raise forms.ValidationError("No image!")
            pass
        else:
            w, h = get_image_dimensions(image)
            if w != 386:
                raise forms.ValidationError(
                    "La imagen que intenta subir tiene %i pixeles de ancho. El tamaño permitido es 386px" % w)
            if h != 249:
                raise forms.ValidationError(
                    "La imagen que intenta subir tiene %h pixeles de alto. El tamaño permitido es 249px" % h)
        return image


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'unity', 'quantity', 'category', 'active')
    search_fields = ('nombre', 'code')
    list_filter = ('unity', 'category', 'active')
    ordering = ('name',)
    form = ProductForm

class VersionAdmin(admin.ModelAdmin):
    list_display = ('version', 'date')

class UnityAdmin(admin.ModelAdmin):
    list_display = ('name', 'acronym')
    ordering = ('name', 'acronym')
    search_fields = ('name', 'acronym')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'active')
    ordering = ('name', 'code')
    search_fields = ('name', 'code')

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'country', 'state', 'city', 'active')
    search_fields = ('name', 'code')
    ordering = ('name', 'code')

class ProductInStoreAdmin(admin.ModelAdmin):
    list_display = ('store', 'product', 'price', 'date', 'active')
    search_fields = ('product', 'store')
    ordering = ('store', 'product')
        
    
admin.site.register(Product, ProductAdmin)
admin.site.register(Version, VersionAdmin)
admin.site.register(Unity, UnityAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(ProductInStore, ProductInStoreAdmin)



