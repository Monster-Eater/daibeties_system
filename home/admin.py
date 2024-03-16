from django.contrib import admin
from home.models import Donate, Profile, MyClubUser
from home.models import Reports
from django.contrib.auth.models import User, Group


# Register your models here.
admin.site.register(Donate)
admin.site.register(Reports)
admin.site.register(MyClubUser)



class ProfileInline(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    model = User    
    fields = ['username']
    inlines = [ProfileInline]  


admin.site.register(User, UserAdmin)
admin.site.unregister(User)
admin.site.register(Profile)
 