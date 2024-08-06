from django.urls import path

from . import views

urlpatterns = [
    path("", views.index_page, name="home"),
    path("about", views.about_page, name="about"),
    path("services", views.services_page, name="services"),
    path("skills", views.skills_page, name="skills"),
    path("contact", views.contact_page, name="contact"),
    
]