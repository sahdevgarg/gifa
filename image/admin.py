from django.contrib import admin
from image.models import Image
from django.conf import settings


class ImageAdmin(admin.ModelAdmin):
    list_display = ("title","image","team","tags","user","enabled","trivia",'rejected')
    search_fields = ['title']
admin.site.register(Image,ImageAdmin)