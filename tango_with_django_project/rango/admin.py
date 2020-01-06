from django.contrib import admin
from rango.models import Category, Page


#Generate a view in the admin page to present the information about the 
#Category and Page.

class PageAdmin(admin.ModelAdmin):
	fields = ['title', 'category', 'url']
	list_display = ('title', 'category', 'url')
admin.site.register(Category)
admin.site.register(Page, PageAdmin)
# Register your models here.
