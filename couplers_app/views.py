from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.views.generic import DeleteView, ListView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404
from .forms import *
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    products = AdminProducts.objects.filter(is_active = True)
    banner_text = AdminBannerText.objects.all()
    projects = Projects.objects.all()
    project_text = ProdustSectionText.objects.all().first()
    about_us_section = AdminAboutUsSection.objects.all().first()
    counter_section = AdminCounterSection.objects.all().first()
    counter_items = CounterItems.objects.all()
    services_text = ServicesSection.objects.all().first()
    services_items = ServicesItems.objects.all()
    features_section = FeaturesSection.objects.all().first()
    features_items = FeaturesItems.objects.all()
    team_section = TeamSection.objects.all().first()
    team = AdminTeam.objects.filter(is_active = True)
    testimonial_heading = TestimonialHeading.objects.all().first()
    testimonial_items = TestimonialItems.objects.all()
    settings = Settings.objects.all().first()
    modules = AdminModules.objects.filter(is_active = True)
    addresses = AdminAddress.objects.all()
    total_modules = AdminModules.objects.all().count()
    context={
        'products':products,
        'banner_text':banner_text,
        'about_us_section':about_us_section,
        'counter_section':counter_section,
        'counter_items':counter_items,
        'services_text':services_text,
        'services_items':services_items,
        'features_section':features_section,
        'features_items':features_items,
        'team_section':team_section,
        'team':team,
        'testimonial_heading':testimonial_heading,
        'testimonial_items':testimonial_items,
        'settings':settings,
        'modules':modules,
        'addresses':addresses,
        'total_modules':total_modules,
        'projects':projects,
        'project_text':project_text
    }
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
    return render(request, 'index.html', context=context)

def thank_you(request):
    return render(request, 'thank_you.html')


def admin_login(request):
    if request.user.is_authenticated:
        return redirect("/dashboard/")
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Ensure the user is an instance of your User model
            if isinstance(user, User):
                login(request, user)
                return redirect('/dashboard/')
            else:
                messages.info(request, 'Invalid user type.')

        else:
            messages.info(request, 'Invalid email or password. Please try again.')

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    return render(request, 'admin_login.html')


@login_required
def admin_dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('couplers:super-admin-login')

# username = Admin
# email = arunjangid@gmail.com
# password = Arunjangid@123


class AdminProductsListView(LoginRequiredMixin,ListView):
    model = AdminProducts
    template_name = 'admin_products_list.html'
    context_object_name = 'products'


class AdminProductsCreateView(LoginRequiredMixin, CreateView):
    model = AdminProducts
    form_class = AdminProductsForm
    template_name = 'landing_form.html'
    success_url = reverse_lazy('couplers:admin_products_list')


class AdminProductsUpdateView(LoginRequiredMixin, UpdateView):
    model = AdminProducts
    form_class = AdminProductsForm
    template_name = 'landing_form.html'
    success_url = reverse_lazy('couplers:admin_products_list')

class AdminProductsDeleteView(LoginRequiredMixin, DeleteView):
    model = AdminProducts
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('couplers:admin_products_list')


class AdminModulesListView(LoginRequiredMixin, ListView):
    model = AdminModules
    template_name = 'admin_modules_list.html'
    context_object_name = 'modules'


class AdminModulesCreateView(LoginRequiredMixin, CreateView):
    model = AdminModules
    form_class = AdminModulesForm
    template_name = 'landing_form.html'
    success_url = reverse_lazy('couplers:admin_modules_list')


class AdminModulesUpdateView(LoginRequiredMixin, UpdateView):
    model = AdminModules
    form_class = AdminModulesForm
    template_name = 'landing_form.html'
    success_url = reverse_lazy('couplers:admin_modules_list')


class AdminModulesDeleteView(LoginRequiredMixin, DeleteView):
    model = AdminModules
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('couplers:admin_modules_list')


class AdminTeamListView(LoginRequiredMixin, ListView):
    model = AdminTeam
    template_name = 'admin_team_list.html'
    context_object_name = 'team'


class AdminTeamCreateView(LoginRequiredMixin, CreateView):
    model = AdminTeam
    form_class = AdminTeamForm
    template_name = 'landing_form.html'
    success_url = reverse_lazy('couplers:admin_team_list')


class AdminTeamUpdateView(LoginRequiredMixin, UpdateView):
    model = AdminTeam
    form_class = AdminTeamForm
    template_name = 'landing_form.html'
    success_url = reverse_lazy('couplers:admin_team_list')


class AdminTeamDeleteView(LoginRequiredMixin, DeleteView):
    model = AdminTeam
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('couplers:admin_team_list')


class AdminAddressListView(LoginRequiredMixin, ListView):
    model = AdminAddress
    template_name = 'admin_address_list.html'
    context_object_name = 'addresses'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['has_multiple_addresses'] = self.get_queryset().count() == 1
        
        return context


class AdminAddressCreateView(LoginRequiredMixin, CreateView):
    model = AdminAddress
    form_class = AdminAddressForm
    template_name = 'landing_form.html'
    success_url = reverse_lazy('couplers:admin_address_list')


class AdminAddressUpdateView(LoginRequiredMixin, UpdateView):
    model = AdminAddress
    form_class = AdminAddressForm
    template_name = 'landing_form.html'
    success_url = reverse_lazy('couplers:admin_address_list')


class AdminAddressDeleteView(LoginRequiredMixin, DeleteView):
    model = AdminAddress
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('couplers:admin_address_list')

class DocumentListView(LoginRequiredMixin, ListView):
    model = AdminLegalDocuments
    template_name = 'document_list.html'
    context_object_name = 'documents'


class DocumentCreateView(LoginRequiredMixin, CreateView):
    model = AdminLegalDocuments
    form_class = AdminLegalDocumentsForm
    template_name = 'document_form.html'
    success_url = reverse_lazy('couplers:admin_document_list')


class DocumentUpdateView(LoginRequiredMixin, UpdateView):
    model = AdminLegalDocuments
    form_class = AdminLegalDocumentsForm
    template_name = 'document_form.html'
    success_url = reverse_lazy('couplers:admin_document_list')


class DocumentDeleteView(LoginRequiredMixin, DeleteView):
    model = AdminLegalDocuments
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('couplers:admin_document_list')
    
    
class AdminBannerTextListView(LoginRequiredMixin, ListView):
    model = AdminBannerText
    template_name = 'admin_banner_text.html'
    context_object_name = 'bannerText'


class AdminBannerTextCreateView(LoginRequiredMixin, CreateView):
    model = AdminBannerText
    form_class = AdminBannerTextForm
    template_name = 'landing_form.html'
    success_url = reverse_lazy('couplers:admin_banner_text_list')


class AdminBannerTextUpdateView(LoginRequiredMixin, UpdateView):
    model = AdminBannerText
    form_class = AdminBannerTextForm
    template_name = 'landing_form.html'
    success_url = reverse_lazy('couplers:admin_banner_text_list')


class AdminBannerTextDeleteView(LoginRequiredMixin, DeleteView):
    model = AdminBannerText
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('couplers:admin_banner_text_list')
    
# ======================== ADMIN ABOUT US SECTION ================================== 
    
class AdminAboutUsListView(LoginRequiredMixin, ListView):
    model = AdminAboutUsSection
    template_name = 'admin_aboutus_list.html'
    context_object_name = 'adminAdboutUs'


class AdminAboutUsCreateView(LoginRequiredMixin, CreateView):
    model = AdminAboutUsSection
    form_class = AdminAboutUsSectionForm
    template_name = 'landing_form.html'
    success_url = reverse_lazy('couplers:admin_about_us_list')


class AdminAboutUsUpdateView(LoginRequiredMixin, UpdateView):
    model = AdminAboutUsSection
    form_class = AdminAboutUsSectionForm
    template_name = 'landing_form.html'
    success_url = reverse_lazy('couplers:admin_about_us_list')


class AdminAboutUsDeleteView(LoginRequiredMixin, DeleteView):
    model = AdminAboutUsSection
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('couplers:admin_about_us_list')
    
class AdminCounterSectionListView(LoginRequiredMixin, ListView):
    model = AdminCounterSection
    template_name = 'admin_counter_text.html'
    context_object_name = 'adminCounter'


class AdminCounterSectionCreateView(LoginRequiredMixin, CreateView):
    model = AdminCounterSection
    form_class = AdminCounterSectionForm
    template_name = 'landing_form.html'
    success_url = reverse_lazy('couplers:admin_counter_list')


class AdminCounterSectionUpdateView(LoginRequiredMixin, UpdateView):
    model = AdminCounterSection
    form_class = AdminCounterSectionForm
    template_name = 'landing_form.html'
    success_url = reverse_lazy('couplers:admin_counter_list')


class AdminCounterSectionDeleteView(LoginRequiredMixin, DeleteView):
    model = AdminCounterSection
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('couplers:admin_counter_list')    
    
class AdminCounterItemsListView(LoginRequiredMixin, ListView):
    model = CounterItems
    template_name = 'admin_counter_items.html'
    context_object_name = 'adminItems'


class AdminCounterItemsCreateView(LoginRequiredMixin, CreateView):
    model = CounterItems
    form_class = CounterItemForm
    template_name = 'landing_form.html'
    success_url = reverse_lazy('couplers:admin_items_list')


class AdminCounterItemsUpdateView(LoginRequiredMixin, UpdateView):
    model = CounterItems
    form_class = CounterItemForm
    template_name = 'landing_form.html'
    success_url = reverse_lazy('couplers:admin_items_list')


class AdminCounterItemsDeleteView(LoginRequiredMixin, DeleteView):
    model = CounterItems
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('couplers:admin_items_list')
    
class ServicesSectionListView(LoginRequiredMixin, ListView):
    model = ServicesSection
    template_name = 'admin_service.html'
    context_object_name = 'adminService'


class ServicesSectionCreateView(LoginRequiredMixin, CreateView):
    model = ServicesSection
    form_class = ServicesSectionForm
    template_name = 'landing_form.html'
    success_url = reverse_lazy('couplers:admin_services_list')


class ServicesSectionUpdateView(LoginRequiredMixin, UpdateView):
    model = ServicesSection
    form_class = ServicesSectionForm
    template_name = 'landing_form.html'
    success_url = reverse_lazy('couplers:admin_services_list')


class ServicesSectionDeleteView(LoginRequiredMixin, DeleteView):
    model = ServicesSection
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('couplers:admin_services_list')
    
# =============================== services items ===========================

class ServicesItemsListView(LoginRequiredMixin, ListView):
    model = ServicesItems
    template_name = 'admin_services_items.html'
    context_object_name = 'serviceItems'


class ServicesItemsCreateView(LoginRequiredMixin, CreateView):
    model = ServicesItems
    form_class = ServicesItemsForm
    template_name = 'landing_form.html'
    success_url = reverse_lazy('couplers:services_items_list')


class ServicesItemsUpdateView(LoginRequiredMixin, UpdateView):
    model = ServicesItems
    form_class = ServicesItemsForm
    template_name = 'landing_form.html'
    success_url = reverse_lazy('couplers:services_items_list')


class ServicesItemsDeleteView(LoginRequiredMixin, DeleteView):
    model = ServicesItems
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('couplers:services_items_list')
    
# =============================== Features services ===========================

class FeaturesSectionListView(LoginRequiredMixin, ListView):
    model = FeaturesSection
    template_name = 'admin_features_section.html'
    context_object_name = 'featuresSection'


class FeaturesSectionCreateView(LoginRequiredMixin, CreateView):
    model = FeaturesSection
    form_class = FeaturesSectionForm
    template_name = 'landing_form.html'
    success_url = reverse_lazy('couplers:features_list')


class FeaturesSectionUpdateView(LoginRequiredMixin, UpdateView):
    model = FeaturesSection
    form_class = FeaturesSectionForm
    template_name = 'landing_form.html'
    success_url = reverse_lazy('couplers:features_list')


class FeaturesSectionDeleteView(LoginRequiredMixin, DeleteView):
    model = FeaturesSection
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('couplers:features_list')
    
# =============================== Features Items ===========================

class FeaturesItemsListView(LoginRequiredMixin, ListView):
    model = FeaturesItems
    template_name = 'admin_features_items.html'
    context_object_name = 'featuresItems'


class FeaturesItemsCreateView(LoginRequiredMixin, CreateView):
    model = FeaturesItems
    form_class = FeaturesItemsForm
    template_name = 'landing_form.html'
    success_url = reverse_lazy('couplers:features_items_list')


class FeaturesItemsUpdateView(LoginRequiredMixin, UpdateView):
    model = FeaturesItems
    form_class = FeaturesItemsForm
    template_name = 'landing_form.html'
    success_url = reverse_lazy('couplers:features_items_list')


class FeaturesItemsDeleteView(LoginRequiredMixin, DeleteView):
    model = FeaturesItems
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('couplers:features_items_list')
    
# =============================== Team Sections ===========================

class TeamSectionListView(LoginRequiredMixin, ListView):
    model = TeamSection
    template_name = 'admin_team_section.html'
    context_object_name = 'teamSections'


class TeamSectionCreateView(LoginRequiredMixin, CreateView):
    model = TeamSection
    form_class = TeamSectionForm
    template_name = 'landing_form.html'
    success_url = reverse_lazy('couplers:team_section_list')


class TeamSectionUpdateView(LoginRequiredMixin, UpdateView):
    model = TeamSection
    form_class = TeamSectionForm
    template_name = 'landing_form.html'
    success_url = reverse_lazy('couplers:team_section_list')


class TeamSectionDeleteView(LoginRequiredMixin, DeleteView):
    model = TeamSection
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('couplers:team_section_list')
    
# =============================== testimonial heading Sections ===========================

class TestimonialListView(LoginRequiredMixin, ListView):
    model = TestimonialHeading
    template_name = 'admin_testimonial.html'
    context_object_name = 'testimonial'


class TestimonialCreateView(LoginRequiredMixin, CreateView):
    model = TestimonialHeading
    form_class = TestimonialHeadingForm
    template_name = 'landing_form.html'
    success_url = reverse_lazy('couplers:admin_testimonial_list')


class TestimonialUpdateView(LoginRequiredMixin, UpdateView):
    model = TestimonialHeading
    form_class = TestimonialHeadingForm
    template_name = 'landing_form.html'
    success_url = reverse_lazy('couplers:admin_testimonial_list')


class TestimonialdeleteView(LoginRequiredMixin, DeleteView):
    model = TestimonialHeading
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('couplers:admin_testimonial_list')
    
# =============================== testimonial Items Sections ===========================

class TestimonialItemsListView(LoginRequiredMixin, ListView):
    model = TestimonialItems
    template_name = 'admin_testimonial_items.html'
    context_object_name = 'testimonialItems'


class TestimonialItemsCreateView(LoginRequiredMixin, CreateView):
    model = TestimonialItems
    form_class = TestimonialItemsForm
    template_name = 'landing_form.html'
    success_url = reverse_lazy('couplers:admin_testimonial_items_list')


class TestimonialItemsUpdateView(LoginRequiredMixin, UpdateView):
    model = TestimonialItems
    form_class = TestimonialItemsForm
    template_name = 'landing_form.html'
    success_url = reverse_lazy('couplers:admin_testimonial_items_list')


class TestimonialItemsdeleteView(LoginRequiredMixin, DeleteView):
    model = TestimonialItems
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('couplers:admin_testimonial_items_list')
    
# ================================== contact us views =================================================
class ContactUsListView(LoginRequiredMixin, ListView):
    model = ContactUs
    template_name = 'connect_us.html'
    context_object_name = 'connectUs'
    
def contact_us(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # validating fields
        if first_name and email:
            ContactUs.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                subject=subject,
                message=message
            )
            return redirect('couplers:home')
    
    return render(request, 'index.html')

def contact_detail(request, pk):
    contact = get_object_or_404(ContactUs, pk=pk)
    print('contact',contact)
    return render(request, 'admin_contact_detail.html', {'contact': contact})

class ConnectUsdeleteView(LoginRequiredMixin, DeleteView):
    model = ContactUs
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('couplers:connect_list')
    
    
# =========================================== Settings Sections ===========================================

class SettingsListView(LoginRequiredMixin, ListView):
    model = Settings
    template_name = 'admin_settings.html'
    context_object_name = 'settingsItems'


class SettingsCreateView(LoginRequiredMixin, CreateView):
    model = Settings
    form_class = SettingsForm
    template_name = 'landing_form.html'
    success_url = reverse_lazy('couplers:settings_list')


class SettingsUpdateView(LoginRequiredMixin, UpdateView):
    model = Settings
    form_class = SettingsForm
    template_name = 'landing_form.html'
    success_url = reverse_lazy('couplers:settings_list')


class SettingsdeleteView(LoginRequiredMixin, DeleteView):
    model = Settings
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('couplers:settings_list')


class ProjectsListView(LoginRequiredMixin, ListView):
    model = Projects
    template_name = 'projects_list.html'
    context_object_name = 'projects'


class ProjectsCreateView(LoginRequiredMixin, CreateView):
    model = Projects
    form_class = ProjectForm
    template_name = 'landing_form.html'
    success_url = reverse_lazy('couplers:admin_projects_list')


class ProjectsUpdateView(LoginRequiredMixin, UpdateView):
    model = Projects
    form_class = ProjectForm
    template_name = 'landing_form.html'
    success_url = reverse_lazy('couplers:admin_projects_list')


class ProjectsdeleteView(LoginRequiredMixin, DeleteView):
    model = Projects
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('couplers:admin_projects_list')


class ProdustSectionTextListView(LoginRequiredMixin, ListView):
    model = ProdustSectionText
    template_name = 'projects_section_text_list.html'
    context_object_name = 'projects_text'


class ProdustSectionTextCreateView(LoginRequiredMixin, CreateView):
    model = ProdustSectionText
    form_class = ProdustSectionTextForm
    template_name = 'landing_form.html'
    success_url = reverse_lazy('couplers:project_text_list')


class ProdustSectionTextUpdateView(LoginRequiredMixin, UpdateView):
    model = ProdustSectionText
    form_class = ProdustSectionTextForm
    template_name = 'landing_form.html'
    success_url = reverse_lazy('couplers:project_text_list')


class ProdustSectionTextdeleteView(LoginRequiredMixin, DeleteView):
    model = ProdustSectionText
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('couplers:project_text_list')