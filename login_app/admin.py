from django.contrib import admin
from django.urls import path, include

from login_app.models import User

from manager_app.models import Comment, Contract, Customer, Carrier, PhoneNumber, Address, Route

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    pass
admin.site.register(User, UserAdmin)

class CommentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Comment, CommentAdmin)

class ContractAdmin(admin.ModelAdmin):
    pass
admin.site.register(Contract, ContractAdmin)

class CustomerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Customer, CustomerAdmin)

class CarrierAdmin(admin.ModelAdmin):
    pass
admin.site.register(Carrier, CarrierAdmin)

class PhoneNumberAdmin(admin.ModelAdmin):
    pass
admin.site.register(PhoneNumber, PhoneNumberAdmin)

class AddressAdmin(admin.ModelAdmin):
    pass
admin.site.register(Address, AddressAdmin)

class RouteAdmin(admin.ModelAdmin):
    pass
admin.site.register(Route, RouteAdmin)

urlpatters = [
    path('admin/',admin.site.urls),
    path('login_app/', include('login_app.urls')),
    path('manager_app/', include("manager_app.urls"))
]