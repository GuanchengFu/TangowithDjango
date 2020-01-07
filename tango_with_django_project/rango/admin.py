from django.contrib import admin
from rango.models import Category, Page


class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}

#Generate a view in the admin page to present the information about the 
#Category and Page.

class PageAdmin(admin.ModelAdmin):
	fields = ['title', 'category', 'url', 'views']
	list_display = ('title', 'category', 'url', 'views')
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
# Register your models here.
