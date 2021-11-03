from django.http.response import JsonResponse
from django.shortcuts import render
import json
from web.models import category
from web import models
import operator

# Create your views here.


def select_model(request):

    if request.is_ajax():

        a = []

        products = []

        id = request.POST['id']
        brand = request.POST['brand']
        category = request.POST['category']
        print(category)

        try:


            if id == '81456':

                model = models.product_model.objects.filter(brand_id = brand, category_id = category)
                print(model)

                for i in model:

                    data = {
                        'id':i.id,
                        'model':i.model_name
                        
                    }
                    a.append(data)

                for j in a:
                    print('model',a)

                if brand == '0':


                    selectImage = models.product.objects.filter(category_id = category)

                    
                    for j in selectImage:
                        md = models.product_model.objects.get(id = j.model_id)
                        br = models.brand.objects.get(id=j.brand_id)

                        data1 = {



                            'id':j.id,
                            'name':j.product_name,
                            'image':j.product_image.url,
                            'brand':br.brand_name,
                            'model':md.model_name,
                            'price':j.price
                        }

                        products.append(data1)


                    for i in products:
                        print(i)


                else:
                    selectImage = models.product.objects.filter(brand_id=brand, category_id= category)

                
                    br = models.brand.objects.get(id=brand)
                    

                    for j in selectImage:
                        md = models.product_model.objects.get(id = j.model_id)
                        data1 = {



                            'id':j.id,
                            'name':j.product_name,
                            'image':j.product_image.url,
                            'brand':br.brand_name,
                            'model':md.model_name,
                            'price':j.price
                        }

                        products.append(data1)


                    for i in products:
                        print(i)


            else:
                msg = 'error'

        except Exception as e:
            print('eeeeeeeeeeeeeeeeeeee',e)

    return JsonResponse({'data':a,'product':products})



def select_model_based_images(request):


    if request.is_ajax():

        a = []

        id = request.POST['id']
        brand = request.POST['brand']
        model = request.POST['model']
        category = request.POST['category']


        br = models.brand.objects.get(id = brand)
        md = models.product_model.objects.get(id = model)


        try:

            if id == '87476':

                selectImage = models.product.objects.filter(brand_id = brand,category_id = category, model_id = model)

                for i in selectImage:
                    data = {

                        'id':i.id,
                        'name':i.product_name,
                        'image':i.product_image.url,
                        'brand':br.brand_name,
                        'model':md.model_name,
                        'price':i.price
                    }
                    a.append(data)

            for i in a:
                print(a)

            else:

                pass

        except Exception as e:


            print('eeeeeeeeeee',e)

    return JsonResponse({'data':a})


def cart(request):
    if request.is_ajax():
        msg =''

        # del request.session['cartdata']
        productId = request.POST['product_id']
        productDetails = models.product.objects.get(id = productId)
        cart_p = {}
        cart_p[str(productId)]={
            'id':productId,
            'name':productDetails.product_name,
            'image':productDetails.product_image.url,
            'price':productDetails.price,
            'quantity':1,
        }


        if 'cartdata' in request.session:

            if productId in request.session['cartdata']:
                if(str(productId in request.session['cartdata'])):
                    msg = '1'
            else:
                cart_data=request.session['cartdata']
                cart_data.update(cart_p)
                request.session['cartdata'] = cart_data
                msg= '0'

        else:
            request.session['cartdata']=cart_p
            msg ='0'

            

    return JsonResponse({'data':request.session['cartdata'],'length':len(request.session['cartdata']),'msg':msg})


def cart_delete(request):


    if request.is_ajax():
        length = ''
        id = request.POST['product_id']
        pr = request.session['cartdata'][id]
        price = pr['price']
        print(pr)
        try:
            del request.session['cartdata'][id]
            request.session.modified = True
            length = len(request.session['cartdata'])
            if length > 0:
                pass
            else:
                del request.session['cartdata']

        except Exception as e:
            print(e)
    return JsonResponse({'length':length,'price':price})



def update_cart(request):

    if request.is_ajax():

        id = request.POST['id']
        productId = request.POST['product_id']
        quantity = request.POST['quantity']

        qty = ''
        price = ''
        qty1 = ''
        data = []
        subTotal = ''


        try:

            if id == '1':
                updateCart = request.session['cartdata'][productId]
                updateCart['quantity'] = quantity
                request.session.modified = True
                price = updateCart['price']


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

            else:
                updateCart = request.session['cartdata'][productId]
                updateCart['quantity'] = quantity
                request.session.modified = True
                price = updateCart['price']


                
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
            print('eeeeeee',e)

    return JsonResponse({'quantity':quantity,'price':price,'sub_total':subTotal})



############### SELECT BRAND ###################

def select_models(request):

    if request.is_ajax():
        a =[]

        brand = request.POST['brand']
        category = request.POST['category']

        model = models.product_model.objects.filter(category_id = category, brand_id = brand)

        for i in model:
            data = {
                'id':i.id,
                'model':i.model_name
            }
            a.append(data)

        return JsonResponse({'data':a})
