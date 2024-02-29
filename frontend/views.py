import datetime
import secrets
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone
from frontend.models import logindb, contactdb,  Service, BookingDB
from backend.models import singledb
import razorpay
from django.http import HttpResponseRedirect
from django.urls import reverse




# Create your views here.
def main_view(request):
    return render(request,'index.html')

def login_view(request):
    return render(request,'login.html')

def user_sigin_in_post(request):
    if request.method=="POST":
        a=request.POST.get("Username")
        b=request.POST.get("Email")
        c=request.POST.get("Password")
        obj=logindb(Username=a,Email=b,Password=c)
        obj.save()
        return redirect(login_view)

def sign_up_save(request):
    if request.method == "POST":
        un = request.POST.get("Email")
        pwd = request.POST.get("Password")

        # Check if the user exists in the database
        if logindb.objects.filter(Email=un, Password=pwd).exists():
            request.session["Email"] = un
            request.session["Password"] = pwd
            messages.success(request, "Logged in successfully")

            # Redirect to the main view (index page)
            return redirect('main_view')
        else:
            messages.error(request, "Wrong username or password")
            return redirect('login_view')
    else:
        return redirect('login_view')


def userlogout(request):
    if "Email" in request.session:
        del request.session["Email"]
    if "Password" in request.session:
        del request.session["Password"]
    return redirect('login_view')
def service_view(request):
    single = singledb.objects.all()
    return render(request,'service.html',{"single":single})

def single_service(request,g_id):
    single = singledb.objects.get(id=g_id)
    return render(request,'single_service.html',{"single":single})


def contact_view(request):
    return render(request,'contact.html')

def contact_save(request):
    if request.method=="POST":
        a=request.POST.get("Name")
        b = request.POST.get("Email")
        c = request.POST.get("Place")
        d = request.POST.get("Message")
        obj = contactdb(Name=a, Email=b, Place=c,Message=d)
        obj.save()
        return redirect(contact_view)




def booking_view(request):
    return render(request,'booking.html')

def about_view(request):
    return render(request,'about.html')

def project_view(request):
    return render(request,'project.html')




def booking_save(request):
    if request.method == "POST":
        # Retrieve form data
        a = request.POST.get("state")
        b = request.POST.get("city")
        c = request.POST.getlist("services")
        d = request.POST.get("name")
        e = request.POST.get("phone")
        f = request.POST.get("email")
        g = request.POST.get("date")
        h = request.POST.get("total")

        # Create a BookingDB instance and save it with the Razorpay order ID
        obj = BookingDB(
            state=a,
            city=b,
            name=d,
            phone=e,
            email=f,
            date=g,
            total=h,
            razorpay_order_id=None  # Set initially to None
        )
        obj.save()

        # Initialize Razorpay client
        client = razorpay.Client(auth=("rzp_test_pPYsnBhgBlEXV8", "oXrbgaJmUg8oCLcf8RDKI9KL"))

        # Create Razorpay order
        total_amount = int(h)
        currency = 'INR'
        payment_capture = 1

        order_payload = {
            'amount': total_amount * 100,  # Amount should be in paisa, hence multiply by 100
            'currency': currency,
            'payment_capture': payment_capture
        }

        payment = client.order.create(order_payload)

        # Update the BookingDB instance with the Razorpay order ID
        obj.razorpay_order_id = payment['id']
        obj.save()

        # Continue with the rest of your code...

        return render(request, 'booking.html', {'obj': obj, 'payment': payment})

    return render(request, 'booking.html')


def success(request):
    if request.method == "POST":
        a=request.POST
        print(a)
    return render(request,'sucess.html')

def blog_view(request):
    return render(request,'blog.html')




TOKEN_EXPIRATION_MINUTES =10 # Adjust as needed

def generate_token():
    return secrets.token_urlsafe(32)




def forgot_password(request):
    if request.method == 'POST':
        em = request.POST.get('email')
        user = logindb.objects.filter(Email=em).first()
        if user:
            # Generate a unique token
            token = generate_token()
            # Set the expiration time for the token
            token_expiration = timezone.now() + datetime.timedelta(minutes=TOKEN_EXPIRATION_MINUTES)
            # Store the token and expiration time in the user object
            user.password_reset_token = token
            user.token_expiration = token_expiration
            user.save()
            # Send the email with the recovery link
            subject = "Password Reset"
            expiration_message = f"This link will expire in {TOKEN_EXPIRATION_MINUTES} minutes. Please reset your password before then."
            # Format the message with HTML for a clickable hyperlink
            message = f"Click the following link to reset your password: <a href='http://127.0.0.1:8080/frontend/change_password/{token}/'>Reset Password</a><br><br>{expiration_message}"
            frm = 'alanks002@gmail.com'  # Sender email (change accordingly)
            to = em  # Recipient email
            send_mail(subject, '', frm, [to], html_message=message)
            return render(request, 'verification.html', {'expiration_minutes': TOKEN_EXPIRATION_MINUTES})
        else:
            return HttpResponse("Sorry, this email is not registered.")
    return render(request, 'forgot_password.html')



def change_password(request, token):
    user = logindb.objects.filter(password_reset_token=token).first()
    if user:
        # Check if the token is expired
        if user.token_expiration < timezone.now():
            return HttpResponse("Sorry, the password reset link has expired.")
        if request.method == 'POST':
            p1 = request.POST.get('password')
            p2 = request.POST.get('confirm_password')
            if p1 == p2:
                # Update user's password and clear the token
                user.Password = p1
                user.password_reset_token = None
                user.token_expiration = None
                user.save()
                return redirect('login_view')  # Assuming 'loginpage' is a valid URL name
            else:
                return HttpResponse('Passwords do not match.')
        return render(request, 'change_password.html')
    else:
        return HttpResponse("Invalid or expired password reset link.")

def verification(request):
    return render(request, 'verification.html')

