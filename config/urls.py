from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
]

admin.site.site_header = "Burger Shot Admin"
admin.site.site_title = "Burger Shot Admin"
admin.site.index_title = "Welcome to the Burger Shot"
