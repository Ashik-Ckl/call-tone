from django.shortcuts import render

# Create your views here.
from django import template
from django.shortcuts import redirect, render
from django.http.response import HttpResponseRedirect
from django.http import HttpResponse, request
from django.template import loader
from . import models
import operator



# Create your views here.


def index(request):
    template = loader.get_template('index.html')
    cartLength = ''
    try:
        cartLength = len(request.session['cartdata'])
    except:
        pass    
    category = models.category.objects.all()

    return HttpResponse(template.render({'category':category,'cart_length':cartLength},request))


def product_details_view(request,category):

    template = loader.get_template('display.html')
    cartLength = ''
    categoryId = models.category.objects.get(category = category)
    cId = categoryId.id
    try:
        cartLength = len(request.session['cartdata'])
    except:
        pass
    brand = models.brand.objects.all()
    products = models.product.objects.filter(category_id = categoryId.id)
    return HttpResponse(template.render({'brand':brand,'product':products,'cart_length':cartLength,'category':cId,'category_name':category},request))


def cart(request):

    template = loader.get_template('cart.html')
    cartLength = ''
    subTotal = ''
    data = []
    cartLength =''
    try:
        for i in request.session['cartdata']:
            selectfgf =request.session['cartdata'][i]
            data1 = {
                'id':selectfgf['id'],
                'name':selectfgf['name'],
                'image':selectfgf['image'],
                'quantity':selectfgf['quantity'],
                'price':selectfgf['price'],
                'sub_total':int(selectfgf['quantity']) * int(selectfgf['price'])               
            }
            data.append(data1)
        subTotal = sum(map(operator.itemgetter('sub_total'),data))

    except Exception as e:

        pass
    try:
        cartLength = len(request.session['cartdata'])   
    except Exception as e:
        pass

    return HttpResponse(template.render({'cart_length':cartLength,'cart_data':data,'data':data,'total':subTotal},request))



def checkout(request):

    template = loader.get_template('checkout.html')
    subTotal = ''
    data = []
    messagestring = ''
    cartLength =''
    try:
        cartLength = len(request.session['cartdata'])

        if request.method == "POST":

            name = request.POST.get('name')
            address = request.POST.get('address')
            phone = request.POST.get('number')
        subTotal = sum(map(operator.itemgetter('sub_total'),data))  
        return redirect('/order_send_to_whatsaapp/'+name+'/'+address+'/'+phone) 
    except Exception as e:
        pass

    return HttpResponse(template.render({'cart_length':cartLength},request))


def send_to_whatsapp(request,name,address,phone):

    template = loader.get_template('sendwhatsapp.html')
    name = name
    address = address
    phone = phone
    messagestring = ''
    grandtotal=0
    data = []
    cartLength = ''
    try:
        cartLength = len(request.session['cartdata'])
        messagestring = 'https://wa.me/9660590099210?text=Name :'+name+'%0aAddress :'+address+'%0aPhone :'+phone+\
            "%0a-----Order Details------"

        for i in request.session['cartdata']:
            selectfgf =request.session['cartdata'][i]
            
            data1 = {
                'id':selectfgf['id'],
                'name':selectfgf['name'],
                'image':selectfgf['image'],
                'quantity':selectfgf['quantity'],
                'price':selectfgf['price'],
                'sub_total':int(selectfgf['quantity']) * int(selectfgf['price'])               
            }
            data.append(data1)
            grandtotal+=int(selectfgf['quantity']) * int(selectfgf['price'])   
        for i in data:
            messagestring +="%0aProduct-Id:"+str(i['id'])+"%0aName:"+str(i['name'])+"%0aQty:"+str(i['quantity'])+"%0aPrice:"+str(i['price'])+"%0aTotal :"+str(i['sub_total'])+"%0a-----------------------------"
        messagestring+="%0a-----------------------------%0a\
        Grand Total :"+str(grandtotal)+"%0a--------------------------------"
        # del request.session['cartdata']

    except:

        pass        


    return HttpResponse(template.render({'cart_length':cartLength,'link':messagestring,'name':name,'address':address,'phone':phone},request))



def about(request):

    template = loader.get_template('about.html')
    cartLength = ''
    try:
        cartLength = len(request.session['cartdata'])
    except:
        pass
    return HttpResponse(template.render({'cart_length':cartLength},request))


def contact(request):

    template = loader.get_template('contact.html')
    cartLength =''
    try:
        cartLength = len(request.session['cartdata'])
    except:
        pass
    return HttpResponse(template.render({'cart_length':cartLength},request))




