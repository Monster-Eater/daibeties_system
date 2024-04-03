from django.contrib import admin
from home.models import Donate, Profile
from home.models import Reports
from django.contrib.auth.models import User, Group


# Register your models here.
admin.site.register(Donate)
admin.site.register(Reports)
admin.site.register(Profile)



class ProfileInline(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    model = User    
    fields = ['username', 'first_name', 'last_name', 'email' ]
    inlines = [ProfileInline]  


admin.site.unregister(User)

admin.site.register(User, UserAdmin)

 