from django.contrib import admin
from django.urls import path, include

from login_app.models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    pass
admin.site.register(User, UserAdmin)

urlpatters = [
    path('admin/',admin.site.urls),
    path('login_app/', include('login_app.urls')),
]