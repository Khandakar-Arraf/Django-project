from django.db import models
import bcrypt
from django.db.models import CheckConstraint, Q, F
# Create your models here.

class Client(models.Model):

    STATUS_CHOICES = (
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    )
    GENDER_CHOICES = (
        ('male','Male'),
        ('female','Female'),
        ('other','Other')
    )
    ROLE_CHOICES=(
        ('general_user','general_user'),
        ('admin','admin'),
        ('authority','authority'),
        ('staff','staff'),
        ('investigator','investigator'),
    )

    client_id = models.AutoField(primary_key=True)
    client_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=50,default='',null=True)
    dob = models.DateField(null=True)
    address = models.CharField(max_length=255,null=True)
    gender = models.CharField(max_length=10,choices=GENDER_CHOICES,null=True)
    age = models.IntegerField(null=True)
    account_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    user_image = models.ImageField(upload_to="uploads",null=True,default=None)
    client_password = models.CharField(max_length=255,null=True)
    client_confirm_password = models.CharField(max_length=255,null=True)
    role = models.CharField(max_length=15,choices=ROLE_CHOICES,null=True)

    def is_active(self):
        return self.account_status == 'active'

    def is_inactive(self):
        return self.account_status == 'inactive'

class Client_info(models.Model):

    GENDER_CHOICES = [
        ('male','Male'),
        ('female','Female'),
        ('other','Other')
    ]

    phone_number = models.CharField(max_length=30, primary_key=True)
    claim_number = models.CharField(max_length=30)
    email = models.EmailField(max_length=50,default='')
    gender = models.CharField(max_length=10,choices=GENDER_CHOICES,null=True)
    age = models.IntegerField(null=True)

    class constraints:
        constraints = [
            models.CheckConstraint(check=models.Q(gender='M') | models.Q(gender='F'),
            name='valid_gender'
            )
            
        ]

class Product(models.Model):
    name = models.CharField(max_length=255) 
    description = models.CharField(max_length=255,default="") 
    image = models.ImageField(upload_to="uploads",null=True,default=None)
    price = models.FloatField()
    quantity = models.IntegerField(null=True)
    status = models.CharField(max_length=255,null=True)



class Claims(models.Model):
    claim_id = models.CharField(primary_key=True,max_length=40)
    claim_payout = models.FloatField(null=True)
    liability_claim_percentage = models.FloatField(null=True)
    policy_channel = models.CharField(max_length=255,null=True)
    third_party_policy = models.CharField(max_length=255,null=True)
    fraud = models.BooleanField(null=True)
    probability = models.FloatField(null=True)






class Driver_info(models.Model):
    claim_id = models.ForeignKey(Claims, on_delete=models.CASCADE)
    vehicle_id = models.CharField(primary_key=True,max_length=255)
    name = models.CharField(null=True,max_length=255)
    age = models.FloatField(null=True)
    zip_code = models.CharField(null=True,max_length=255)
    safety_rating = models.FloatField(null=True),
    number_of_claims_five_years = models.IntegerField(null=True)
    gender = models.CharField(null=True),
    marital_status = models.CharField(max_length=255,null=True)
    annual_income = models.FloatField(null=True),
    living_status = models.CharField(max_length=255,null=True)
    address_change = models.CharField(max_length=255,null=True)

class Vehicle_info(models.Model):
    vehicle_id = models.ForeignKey(Driver_info, on_delete = models.CASCADE,default='')
    claim_id = models.ForeignKey(Claims, on_delete=models.CASCADE)
    price = models.FloatField(null=True)
    weight = models.CharField(null=True,max_length=255)
    color = models.CharField(null=True,max_length=255)
    vehicle_age = models.FloatField(null=True)


class Accident_info(models.Model):
    claim_id = models.ForeignKey(Claims, on_delete=models.CASCADE)
    witness = models.BooleanField(null=True)
    accident_loaction = models.CharField(max_length=255,null=True)
    vehicle_id = models.ForeignKey(Driver_info,max_length=255,on_delete=models.CASCADE )

class Order(models.Model):
    order_id = models.CharField(primary_key=True,max_length=10)
    order_date = models.DateField(null=True)
    customer_name = models.CharField(null=True,max_length=100)
    email = models.EmailField(null=True)
    status = models.CharField(null=True,max_length=100)
    total = models.FloatField(null=True)
    gateway = models.CharField(null=True,max_length=100)

    def is_pending(self):
        return self.status == 'pending'
    
    def is_approved(self):
        return self.status == 'approved'

class Invoice(models.Model):
    invoice_id = models.CharField(primary_key=True,max_length=10)
    order_id = models.ForeignKey(Order,on_delete=models.CASCADE)
    order_date = models.DateField(null=True)
    customer_name = models.CharField(null=True,max_length=100)
    email = models.EmailField(null=True)
    gateway = models.CharField(null=True,max_length=100)

class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    transaction_number = models.CharField(null=True,max_length=255)
    phone_number = models.CharField(null=True,max_length=255)
    email = models.EmailField(null=True)
    order_id = models.ForeignKey(Order,on_delete=models.CASCADE,null=True)

from datetime import datetime

class Cart(models.Model):
   
   
    email = models.EmailField(null=True)
    item_name = models.CharField(null=True,max_length=100)
    item_price = models.CharField(null=True,max_length=100)
    total = models.FloatField(null=True)
    cart_session =models.FloatField(null=True)
    order_id = models.ForeignKey(Order,on_delete=models.CASCADE,null=True)

  

class Admin(models.Model):
    name=models.CharField(max_length=100,null=True)
    email = models.EmailField(null=True)
    password = models.CharField(max_length=100)


class Staff(models.Model):
    name=models.CharField(max_length=100,null=True)
    email = models.EmailField(null=True)
    password = models.CharField(max_length=100)

# make migration pending for this model
class BlogPost(models.Model):
    author_name = models.CharField(max_length=100,null=True)  # You can adjust the max_length as needed.
    blog_title = models.CharField(max_length=200,null=True)   # You can adjust the max_length as needed.
    user_image = models.ImageField(upload_to="uploads/blogs",null=True,default=None)
    date = models.DateField(null=True)
    writing = models.TextField(null=True) 

class Blog_comment(models.Model):
    blog_id = models.ForeignKey(BlogPost,on_delete=models.CASCADE)
    user_id = models.IntegerField(null=True)
    user_name = models.CharField(max_length=100,null=True)
    comment = models.TextField(null=True)
    comment_date = models.DateField(null=True)

class Contact_message(models.Model):
    name =  models.CharField(max_length=100,null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=100,null=True)
    subject = models.CharField(max_length=100,null=True)
    message = models.TextField(max_length=100,null=True)
    message_posted = models.DateField(null=True)

