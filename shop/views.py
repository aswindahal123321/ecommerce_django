import paypalrestsdk
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from .models import Product, Contact, Order
# Create your views here.

def index(request):
    data = Product.objects.all()
    slider = Product.objects.all()[:3]
    electric = Product.objects.filter(category = "Keyboard")
    headphones = Product.objects.filter(category = "Headphones")
    
    all_categories = Product.objects.values('category').distinct()
    all_products = []
    
    for item in all_categories:
        category = item['category']
        products = Product.objects.filter(category = category)
        all_products.append({'category':category, 'products':products})

    print(all_products)
    
    context = {
        'data': data,
        'slider': slider,
        'electric' : electric,
        'headphones': headphones,
        'all_products':all_products
        }
    return render(request, 'shop/index.html', context)




def about(request):
    return render(request, 'shop/about.html')



def contact(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        message = request.POST.get('message')
        query = Contact(email = email, message = message)
        query.save()             
    return render(request, 'shop/contact.html')



def tracker(request):
    return render(request, 'shop/tracker.html')


def search(request):
    query = request.GET.get('search')
    if query:
        allItems = Product.objects.filter(Q(product_name__icontains = query) | Q(product_desc__icontains = query) | Q(category__icontains = query))
    
    else:
        allItems = []
    
    return render(request, 'shop/search.html', {'allItems':allItems, 'query': query})



def ProductView(request, myid):
    prodView = Product.objects.filter(product_id = myid)
    return render(request, 'shop/product-view.html', {'prodView' : prodView[0], 'products': range(1,100)})
def checkout(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        fname = request.POST.get('fname')
        email = request.POST.get('email')
        address = request.POST.get('address1') + '' + request.POST.get('address2')
        zip = request.POST.get('zip')
        orderItems = request.POST.get('orderItems')
        order = Order(order_id = order_id, fname = fname, email=email, address = address, zip=zip, orderItems=orderItems)
        order.save()
    return render(request, 'shop/checkout.html')    

