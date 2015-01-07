from django.contrib import admin
from test4.models import company,image

class companyInfoAdmin(admin.ModelAdmin):
	list_display=('id','name')
class imageInfoAdmin(admin.ModelAdmin):
	list_display=('id','name')	

admin.site.register(company,companyInfoAdmin)	
admin.site.register(image,imageInfoAdmin)	