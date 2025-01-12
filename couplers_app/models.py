from django.db import models

# Create your models here.
class Projects(models.Model):
    name = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    date= models.DateField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} at {self.place}"


class Services(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

class Team(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    instagram = models.CharField(max_length=200, null=True, blank=True)
    facebook = models.CharField(max_length=200, null=True, blank=True)
    twitter = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} as {self.designation}"

class Products(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    product_image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

class Clients(models.Model):
    name = models.CharField(max_length=200)
    profession = models.CharField(max_length=200)
    reviews = models.CharField(max_length=400)

    def __str__(self):
        return f"{self.name} from {self.place}"

class Banner(models.Model):
    heading = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return f"{self.heading}"

class AboutUs(models.Model):
    description = models.CharField(max_length=1000)
    number_of_clients = models.IntegerField()
    number_of_projects = models.IntegerField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return f"{self.number_of_clients} clients and {self.number_of_projects} has done"

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

    def __str__(self):
        return self.email