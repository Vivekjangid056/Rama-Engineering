from django import forms
from .models import *


class AdminProductsForm(forms.ModelForm):
    class Meta:
        model = AdminProducts
        fields = "__all__"


class AdminModulesForm(forms.ModelForm):
    class Meta:
        model = AdminModules
        fields = "__all__"


class AdminTeamForm(forms.ModelForm):
    class Meta:
        model = AdminTeam
        fields = "__all__"


class AdminBannerSliderForm(forms.ModelForm):
    class Meta:
        model = AdminBannerSlider
        fields = "__all__"
        
class AdminBannerTextForm(forms.ModelForm):
    class Meta:
        model = AdminBannerText
        fields = "__all__"
        
class AdminAboutUsSectionForm(forms.ModelForm):
    class Meta:
        model = AdminAboutUsSection
        fields = "__all__"


class AdminAddressForm(forms.ModelForm):
    class Meta:
        model = AdminAddress
        fields = "__all__"
        
class AdminLegalDocumentsForm(forms.ModelForm):
    class Meta:
        model = AdminLegalDocuments
        fields = ['document_title', 'document_type', 'heading','content']
        
class AdminCounterSectionForm(forms.ModelForm):
    class Meta:
        model = AdminCounterSection
        fields = "__all__"

class CounterItemForm(forms.ModelForm):
    class Meta:
        model = CounterItems
        fields = "__all__"
        
class ServicesSectionForm(forms.ModelForm):
    class Meta:
        model = ServicesSection
        fields = "__all__"
        
class ServicesItemsForm(forms.ModelForm):
    class Meta:
        model = ServicesItems
        fields = "__all__"
        
class FeaturesSectionForm(forms.ModelForm):
    class Meta:
        model = FeaturesSection
        fields = "__all__"
        
class FeaturesItemsForm(forms.ModelForm):
    class Meta:
        model = FeaturesItems
        fields = "__all__"

class TeamSectionForm(forms.ModelForm):
    class Meta:
        model = TeamSection
        fields = "__all__"
        
class TestimonialHeadingForm(forms.ModelForm):
    class Meta:
        model = TestimonialHeading
        fields = "__all__"

class TestimonialItemsForm(forms.ModelForm):
    class Meta:
        model = TestimonialItems
        fields = "__all__"
                
class SettingsForm(forms.ModelForm):
    class Meta:
        model = Settings
        fields = "__all__"
