from django.db import models
from django.db.models.base import Model
from django.utils.tree import Node



class brand(models.Model):

    choices = ('Battery','Battery'),('Display','Display'),('Touch','Touch'),('Accessories','Accessories'),('Data Cable','Data Cable')
    category =  models.CharField(choices = choices, max_length=50, default='Battery')
    brand_name = models.CharField(max_length=50)

    
    def __str__(self):
        return self.brand_name

class product_model(models.Model):

    brand = models.ForeignKey(brand,on_delete=models.CASCADE,)
    model_name = models.CharField(max_length=50)

    def __str__(self):
        return self.model_name



class product(models.Model):
    id = models.IntegerField(primary_key=True, default=9)
    choices = ('Battery','Battery'),('Display','Display'),('Touch','Touch'),('Accessories','Accessories'),('Data Cable','Data Cable')
    date = models.DateField(auto_now_add=True)
    product_name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=choices)
    brand = models.ForeignKey(brand, on_delete=models.CASCADE)
    model = models.ForeignKey(product_model, on_delete=models.CASCADE)
    product_image = models.ImageField(upload_to = 'product_image')
    price = models.IntegerField()

    def __str__(self):
        return self.product_name


    # def __str__(self):
    #     return self.brand

    # def __str__(self):
    #     return self.model


class category_image(models.Model):

    choices = ('Battery','Battery'),('Display','Display'),('Touch','Touch'),('Accessories','Accessories'),('Data Cable','Data Cable')

    category = models.CharField(max_length=50, choices=choices,unique=True)
    category_image = models.ImageField(upload_to = 'category_image')


    def __str__(self):
        return self.category

