from django.contrib import admin
from . import models
# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    fields = ['title','release_year','length']
    search_fields = ['title','release_year']
    list_filter = ['release_year','title','length']
    list_display = ['title','release_year','length']
    list_editable = ['length','release_year']

class CustomerAdmin(admin.ModelAdmin):
    search_fields = ['first_name','last_name','phone']
    list_display = ['first_name','last_name','phone']

admin.site.register(models.Movie,MovieAdmin)
admin.site.register(models.Customer,CustomerAdmin)
