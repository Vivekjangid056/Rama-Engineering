from django.db import models
from django.core.validators import RegexValidator

class AdminProducts(models.Model):
    name = models.CharField(max_length=200)
    product_heading = models.CharField(max_length=200)
    description_for_detailed_page1 = models.TextField(max_length=500)
    description_for_detailed_page2 = models.TextField(max_length=500)
    description_for_detailed_page3 = models.TextField(max_length=500)
    product_image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    is_active = models.BooleanField(default=False)

class AdminModules(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)
    module_image = models.ImageField(upload_to='module_images/', blank=True, null=True)
    is_active = models.BooleanField(default=False)

class AdminTeam(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    image = models.ImageField(upload_to='team_images/', blank=True, null=True)
    is_active = models.BooleanField(default=False)

class AdminBannerText(models.Model):
    heading = models.CharField(max_length=200)
    sub_heading = models.CharField(max_length=200)
    banner_image = models.ImageField(upload_to='banner_images/', null=True)
    
class AdminAboutUsSection(models.Model):
    heading = models.CharField(max_length=200)
    sub_heading = models.TextField()
    service1 = models.CharField(max_length=26, null=True, blank=True)
    service2 = models.CharField(max_length=26, null=True, blank=True)
    service3 = models.CharField(max_length=26, null=True, blank=True)
    service4 = models.CharField(max_length=26, null=True, blank=True)
    about_us_media = models.ImageField(upload_to='about_us_section/', null=True, blank=True)
   

class AdminAddress(models.Model):
    company_name = models.CharField(max_length=200)
    office_address = models.TextField(max_length=500)
    mape_url = models.CharField(max_length=1000)
    mobile_number = models.CharField( max_length=12, validators=[ RegexValidator(regex='^\d{10,12}$', message='Mobile number must be 10 to 12 digits.') ])
    email = models.EmailField(max_length=200)


class AdminLegalDocuments(models.Model):
    
    TandC = 'TandC'
    PrivacyPolicy = 'PrivacyPolicy'
    EULA = 'EULA'
    

    ROLE_CHOICES = [
        (TandC, 'TandC'),
        (PrivacyPolicy, 'PrivacyPolicy'),
        (EULA, 'EULA'),
    ]
    
    document_title = models.CharField(max_length=220)
    document_type = models.CharField(max_length=20 , choices=ROLE_CHOICES)
    heading = models.CharField(max_length=225)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.document_title
    
class AdminCounterSection(models.Model):
    heading = models.CharField(max_length=225)    
    sub_heading = models.CharField(max_length=225, null=True,blank=True)
    
    
    def __str__(self):
        return self.heading
    
class CounterItems(models.Model):
    counter_number = models.CharField(max_length=225, null=True, blank=True)
    counter_text = models.CharField(max_length=225, null=True, blank=True)
    counter_icon = models.FileField(upload_to='counter_section/', null=True, blank=True)

    def __str__(self):
        return f"{self.counter_text} ({self.counter_number})"
    
class ServicesSection(models.Model):
    heading = models.CharField(max_length=225)    
    sub_heading = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.heading
    
class ServicesItems(models.Model):
    title = models.CharField(max_length=225, null=True, blank=True)
    content = models.CharField(max_length=225, null=True, blank=True)
    icon = models.FileField(upload_to='counter_section/', null=True, blank=True)

    def __str__(self):
        return f"{self.title} ({self.content})"
    
class FeaturesSection(models.Model):
    heading = models.CharField(max_length=225)    
    sub_heading = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.heading
    
class FeaturesItems(models.Model):
    title = models.CharField(max_length=225, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    icon = models.FileField(upload_to='counter_section/', null=True, blank=True)

    def __str__(self):
        return f"{self.title} ({self.content})"
    
class TeamSection(models.Model):
    heading = models.CharField(max_length=225)    
    sub_heading = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.heading
    
class TestimonialHeading(models.Model):
    heading = models.CharField(max_length=225)    
    sub_heading = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.heading
    
class TestimonialItems(models.Model):
    name = models.CharField(max_length=225, null=True, blank=True)
    designation = models.CharField(max_length=225, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    image = models.FileField(upload_to='testimonial/', null=True, blank=True)

    def __str__(self):
        return f"{self.title} ({self.content})"
    
class ContactUs(models.Model):
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225,null=True, blank=True)
    email = models.EmailField(max_length=225)
    subject = models.CharField(max_length=225,null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.subject}"
    
class Settings(models.Model):
    phone_number = models.CharField(max_length=12, null=True, blank=True)
    email_address = models.EmailField(null=True, blank=True)
    address = models.CharField(max_length=225,null=True,blank=True)
    content = models.TextField(null=True,blank=True)
    footer_logo = models.FileField(upload_to='logo/',null=True,blank=True)

class EnquiryEmail(models.Model):
    email = models.EmailField(max_length=200)

    def save(self, *args, **kwargs):
        # Ensure only one instance of the model exists
        if EnquiryEmail.objects.exists():
            # Delete the existing instance
            EnquiryEmail.objects.all().delete()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "EnquiryEmail Model"
        verbose_name_plural = "EnquiryEmail Models"