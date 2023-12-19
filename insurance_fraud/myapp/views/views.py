from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect,get_object_or_404
import requests
from django.http import JsonResponse
import json
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
import pickle
from ..models import Client,Product,Order,Payment,Contact_message
from pathlib import Path
from myapp import utils
import pandas as pd
from django.http import HttpResponse
from django.contrib import messages
from myapp.forms import registration,NameForm
from django.contrib.auth.hashers import BCryptPasswordHasher as bcrypt
import re
from django.contrib.auth.hashers import check_password,make_password
import pickle
from django.utils.safestring import mark_safe
from .emailview import activate,activate_email,mailtest,forgotPassword,verify
import random
from ..models import Product,Claims,Driver_info,Accident_info,Vehicle_info,Cart,BlogPost,Blog_comment
from ..forms import ProductForm
from django.db import transaction
import datetime
from django.db.models import Q

# Create your views here.



def insurances(request):
    user_credential = request.session.get('user_credential')
    return render(request,'index.html',{'user_credential':user_credential})


def delete_sessions(request, session_keys):
    for key in session_keys:
        if key in request.session:
            del request.session[key]

    # You can optionally return a response or redirect to a specific page
    return HttpResponse('')

def logout(request):
    # List of session keys to delete
    session_keys_to_delete = ['login_status', 'user_credential','user_id']

    # Call the delete_sessions function to delete the specified keys
    delete_sessions(request, session_keys_to_delete)

    # Continue with your view logic
    # ...
    return redirect('home')

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("/myapp/predict/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, "index.html", {"form": form})
project_dir = Path(__file__).resolve().parents[0]


#view for checking insurance fraud
def results(request):

    user_credential = None
    #user_credential = request.session['user_credential']
    

    
        
    
    if 'user_credential' in request.session:
        user_credential = request.session['user_credential']
        if request.method == 'POST':
            with open(project_dir / "lgr_model.pickle", "rb") as f:
                model = pickle.load(f)

            # Assuming utils.preprocess returns a dictionary
            form_data = request.POST.dict()
             # Exclude the CSRF token from the data
            
            #gender = form_data.pop('gender',None)
            preprocessed_data = utils.preprocess(form_data)

            # Convert the preprocessed data to a DataFrame for prediction
            input_data = pd.DataFrame([preprocessed_data])

            
                # Use predict method directly (without [0] indexing for probabilities)
            global predicted_class
            predicted_class = model.predict(input_data)
            global probability
            probability = model.predict_proba(input_data)[:, 1]
           

            claim_id = request.POST['claim_id']
            name = request.POST['name']
            age_of_driver = request.POST['age_of_driver']
            zip_code = request.POST['zip_code']
            annual_income = request.POST['annual_income']
            past_num_of_claims = request.POST['past_num_of_claims']
            safety_rating = request.POST['safty_rating']
            gender = request.POST['gender']
            marital_status = request.POST['marital_status']
            living_status = request.POST['living_status']
            high_education_ind = request.POST['high_education_ind']
            address_change_ind = request.POST['address_change_ind']
            claim_est_payout = request.POST['claim_est_payout']
            liab_prct = request.POST['liab_prct']
            witness_present_ind = request.POST['witness_present_ind']
            third_party_policy_filed = request.POST['policy_report_filed_ind']
            accident_site = request.POST['accident_site']
            policy_channel = request.POST['channel']
            vehicle_id = request.POST['vehicle_id']
            age_of_vehicle = request.POST['age_of_vehicle']
            vehicle_price = request.POST['vehicle_price']
            vehicle_weight = request.POST['vehicle_weight']
            vehicle_category = request.POST['vehicle_category']
            vehicle_color = request.POST['vehicle_color']



            if predicted_class[0]==1:
                claims = Claims(claim_id=claim_id,claim_payout= claim_est_payout,liability_claim_percentage = liab_prct,policy_channel=policy_channel,third_party_policy = third_party_policy_filed,fraud = True,probability = probability)
            else:
                 claims = Claims(claim_id=claim_id,claim_payout= claim_est_payout,liability_claim_percentage = liab_prct,policy_channel=policy_channel,third_party_policy = third_party_policy_filed,fraud = False,probability = probability)

            driver_info = Driver_info(claim_id = claims,vehicle_id = vehicle_id, name=name,zip_code=zip_code,number_of_claims_five_years = past_num_of_claims,marital_status = marital_status,living_status = living_status,address_change = address_change_ind)

            vehicle_info = Vehicle_info(vehicle_id = driver_info, claim_id = claims,price = vehicle_price, weight = vehicle_weight,color = vehicle_color,vehicle_age = age_of_vehicle)
            accident_info= Accident_info(claim_id = claims,witness = convert_yes_no_to_boolean(witness_present_ind),accident_loaction = accident_site,vehicle_id = driver_info)


            #return HttpResponse(vehicle_info)

            claims.save()
            driver_info.save()
            accident_info.save()
            vehicle_info.save()
            context ={
                'user_credential':user_credential,
                'probability':f'{probability[0] * 100}{predicted_class}'
            }
            
            return render(request,"result.html", context)
            #return HttpResponse(predicted_class)
            #return render(request,"result.html", {'probability': f'{probability}{predicted_class}'})


            #return redirect('check_fraud')
    else:
        messages.success(request,'You need to login to check the results')
        user_credential = None
    print(user_credential)
    return redirect('check_fraud')
    

def convert_yes_no_to_boolean(value):
    if value.lower() == 'yes':
        return True
    elif value.lower() == 'no':
        return False
    else:
        # You might want to handle other cases or raise an exception here
        return None
    

def homes(request):
    return render(request,"frontend/index-2.html")
def home(request):

    try:
        user_credential = request.session.get('user_credential')
        user = Client.objects.get(email=user_credential)
        context ={
            'user_credentials':user_credential,
            'users':user
        }
        return render(request,"frontend/homepage.html",context)
    except Client.DoesNotExist:
        return render(request,"frontend/homepage.html")

def check_fraud(request):
    return render(request,"index.html")

def login(request):
    #messages = messages.get_messages(request)  # Retrieve messages
    return  render(request,"frontend/log-in.html")




def login_user(request):
    if request.method == 'POST':
        emails = request.POST['email_login']
        password = request.POST['password_login']
        request.session['email'] = emails

        try:
            user_id = Client.objects.get(email=emails).client_id
            user = Client.objects.get(email=emails)
            
            if check_password(password,user.client_password) and user.account_status == "active":
                
                mailtest(request)  # Send mail for 2-FA code 
                request.session['user_credential'] = emails
                request.session['user_id'] = user_id
                return render(request,'2-FA.html')
            # if not check_password(password, user.client_password ):
               #messages.error(request, 'Invalid email or password or account inactive.')
            else:
                #mailtest(request)
                # Incorrect password
                messages.error(request, 'Invalid email or password or account inactive.')
        except Client.DoesNotExist:
            # User not found
            messages.error(request, 'Invalid emails or passwords.')

    return render(request, 'frontend/log-in.html')  # Replace 'login.html' with your login template file path



def resend_code(request):
    mailtest(request)
    return redirect('verify')

    

def activateEmailMessage(request):
    user = request.POST.get('name')
    email = request.POST.get('email')
    success_message = mark_safe(
        f'Dear <b>{user}</b>, please check your email <b>{email}</b> inbox and click on the received confirmation link to activate your account and complete the registration. <b>Note:</b> check your spam folder.'
    )

    messages.success(request, success_message)



def user_registration(request):
   return render(request, 'frontend/registration.html')

# view for registration
def insertuser(request):
    if request.method == 'POST':
        
        Regform = registration(request.POST)
        phone_number = request.POST.get('phone_number')
        dob = request.POST.get('DOB')
        if request.POST.get('age') == "":
             messages.error(request, 'Age cannot be empty')
        else: 
            age = int(request.POST.get('age'))
        
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        if Regform.is_valid():
            name = request.POST['name']
            email = request.POST['email']
            
            password = request.POST['password']
            c_password = request.POST['c_password']
            
        
        if request.POST.get('name') == "":
            return render(request,"frontend/registration.html",{'error_name':True})
        
   

        if request.POST.get('email') == "":
            return render(request,"frontend/registration.html",{'error_email':True})
        
       
        if request.POST.get('phone_number') == "":
             messages.error(request, 'add phone number')
        

        if request.POST.get('DOB') == "":
            messages.error(request, 'Add date of birth')
        

        if request.POST.get('address') == "":
            messages.error(request, 'Please provide your address')
        
        if request.POST.get('age') == "" or None:
            messages.error(request, 'Age cannot be empty')

        if not request.POST['age'].isdigit():
            messages.error(request, 'Age must be a number')

        if request.POST.get('gender') == "":
            messages.error(request, 'Gender is required')

        if request.POST.get('password') == "":
            return render(request,"frontend/registration.html",{'error_password':True})
        
        
        #email validation
        
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        email = request.POST['email']
        if not re.search(pattern,email):
            return render(request,"frontend/registration.html",{'error_email_valid':True})

         # Checking password matches confirm passowrd
        if password != c_password:
            messages.error(request, "Password and Confirm Password do not match.")
            return redirect('registration')  # Redirect to the registration page if passwords don't match

        if len(password)<3:
            return render(request,"frontend/registration.html",{'error_password_num':True})

       #password validation
        pattern = r'^(?=.*[a-z])(?=.*[A-Z]).+$'
        password = request.POST['password']
        if not re.search(pattern, password):
            return render(request,"frontend/registration.html",{'password_char':True})
        
        request.session['name'] = name
        request.session['email'] = email
        #return HttpResponse(request.session['email'])
        #request.session['phone_number'] = phone_number
        #request.session['DOB'] = dob
        #request.session['address'] = address
        #request.session['age'] = age
        #request.session['gender'] = gender
        #request.session['password'] = password
        #request.session['c_password'] = c_password

        hashed_password = make_password(password)
        c_hashed_password = make_password(c_password)

        activate_email(request)
        #activateEmailMessage(request)
        #return HttpResponse(request.session.get('phone_number'))
        us = Client(client_name = name, email=email, client_password=hashed_password,client_confirm_password=c_hashed_password,account_status='inactive',address=address,age=age,dob=dob,gender=gender,phone_number=phone_number,role='',user_image='' )
        us.save()
        return redirect('registration')
            
    else:
        return HttpResponse('error')
  



#def checkout(request):
    #return render(request,"frontend/checkout.html")

def faq(request):
    user_credentials = request.session.get('user_credential')
    return render(request,"frontend/faq.html",{'user_credeitals':user_credentials})

def team(request):
    return render(request,"frontend/team.html")

def policy(request):
    return render(request,"frontend/privacy-policy.html")

def testimonials(request):
    return render(request,"frontend/testimonials.html")

def conditions(request):
    return render(request,"frontend/terms-conditions.html")

def contact(request):
    user_credentials = request.session.get('user_credential')
    return render(request,"frontend/contact.html",{'user_credentials':user_credentials})

def recover_password(request):
    return render(request,"frontend/recover-password.html")

def insurance_application(request):
    return render(request,"frontend/application.html")

def forgot_password(request):
    return render(request,"frontend/forget-password.html")

#view after submitting email for reset password
def reset_password(request):
    emails = request.POST.get('email')

    try:
        user = Client.objects.get(email=emails)
        
        if user:
            
            forgotPassword(request)  # Redirect to the password change page
            
        else:
            # Incorrect password
            messages.error(request, 'Invalid email.')
    except Client.DoesNotExist:
            messages.error(request, 'Email does not exist.')
    return render(request,'frontend/forget-password.html')

#Password updated after changing password
def update_password(request):
    change_password = request.POST['change_password']
    change_ConfirmPassword = request.POST['change_confirmPassword']
    email = request.session.get('email')

    try:
        user_to_update = Client.objects.get(email=email)
        user_to_update.client_password = make_password(change_password)
        user_to_update.client_confirm_password = make_password(change_ConfirmPassword)
        user_to_update.save()
    except Client.DoesNotExist:
        messages.error("error")
    return render(request,'frontend/log-in.html',{'email_check':email})


# product upload views
def upload_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Redirect to a page showing the list of products
    else:
        form = ProductForm()
    return render(request, 'upload_product.html', {'form': form})

#view products upload
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

#sales dashboards
def sales_dashboard(request):
    return render(request,"backend/dashboards/sales.html")

#analytics dashboards
def analytics_dashboard(request):
    return render(request,"backend/dashboards/analytics.html")

#ecommerce dashboards
def ecommerce(request):
    return render(request,"backend/dashboards/ecommerce.html")



#view for cart functionality
def product_test(request):
    #products = list(Product.objects.values())
    products = list(Product.objects.values())
    product_image = Product.objects.all()
    total_prod = Product.objects.all().count()
    cartItem = list(Product.objects.values('id','name','image','price'))
    context = {
            'products': products,
            'product_image': product_image,
            'total_prod': total_prod,
            'cartItem':cartItem
        }
    return render(request,"products.html",context)



def Products(request):
    
    try:
        user_credential = request.session.get('user_credential')
        user= Client.objects.get(email = user_credential)
        products = list(Product.objects.values())
        product_image = Product.objects.all()
        total_prod = Product.objects.all().count()
        cartItem = list(Product.objects.values('id','name','image','price'))
        context = {
                'products': products,
                'product_image': product_image,
                'total_prod': total_prod,
                'cartItem':cartItem,
                'user_credentials':user_credential,
                'user':user
            }
        return render(request,"frontend/Products.html",context)
    except Client.DoesNotExist:
        products = list(Product.objects.values())
        product_image = Product.objects.all()
        total_prod = Product.objects.all().count()
        cartItem = list(Product.objects.values('id','name','image','price'))
        context = {
                'products': products,
                'product_image': product_image,
                'total_prod': total_prod,
                'cartItem':cartItem,
               
               
            }
        return render(request,"frontend/Products.html",context)
        return redirect('home')

# product quantity from database subtracted from user cart information



def order_process(request):
    json_data = cart_list
   
    
    # Iterate through the JSON data, where each item contains 'id' and 'quantity'
    for item in json_data:
        product_id = item.get('id')
        selected_quantity = item.get('quantity')

        # Retrieve the product from the database by ID
        product = Product.objects.get(pk=product_id)

        # Check if there are enough products in stock
        if product.quantity >= selected_quantity:
            # Subtract the selected quantity from the database
            product.quantity -= selected_quantity
            product.save()
            payment_process(request)
            
            messages.success(request,'Payment Successful! Your Order is waiting for approval')
            return redirect('profile')
            
        else:
            return JsonResponse({'message': 'Not enough products in Stock.'}, status=400)
    return redirect('profile')
    #return JsonResponse({'message': 'Quantity subtracted successfully.'}, status=200)

  
    

def process_cart(request,order_id):
   
    # Get the JSON data from the request.
    #json_data = request.POST.get("cart_data")
    
    #cart_session = random.randint(1000,9999)
    email = request.session.get('user_credential') # Get the currently logged-in user.
    #request.session['cart_session'] = cart_session
    # Loop through the cart items and create CartItem objects.
 
        
    with transaction.atomic():
        json_data = cart_list
        for item in json_data:
            item_name = item["name"]
            item_price = item["price"]
            

            # Create a new CartItem record for the user.
            Cart.objects.create(
                email=email,
                item_name=item_name,
                item_price=item_price,
                total=totals,
                cart_session = None,
                order_id = order_id
            )

            
        # Redirect to a confirmation page or perform any additional actions.
        return HttpResponse(email)
        return redirect("profile")
  
    


def payment_process(request):
    email = request.session.get('user_credential')
    transaction_number = request.POST['transaction_id']
    #user_name = request.POST['user_name']
    user_name = Client.objects.get(email=email).client_name
    cart_total = totals
    phone_number = request.POST['phone_number']
    gateway = request.POST['gateway']
    #return HttpResponse(cart_total)
    order_id = random.randint(1,9999)
    order = Order(order_id=order_id,order_date=datetime.date.today(),customer_name=user_name,email=email,status='pending',total=cart_total,gateway=gateway)
    order.save()
    

    payment = Payment(transaction_number = transaction_number,phone_number = phone_number, email = email,order_id=order)
    payment.save()

    process_cart(request,order)    
    
def prescription_approval(request):
    #if request.method == 'POST':
        global  list_cards_data 
        list_cards_data = request.POST.get('listCardsData')
        #cart total
        total = request.POST.get('total')
        # Convert the JSON data back to a Python object
        global list_cards
        list_cards = json.loads(list_cards_data)

        # Initialize an empty list to store the dictionaries
        list_of_dicts = []

# Check if 'list_cards' is a list (to handle dynamic input)
        if isinstance(list_cards, list):
            # Iterate through each dictionary and add it to 'list_of_dicts'
            for card in list_cards:
                list_of_dicts.append(card)
        
        # contexts
        contexts = {
            'list_cards':list_cards,
            'total':total,
            'list_of_dicts':list_of_dicts,
        }
        
        
        return render(request,"frontend/prescription_approval.html",contexts)
    #else:
        return JsonResponse({'message': 'Invalid request method'}, status=400)
    #return render(request,"frontend/prescription_approval.html")


#views for profile 
def profile(request):

    try:
        user = request.session.get('user_credential')
        order = Order.objects.filter(email=user)
       
        client = get_object_or_404(Client, email=user)
        #client = Client.objects.filter(email = user)
        context={
            'credentials':client,
            'users':user,
            'orders':order
        }
        return render(request,'frontend/profile.html',context)
    except client.DoesNotExist:
        return HttpResponse('invalid request. Please login to the account')



def update_profile(request):
    if request.method == "POST":

        user_id = request.session.get('user_id')
        user = Client.objects.get(client_id=user_id)

        user_name = request.POST['user_name']
        user_dob = request.POST['dob']
        user_email = request.POST['user_email']
        user_number = request.POST['user_number']
        user_gender = request.POST['user_gender']
        user_address = request.POST['user_address']

        user.client_name = user_name
        user.email = user_email
        user.dob = user_dob
        user.phone_number = user_number
        user.gender = user_gender
        user.address = user_address
        user.save()
        return redirect('profile')



#checkout views

#change password

def new_password(request):
    user_session = request.session.get('user_credential')
    user = Client.objects.get(email=user_session)
    real_pass = user.client_password

    
    old_pass = request.POST['old_pass']
    new_pass = request.POST['new_pass']
    con_new_pass = request.POST['con_new_pass']
    #if real_pass != old_pass:
    if not check_password(old_pass,real_pass):
        messages.error(request,'incorrect password')
        return redirect('profile')

    if con_new_pass != new_pass:
        messages.error(request,'Password do not match')
        return redirect('profile')
    else:
        user.client_password = make_password(new_pass)
        user.client_confirm_password = make_password(con_new_pass)
        user.save()
        messages.success(request,'Password Changed')
        return redirect('profile')

def profile_image(request):
    user = request.session.get('user_credential')
    image = request.FILES['user_image']

    user_image = Client.objects.get(email = user)
    user_image.user_image = image
    user_image.save()
    return redirect('profile')


def contact_message(request):
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone_number']
    subject = request.POST['msg_subject']
    message = request.POST['message']
    

    contact_message = Contact_message(name=name,email=email,phone=phone,subject=subject,message=message,message_posted=datetime.date.today())
    contact_message.save()
    messages.success(request,'Thank you for sending message, we will soon respond to your feedback.')
    return redirect('contact')



def checkout(request):
    if 'user_credential' in request.session:
        user_email = request.session['user_credential']
        try:
            user = Client.objects.get(email=user_email)  # Get user by email
        except Client.DoesNotExist:
            # Handle the case where the user does not exist
            user = None
    else:
        # Handle the case where 'user_credential' is not in the session
        user = None

    product_database = Product.objects.all()

    if request.method == 'POST':
        cart_data = request.POST.get('listCardsData', '')
        global totals # declared global only for particular views to access it
        totals = request.POST.get('total')
        try:
            global cart_list # declared global only for particular views to access it
            cart_list = json.loads(cart_data)
        except json.JSONDecodeError:
            # Handle the case where JSON decoding fails
            cart_list = []

    else:
        # Handle the case where the request method is not POST
        cart_data = ''
        
        cart_list = []

    contexts = {
        'cart_list': cart_list,
        'product_database': product_database,
        'user': user,
        'total': totals
    }
    return render(request, 'frontend/checkout.html', contexts)


#views for subscription pack
def pricing(request):
    return render(request,'frontend/pricing.html')


def invoice(request):
    email = request.session.get('user_credential')
    subject = 'Invoice'
    from_email = settings.EMAIL_HOST_USER
    
    recipient_list = email
    context = {
        'order_date':datetime.date.today(),
        'order_time': datetime.datetime.now().time()
               }
    html_content = render_to_string('invoice.html',context)
    
    msg = EmailMultiAlternatives(subject, html_content, from_email, recipient_list)
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    return HttpResponse('invoice sent')



def blog_details(request,id):
    
    user_auth = request.session.get('user_credential')
  
    blog_piece = BlogPost.objects.get(id=id) # id is id of blog content
    blog_comment = Blog_comment.objects.filter(blog_id_id=id)# id is id of blog content
    comment_count = blog_comment.count()
    comment_greater_than_1 = None
    if comment_count>1:
        comment_greater_than_1 = True
    else:
        comment_greater_than_1 = False
    context ={
        'blog_piece':blog_piece,
        'blog_comments':blog_comment,
        'comment_count':comment_count,
        'comment_greater_than_1':comment_greater_than_1,
        'user_auth': user_auth
    }
    return render(request,'frontend/blog-details.html',context)

def blog(request):
    blog_content = BlogPost.objects.all()
    user_credentials = request.session.get('user_credential')
    context = {
        'user_credentials':user_credentials,
        'blog_contents':blog_content
    }
    return render(request,'frontend/blog-grid.html',context)

def blog_comment(request):
    blog_id = request.POST['blog_id']
    #user_id = 
    if request.method == "POST" and 'user_id' in request.session:
        comment = request.POST['comment']
        blog_id = request.POST['blog_id']
        user_id = request.session.get('user_id')
        name = Client.objects.get(client_id=user_id).client_name
        comment_date = datetime.datetime.today().now()

        comments_save =  Blog_comment(user_id=user_id,user_name=name,comment=comment,comment_date=comment_date,blog_id_id = blog_id)
        comments_save.save()
        return redirect('blog_details',blog_id)
    else:
        messages.error(request,'Please login to account to comment')
    
    return redirect('blog_details',blog_id)

def delete_comment(request,comment_id,blog_id):
    comment_to_delete = Blog_comment.objects.get(id=comment_id)
    comment_to_delete.delete()
    blog_redirect = blog_id
    return redirect('blog_details',blog_redirect)
  