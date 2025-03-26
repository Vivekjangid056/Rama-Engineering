from django.urls import path
from .views import *

app_name = 'couplers'

urlpatterns = [
    path('', home, name = "home"),
    path('admin/', admin_login, name='super-admin-login'),
    path('dashboard/', admin_dashboard, name='admin-dashboard'),
    path('logout/', logout_view, name='logout'),
    path('thank-you', thank_you, name='thank_you'),
    path('products/', AdminProductsListView.as_view(), name='admin_products_list'),
    path('products/add/', AdminProductsCreateView.as_view(), name='admin_products_create'),
    path('products/<int:pk>/edit/', AdminProductsUpdateView.as_view(), name='admin_products_update'),
    path('products/<int:pk>/delete/', AdminProductsDeleteView.as_view(), name='admin_products_delete'),
    path('modules/', AdminModulesListView.as_view(), name='admin_modules_list'),
    path('modules/add/', AdminModulesCreateView.as_view(), name='admin_modules_create'),
    path('modules/<int:pk>/edit/', AdminModulesUpdateView.as_view(), name='admin_modules_update'),
    path('modules/<int:pk>/delete/', AdminModulesDeleteView.as_view(), name='admin_modules_delete'),

    path('address/', AdminAddressListView.as_view(), name='admin_address_list'),
    path('address/add/', AdminAddressCreateView.as_view(), name='admin_address_create'),
    path('address/<int:pk>/edit/', AdminAddressUpdateView.as_view(), name='admin_address_update'),
    path('address/<int:pk>/delete/', AdminAddressDeleteView.as_view(), name='admin_address_delete'),
    
    path('document-list/', DocumentListView.as_view(), name='admin_document_list'),
    path('document/add/', DocumentCreateView.as_view(), name='admin_document_create'),
    path('document/<int:pk>/edit/', DocumentUpdateView.as_view(), name='admin_document_update'),
    path('document/<int:pk>/delete/', DocumentDeleteView.as_view(), name='admin_document_delete'),

    path('banners-text/', AdminBannerTextListView.as_view(), name='admin_banner_text_list'),
    path('banners-text/add/', AdminBannerTextCreateView.as_view(), name='admin_banner_text_create'),
    path('banners-text/<int:pk>/edit/', AdminBannerTextUpdateView.as_view(), name='admin_banner_text_update'),
    path('banners-text/<int:pk>/delete/', AdminBannerTextDeleteView.as_view(), name='admin_banner_text_delete'),
    
    path('banners-aboutus/', AdminAboutUsListView.as_view(), name='admin_about_us_list'),
    path('banners-aboutus/add/', AdminAboutUsCreateView.as_view(), name='admin_about_us_create'),
    path('banners-aboutus/<int:pk>/edit/', AdminAboutUsUpdateView.as_view(), name='admin_about_us_update'),
    path('banners-aboutus/<int:pk>/delete/', AdminAboutUsDeleteView.as_view(), name='admin_about_us_delete'),
    
    path('counter-text/', AdminCounterSectionListView.as_view(), name='admin_counter_list'),
    path('counter-text/add/', AdminCounterSectionCreateView.as_view(), name='admin_counter_create'),
    path('counter-text/<int:pk>/edit/', AdminCounterSectionUpdateView.as_view(), name='admin_counter_update'),
    path('counter-text/<int:pk>/delete/', AdminCounterSectionDeleteView.as_view(), name='admin_counter_delete'),
    
    path('counter-items/', AdminCounterItemsListView.as_view(), name='admin_items_list'),
    path('counter-items/add/', AdminCounterItemsCreateView.as_view(), name='admin_items_create'),
    path('counter-items/<int:pk>/edit/', AdminCounterItemsUpdateView.as_view(), name='admin_items_update'),
    path('counter-items/<int:pk>/delete/', AdminCounterItemsDeleteView.as_view(), name='admin_items_delete'),
    
    path('services/', ServicesSectionListView.as_view(), name='admin_services_list'),
    path('services/add/', ServicesSectionCreateView.as_view(), name='admin_services_create'),
    path('services/<int:pk>/edit/', ServicesSectionUpdateView.as_view(), name='admin_services_update'),
    path('services/<int:pk>/delete/', ServicesSectionDeleteView.as_view(), name='admin_services_delete'),
    
    path('services-items/', ServicesItemsListView.as_view(), name='services_items_list'),
    path('services-items/add/', ServicesItemsCreateView.as_view(), name='services_items_create'),
    path('services-items/<int:pk>/edit/', ServicesItemsUpdateView.as_view(), name='services_items_update'),
    path('services-items/<int:pk>/delete/', ServicesItemsDeleteView.as_view(), name='services_items_delete'),
    
    path('features-section/', FeaturesSectionListView.as_view(), name='features_list'),
    path('features-section/add/', FeaturesSectionCreateView.as_view(), name='features_create'),
    path('features-section/<int:pk>/edit/', FeaturesSectionUpdateView.as_view(), name='features_update'),
    path('features-section/<int:pk>/delete/', FeaturesSectionDeleteView.as_view(), name='features_delete'),
    
    path('features-items/', FeaturesItemsListView.as_view(), name='features_items_list'),
    path('features-items/add/', FeaturesItemsCreateView.as_view(), name='features_items_create'),
    path('features-items/<int:pk>/edit/', FeaturesItemsUpdateView.as_view(), name='features_items_update'),
    path('features-items/<int:pk>/delete/', FeaturesItemsDeleteView.as_view(), name='features_items_delete'),
    
    path('team-section/', TeamSectionListView.as_view(), name='team_section_list'),
    path('team-section/add/', TeamSectionCreateView.as_view(), name='team_section_create'),
    path('team-section/<int:pk>/edit/', TeamSectionUpdateView.as_view(), name='team_section_update'),
    path('team-section/<int:pk>/delete/', TeamSectionDeleteView.as_view(), name='team_section_delete'),
    
    path('team/', AdminTeamListView.as_view(), name='admin_team_list'),
    path('team/add/', AdminTeamCreateView.as_view(), name='admin_team_create'),
    path('team/<int:pk>/edit/', AdminTeamUpdateView.as_view(), name='admin_team_update'),
    path('team/<int:pk>/delete/', AdminTeamDeleteView.as_view(), name='admin_team_delete'),
    
    path('testimonial/', TestimonialListView.as_view(), name='admin_testimonial_list'),
    path('testimonial/add/', TestimonialCreateView.as_view(), name='admin_testimonial_create'),
    path('testimonial/<int:pk>/edit/', TestimonialUpdateView.as_view(), name='admin_testimonial_update'),
    path('testimonial/<int:pk>/delete/', TestimonialdeleteView.as_view(), name='admin_testimonial_delete'),
    
    path('testimonial-items/', TestimonialItemsListView.as_view(), name='admin_testimonial_items_list'),
    path('testimonial-items/add/', TestimonialItemsCreateView.as_view(), name='admin_testimonial_items_create'),
    path('testimonial-items/<int:pk>/edit/', TestimonialItemsUpdateView.as_view(), name='admin_testimonial_items_update'),
    path('testimonial-items/<int:pk>/delete/', TestimonialItemsdeleteView.as_view(), name='admin_testimonial_items_delete'),
    
    path('contact/', contact_us, name='contact'),
    path('connect-list/', ContactUsListView.as_view(), name='connect_list'),
    path('contact/<int:pk>/', contact_detail, name='connect_view'),
    path('contact-delete/<int:pk>/', ConnectUsdeleteView.as_view(), name='connect_delete'),
    
    path('settings/', SettingsListView.as_view(), name='settings_list'),
    path('settings/add/', SettingsCreateView.as_view(), name='settings_create'),
    path('settings/<int:pk>/edit/', SettingsUpdateView.as_view(), name='settings_update'),
    path('settings/<int:pk>/delete/', SettingsdeleteView.as_view(), name='settings_delete'),

    path('projects/', ProjectsListView.as_view(), name='admin_projects_list'),
    path('project/add/', ProjectsCreateView.as_view(), name='project_create'),
    path('project/<int:pk>/edit/', ProjectsUpdateView.as_view(), name='project_update'),
    path('project/<int:pk>/delete/', ProjectsdeleteView.as_view(), name='project_delete'),

    path('projects-text/', ProdustSectionTextListView.as_view(), name='project_text_list'),
    path('project-text/add/', ProdustSectionTextCreateView.as_view(), name='project_text_create'),
    path('project-text/<int:pk>/edit/', ProdustSectionTextUpdateView.as_view(), name='project_text_update'),
    path('project-text/<int:pk>/delete/', ProdustSectionTextdeleteView.as_view(), name='project_text_delete'),
]
