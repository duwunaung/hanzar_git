from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Hanzar Admin"
admin.site.site_title = "Hanzar Admin Portal"
admin.site.index_title = "Welcome to Hanzar Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("website.urls"))
]
