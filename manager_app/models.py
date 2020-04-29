from django.db import models
from login_app.models import User

class Address(models.Model):
    name= models.CharField(max_length=255)
    street= models.CharField(max_length=255)
    city= models.CharField(max_length=255)
    state= models.CharField(max_length=2)
    zip_code= models.CharField(max_length=15)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
# route = Route added

class Carrier(models.Model):
    archived= models.BooleanField(default=False)
    name= models.CharField(max_length=255)
    website= models.CharField(max_length=255, null=True)
    address=models.OneToOneField(Address, related_name="carrier_address", on_delete=models.CASCADE, null=True)
    completed_contracts= models.IntegerField(default=0)
    open_contracts= models.IntegerField(default=0)
    email= models.CharField(max_length=255)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
# phone_numbers = Phone numbers added
# comments = Comments added

class Customer(models.Model):
    archived= models.BooleanField(default=False)
    name= models.CharField(max_length=255)
    website= models.CharField(max_length=255)
    address=models.OneToOneField(Address, related_name="customer_address", on_delete=models.CASCADE, null=True)
    completed_contracts= models.IntegerField(default=0)
    open_contracts= models.IntegerField(default=0)
    email= models.CharField(max_length=255)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

class Contract(models.Model):
    trip_number= models.CharField(max_length=45, null=True)
    archived= models.BooleanField(default=False)
    status= models.CharField(max_length=255)
    carrier_cost= models.DecimalField(decimal_places= 2, max_digits=8,  null=True)
    customer_price= models.DecimalField(decimal_places= 2,max_digits=8, null=True)
    customer = models.ForeignKey(Customer, related_name="contracts", on_delete=models.CASCADE, default=None)
    carrier = models.ForeignKey(Carrier, related_name="contracts", on_delete=models.CASCADE, default=None)
    pick_up_time= models.DateTimeField()
    delivery_time= models.DateTimeField()
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
# comments = Comments added
# route = Route assigned to this contract

# comments = Comments added
class PhoneNumber(models.Model):
    number_type= models.CharField(max_length= 255)
    number= models.CharField(max_length=30)
    customer= models.ForeignKey(Customer, related_name='phone_numbers', on_delete=models.CASCADE, blank= True, null= True)
    carrier= models.ForeignKey(Carrier, related_name= 'phone_numbers', on_delete=models.CASCADE, blank= True, null= True)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

class Route(models.Model):
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    start= models.ForeignKey(Address, related_name='start_route', on_delete=models.DO_NOTHING)
    end= models.ForeignKey(Address, related_name='end_route', on_delete=models.DO_NOTHING)
    contract= models.OneToOneField(Contract, related_name='route', on_delete=models.DO_NOTHING)

class Comment(models.Model):
    content= models.TextField()
    user= models.ForeignKey(User, related_name='comments', on_delete= models.DO_NOTHING, blank= True, null= True)
    contract= models.ForeignKey(Contract, related_name='comments', on_delete=models.CASCADE, blank= True, null= True)
    customer= models.ForeignKey(Customer, related_name='comments', on_delete=models.CASCADE, blank= True, null= True)
    carrier= models.ForeignKey(Carrier, related_name= 'comments', on_delete=models.CASCADE, blank= True, null= True)
    route= models.ForeignKey(Route, related_name= 'comments', on_delete=models.CASCADE, blank= True, null= True)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)