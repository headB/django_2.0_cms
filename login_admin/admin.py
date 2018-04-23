from django.contrib import admin
from login_admin.models import admin as login_admin
# Register your models here.


class loginAdmin(admin.ModelAdmin):
     list_display = ['id','username','last_login_ip','department','email']
    

admin.site.register(login_admin,loginAdmin)

#admin.site.register(login_admin)