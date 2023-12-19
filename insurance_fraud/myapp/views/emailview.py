from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.auth.hashers import check_password,make_password
from django.shortcuts import render,redirect
from django.contrib import messages
from ..models import Client
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.utils.safestring import mark_safe
from ..models import Client
import secrets
import random
from django.http import HttpResponse


verificationCode = None

#view for sending 2-FA mail
def mailtest(request):
    global verificationCode
    verificationCode = random.randint(1000, 9999)
    subject = 'Confirm your email address'
    from_email = settings.EMAIL_HOST_USER
    
    recipient_list = [request.session.get('email')]
    context = {'verificationCode': verificationCode}
    html_content = render_to_string('two-factor-mail.html',context)

    msg = EmailMultiAlternatives(subject, html_content, from_email, recipient_list)
    msg.attach_alternative(html_content, "text/html")

    #msg.send()
    if msg.send():
            success_message = mark_safe(
           f'Dear <b>user</b>, please check your email <b>{recipient_list}</b> inbox and click on the received confirmation link to activate your account and complete the registration. <b>Note:</b> check your spam folder.'
    )
            messages.success(request, success_message)

               
    else:
            messages.error(request, f'Problem sending email to you, check if you typed it correctly.')
    return render(request, 'email_message.html')

#Email for changing password
def forgotPassword(request):
        token = secrets.token_hex(10),
        subject = 'Password reset link'
        from_email = settings.EMAIL_HOST_USER
        email = request.session.get('email')
        name = request.session.get('name')
        password = request.session.get('password')
        c_password = request.session.get('c_password')
        recipient_list = [email]
        html_content = render_to_string('forget-pass-mail.html', {
            #'User': User.name,
            'domain': get_current_site(request).domain,
            #'uid': urlsafe_base64_encode(force_bytes(name)),
            #'token': account_activation_token.make_token(name),
            'token': token,
            "protocol": 'https' if request.is_secure() else 'http'
        })
        msg = EmailMultiAlternatives(subject, html_content, from_email, recipient_list)
        msg.attach_alternative(html_content, "text/html")
        #msg.send()

        if msg.send():
            success_message = mark_safe(
           f'Dear <b>user</b>, please check your email <b>{email}</b> inbox and click on the received confirmation link to activate your account and complete the registration. <b>Note:</b> check your spam folder.'
    )
            messages.success(request, success_message)

               
        else:
            messages.error(request, f'Problem sending email to you, check if you typed it correctly.')
  
#view for changing pasword
def changePassword(request,token):
     email = email = request.session.get('email')
     return render(request,'frontend/change_password.html',{'usermail':email})

# view will check code given with code from email before login
def verify(request):
    code = request.POST.get('code')
    
    if code == str(verificationCode) and code is not None:
     #login_status = request.session['login_status'] = 1
     
     return redirect('check_fraud') #log in to the system if code is correct

    else:
     
        messages.error(request,'Invalid code')
        return render(request,'2-FA.html')
   
# Registration complete after mail verification
def activate(request,token):
    
  
    email = request.session.get('email')

    print(f"Email from session: {email}") 
    
    Client.objects.filter(email=email).update(account_status='active')
    
     #Success message for complete registration
    messages.success(request, "Registration completed, now log in to the system")
    return render(request,'frontend/log-in.html')

        

#Sending mail after filling registration form
def activate_email(request):
   
        token = secrets.token_hex(10),
        subject = 'Confirm your email address'
        from_email = settings.EMAIL_HOST_USER
   
        email = request.session.get('email')
        name = request.session.get('name')
        
        #password = request.session.get('password')
        #c_password = request.session.get('c_password')
        recipient_list = [email]
        html_content = render_to_string('email.html', {
            'name': name,
            'domain': get_current_site(request).domain,
            #'uid': urlsafe_base64_encode(force_bytes(name)),
            #'token': account_activation_token.make_token(name),
            'token': token,
            "protocol": 'https' if request.is_secure() else 'http'
        })
        msg = EmailMultiAlternatives(subject, html_content, from_email, recipient_list)
        msg.attach_alternative(html_content, "text/html")
        #msg.send()

        if msg.send():
            phone_number = request.session.get('phone_number')
            DOB = request.session.get('DOB')
            address = request.session.get('address')
            age = request.session.get('age')
            email = request.session.get('email')
            gender = request.session.get('gender')
            success_message = mark_safe(
           f'Dear <b>user</b>, please check your email <b>{email}</b> inbox and click on the received confirmation link to activate your account and complete the registration. <b>Note:</b> check your spam folder.'
    )
            messages.success(request, success_message)

               
        else:
            messages.error(request, f'Problem sending email to you, check if you typed it correctly.')


        
