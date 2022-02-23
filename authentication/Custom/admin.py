from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import profiles

# Register your models here.

class profileAdmin(UserAdmin):
    list_display = ('username', 'email','date_joined','last_login','is_admin','is_staff')
    search_fields=('email','username')
    readonly_fields=('id','date_joined','last_login')
    filter_horizontal=()
    list_filter=()
    fieldset=()

admin.site.register(profiles, profileAdmin)    
