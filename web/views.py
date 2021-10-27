from django.shortcuts import render

# Create your views here.
from django import template
from django.shortcuts import redirect, render
from django.http.response import HttpResponseRedirect
from django.http import HttpResponse, request
from django.template import loader
from . import models
import operator
import pywhatkit as kit
import pywhatkit


# Create your views here.


def index(request):
    template = loader.get_template('index.html')
    cartLength = ''
    try:
        cartLength = len(request.session['cartdata'])
    except:
        pass    
    category = models.category_image.objects.all()

    return HttpResponse(template.render({'category':category,'cart_length':cartLength},request))


def product_details_view(request,category):

    template = loader.get_template('display.html')
    cartLength = ''
    try:
        cartLength = len(request.session['cartdata'])
    except:
        pass
    brand = models.brand.objects.filter(category = category)
    products = models.product.objects.filter(category = category)
    # print(brand)
    return HttpResponse(template.render({'brand':brand,'product':products,'cart_length':cartLength,'category':category},request))


def cart(request):

    template = loader.get_template('cart.html')
    # del request.session['cartdata']
    cartLength = ''
    subTotal = ''
    data = []
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

        print('eeee',e)  
    try:
        cartLength = len(request.session['cartdata'])   
    except Exception as e:
        print('eeeeeee',e) 

    return HttpResponse(template.render({'cart_length':cartLength,'cart_data':data,'data':data,'total':subTotal},request))



def checkout(request):

    template = loader.get_template('checkout.html')
    subTotal = ''
    data = []
    messagestring = ''
    try:
        cartLength = len(request.session['cartdata'])

        if request.method == "POST":

            name = request.POST.get('name')
            address = request.POST.get('address')
            phone = request.POST.get('number')
        #     print('',name,address,phone)

        #     messagestring = 'https://wa.me/919656248731?text=Name:',name,'%0aAddress :%0a',address,'%0aPhone',phone
        # for i in request.session['cartdata']:
        #     selectfgf =request.session['cartdata'][i]
        
        #     data1 = {
        #         'id':selectfgf['id'],
        #         'name':selectfgf['name'],
        #         'image':selectfgf['image'],
        #         'quantity':selectfgf['quantity'],
        #         'price':selectfgf['price'],
        #         'sub_total':int(selectfgf['quantity']) * int(selectfgf['price'])               
        #     }
        #     data.append(data1)

        # for i in data:
        #     messagestring +='%0a%0aProduct-Id:',str(i['id']),'%0aName:',str(i['name']),'%0aQty:',str(i['quantity']),'%0aPrice:',str(i['price'])
               
        subTotal = sum(map(operator.itemgetter('sub_total'),data))  
        return redirect('/order_send_to_whatsaapp/'+name+'/'+address+'/'+phone) 


    except Exception as e:
        print('eeeeeeeee',e)

    return HttpResponse(template.render({'cart_length':cartLength},request))


def send_to_whatsapp(request,name,address,phone):


    template = loader.get_template('sendwhatsapp.html')
    data = []
    try:
        cartLength = len(request.session['cartdata'])
        messagestring = 'https://wa.me/0590099210?text=Name:'+name+'%0aAddress :%0a'+address+'%0aPhone'+phone

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

        for i in data:
            messagestring +='%0a[Product-Id:'+str(i['id'])+'%0aName:'+str(i['name'])+'%0aQty:'+str(i['quantity'])+'%0aPrice:'+str(i['price']+']')
               
        del request.session['cartdata']
    except:
        pass        
    return HttpResponse(template.render({'cart_length':cartLength,'link':messagestring},request))



def about(request):

    template = loader.get_template('about.html')
    try:
        cartLength = len(request.session['cartdata'])


    except:
        pass

    return HttpResponse(template.render({'cart_length':cartLength},request))


def contact(request):

    template = loader.get_template('contact.html')
    try:
        cartLength = len(request.session['cartdata'])


    except:
        pass


    return HttpResponse(template.render({'cart_length':cartLength},request))
