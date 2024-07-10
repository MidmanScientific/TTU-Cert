from django.contrib import admin
from .models import myData
from .models  import CompanyRequest
from .models  import AutomaticLogin

# Register your models here.
admin.site.register(myData)
admin.site.register(AutomaticLogin)

@admin.register(CompanyRequest)
class CompanyRequestAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'email', 'contact', 'location', 'post_office', 'status')
    list_filter = ('status',)

