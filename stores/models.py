# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


def path_and_rename(path):
    def wrapper(instance, filename):
        ext = filename.split('.')[-1]
        # get filename
        if instance.pk:
            filename = '{}.{}'.format(instance.pk, ext)
        else:
            # set filename as random string
            filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(path, filename)
    return wrapper


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Version(models.Model):
    version = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return (str(self.version)+". "+str(self.date))


class Unit(models.Model):
    name = models.CharField(max_length=200)
    acronym = models.CharField(max_length=45)
    class Meta:
        verbose_name_plural = "Units"
    def __unicode__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200, help_text='Name of category')
    code = models.CharField(max_length=45, help_text='Code of category')
    active = models.BooleanField(default=True)
    class Meta:
        verbose_name_plural = "Categories"
    def __unicode__(self):
        return "[%s] %s" % (self.code, self.name)


class Product (models.Model):
    name = models.CharField(max_length=200, help_text='Name of product')
    code = models.CharField(max_length=45, help_text='Code of product')
    image = models.ImageField(blank=True, null=True, upload_to='products', help_text='386x249')
    unit = models.ForeignKey(Unit, related_name='products', on_delete=models.CASCADE)
    quantity = models.CharField(max_length=5)
    category = models.ForeignKey(Category, related_name='products_category', blank=False, null=True, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return "[%s] %s" % (self.code, self.name)

class Store(models.Model):
    name = models.CharField(max_length=200,)
    code = models.CharField(max_length=45, help_text='Code of store', blank=False, null=False)
    country = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    def __unicode__(self):
        return "[%s] %s" % (self.code, self.name)

class ProductInStore(models.Model):
    store = models.ForeignKey(Store, related_name='productInStore_store', blank=False, null=False, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='productInStore_product', blank=False, null=False, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    price = models.PositiveIntegerField(blank=False, null=False)
    active = models.BooleanField(default=True)
    def __unicode__(self):
        return "[%s] %s" % (self.store.name, self.store.name)
        

@receiver(post_save, sender=Product, dispatch_uid="update_version")
def update_version(sender, instance=None, **kwargs):
    Version.objects.create()