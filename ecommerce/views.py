from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ecommerce_index_view(request):
    '''This function render index page of ecommerce views'''
    return HttpResponse('Welcome to  6410742321 charatphan chulapanthong views!')

def item_view(request, item_id):
    context_data = {
        "item_id": item_id
       }
    return render(request, 'index.html',context= context_data)

def home_view(request, home_id):
    context_data = {
        "home_id": home_id
       }
    return render(request, 'home.html',context= context_data)

def category_view(request, category_id):
    context_data = {
        "category_id": category_id
       }
    return render(request, 'category.html',context= context_data)

def product_view(request, product_id):
    context_data = {
        "product_id": product_id
       }
    return render(request, 'product.html',context= context_data)

def checkout_view(request, checkout_id):
    context_data = {
        "checkout_id": checkout_id
       }
    return render(request, 'checkout.html',context= context_data)

def contact_view(request, contact_id):
    context_data = {
        "checkout_id": contact_id
       }
    return render(request, 'contact.html',context= context_data)