from django.core import serializers
from ninja import Router
from commerce.models import *

controller_commerce=Router()

@controller_commerce.get("/products")
def gitProducts(request):
    product_item= Product.objects.all()
    product_list = []
    for product in product_item:
     vendor={'name':product.vendor.name}
     merchant={'name':product.merchant.name}
     category={'name':product.category.name,'description':product.category.description,'is_active':product.category.is_active}
     label={'name':product.label.name}
     
     product_list.append({'name' : product.name, 'description' : product.description,
      "weight" : product.weight, "width" : product.width , "height" : product.height ,
      "length" : product.length , 
       "qty" : product.qty , "cost" : product.cost , "price" : product.price ,
      "discounted_price" : product.discounted_price ,
      "vendor":vendor,
       "category" : category,"merchant" : merchant , 
       "label" :  label})
    return product_list
   
@controller_commerce.get("/address")   
def gitProducts(request):
    address_item = Address.objects.all()
  
    address_list = []
    for address in address_item:     
     city = address.city.name
     address_list.append({'address1' : address.address1, 'address2' : address.address2 , 'phone' : address.phone , 'city' : city })
    return address_list    
    

     
    