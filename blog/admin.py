from django.contrib import admin
from . import models

# Register your models here.
class Article1Admin(admin.ModelAdmin):
	list_display = ('title','content','pub_time')
	list_filter = ('pub_time',)

admin.site.register(models.Article1,Article1Admin)