from django.contrib import admin
from django.urls import path, include

from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/auth/", include("djoser.urls")),
    path("api/v1/auth/", include("djoser.urls.jwt")),
    path("api/v1/users/", include("backend.users.urls")),
]

admin.site.site_header = "Burger Shot Admin"
admin.site.site_title = "Burger Shot Admin"
admin.site.index_title = "Welcome to the Burger Shot"


if settings.DEBUG:
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
