from django import forms
from .models import Product
from django.core.validators import  RegexValidator
from django.forms import Form, CharField, EmailField, RegexField,ValidationError



class NameForm(forms.Form):
    your_name = forms.CharField(label="age-of-driver", max_length=100)
    zip_code = forms.CharField(label="zip-code", max_length=100)
    annual_income = forms.CharField(label="annual-income", max_length=100)
    past_num_of_claims = forms.CharField(label="past-num-of-claims", max_length=100)
    safety_rating = forms.CharField(label="safty-rating", max_length=100)
    gender = forms.CharField(label="gender", max_length=100)
    marital_status = forms.CharField(label="marital-status", max_length=100)
    high_education_ind = forms.CharField(label="high-education-ind", max_length=100)
    address_change_ind = forms.CharField(label="address-change-ind", max_length=100)
    claim_est_payout = forms.CharField(label="claim-est-payout", max_length=100)
    liab_prct = forms.CharField(label="liab-prct", max_length=100)
    witness_present_ind = forms.CharField(label="witness-present-ind", max_length=100)
    policy_report_filed_ind = forms.CharField(label="policy-report-filed-ind", max_length=100)
    accident_site = forms.CharField(label="accident-site", max_length=100)
    channel = forms.CharField(label="policy_channel", max_length=100)
    age_of_vehicle = forms.CharField(label="age-of-vehicle", max_length=100)
    vehicle_price = forms.CharField(label="vehicle-price", max_length=100)
    vehicle_weight = forms.CharField(label="vehicle-weight", max_length=100)
    vehicle_category = forms.CharField(label="vehicle-category", max_length=100)
    vehicle_color = forms.CharField(label="vehicle-color", max_length=100)
    _name_to_fitted_passthrough = forms.CharField(label="_name_to_fitted_passthrough", max_length=100)


class registration(forms.Form):
        
        name = forms.CharField(label='name',max_length=30)
        email = forms.EmailField(
                    label='email',
                    max_length=100
                    
        )
        phone_number = forms.CharField(label='phone_number')
        DOB = forms.CharField(label='DOB')
        address = forms.CharField(label='address')
        age = forms.IntegerField(label='age')
        gender = forms.CharField(label='gender')
        password = forms.CharField(label='password',max_length=255)
        c_password = forms.CharField(label='c_password',max_length=255)


class logform(forms.Form):
      
        email_login = forms.CharField(
                    label='email_login',
                    max_length=100
                    
        )

        login_password = forms.CharField(label='password_login',max_length=255)


class verify(forms.Form):
       code = forms.CharField(
              label='code',
              max_length=5
       )

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'image', 'price','description')

class Product_Upload_form(forms.ModelForm):
    name = forms.CharField(label='product_name',
                    max_length=100)
    image = forms.ImageField(label='image')
    price = forms.IntegerField(label='price')
    description = forms.CharField(label='description',max_length=500)
    class Meta:
            model = Product
            fields = ('name', 'image', 'price','description')