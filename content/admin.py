from django.contrib import admin
from .models import Section, Image, TextContent, TextContentImage

class SectionAdmin(admin.ModelAdmin):
    ordering = ['name']
    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return False

class ImageAdmin(admin.ModelAdmin):
    list_filter = ('section', 'year','textcontentimage__text_content')

class TextContentAdmin(admin.ModelAdmin):
    list_filter = ('section',)

class TextContentImageAdmin(admin.ModelAdmin):
    list_filter = ('text_content__section',)

admin.site.register(Section, SectionAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(TextContent, TextContentAdmin)
admin.site.register(TextContentImage, TextContentImageAdmin)