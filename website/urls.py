from django.urls import path

from . import views

urlpatterns = [
    path("", views.index_page, name="home"),
    path("about", views.about_page, name="about"),
    path("services", views.services_page, name="services"),
    path("skills", views.skills_page, name="skills"),
    path("contact", views.contact_page, name="contact"),
    path("send_message", views.send_message, name="send_message"),
    
]