from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Product, Category, NewRelease

# Create your views here.

def landingpage(req):
    template = loader.get_template('base.html')

    products = Product.objects.all()
    categories = Category.objects.all()
    new_releases = NewRelease.objects.all()


    context = {
        'products': products,
        'categories': categories,
        'new_releases': new_releases
    }

    return HttpResponse(template.render(context, req))