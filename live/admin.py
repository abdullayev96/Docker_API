from django.contrib import admin
from .models import *


# class ImgAdmin(admin.ModelAdmin):
#     list_display = ('id', 'image', 'created')
#
#
#     ordering = ("created",)
#


class TextLeftAdmin(admin.ModelAdmin):
    list_display = ('name_left', 'text_left', 'link_left')

    list_filter = ('name_left', 'text_left')
    ordering = ("created",)


class TextRightAdmin(admin.ModelAdmin):
    list_display = ('name_right', 'text_right', 'link_right')

    list_filter = ('name_right', 'text_right')
    ordering = ("created",)

# admin.site.register(Img, ImgAdmin)
admin.site.register(TextRight, TextRightAdmin)
admin.site.register(TextLeft, TextLeftAdmin)
admin.site.register(Users)