from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import request

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

@csrf_exempt
def basic_request(request):
    if request.metod == "GET":
        return JsonResponse({"status":"GET Pass"}, safe=False)
    if request.metod == "POST":
        return JsonResponse({"status":"POST Pass"}, safe=False)

@csrf_exempt
def tokenize(request):
 if request.method == "POST":
    try:
       sentence = request.POST['text']
    except:
       return JsonResponse({"error":"Input not found"}, safe=False, status=500)
    url = "https://api.aiforthai.in.th/tlexplus"
    data = {'text':sentence}
    headers = {
       'Apikey': "9WWtgoyAYigPwwz6RXNEMKWv6emxIp1g"
       }
    response = requests.post(url, data=data, headers=headers)
    reponse_json = response.json()
    return JsonResponse({"student":"student_id", "tokenize":reponse_json}, safe=False)
 return JsonResponse({"error":"Method not allowed!"}, safe=False, status=403)