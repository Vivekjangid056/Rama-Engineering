from django.shortcuts import render
from .models import EnquiryEmail, Products, Team, Projects, Services, Clients, Banner, AboutUs
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def home(request):
    products = Products.objects.all()
    projects = Projects.objects.all()
    team = Team.objects.all()
    services = Services.objects.all()
    clients = Clients.objects.all()
    banners = Banner.objects.all()
    aboutus = AboutUs.objects.all()

    if request.method == 'POST':
        # Handle form submission    
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        service = request.POST.get('service')
        note = request.POST.get('note')

        # Compose email
        subject = 'New Free Quote Request'
        message = f"""
        You have a new quote request:

        Name: {name}
        Email: {email}
        Mobile: {mobile}
        Service: {service}
        Special Note: {note}
        """

        # Fetch recipient email from the EnquiryEmail model
        enquiry_email = EnquiryEmail.objects.first()  # Get the only instance
        recipient_email = enquiry_email.email if enquiry_email else settings.CONTACT_EMAIL

        # Send email
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,  # The sender's email
            [recipient_email],           # The recipient's email
        )

        # Redirect or reload the page after form submission
        return HttpResponseRedirect('/')

    context = {
        'products': products,
        'projects': projects,
        'team': team,
        'services': services,
        'clients': clients,
        'banners': banners,
        'aboutus': aboutus
    }
    return render(request, 'index.html', context)

def thank_you(request):
    return render(request, 'thank_you.html')

# username = Admin
# email = arunjangid@gmail.com
# password = Arunjangid@123
