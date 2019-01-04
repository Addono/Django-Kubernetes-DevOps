from django.contrib import admin

from image_storage import models


class TagsInline(admin.StackedInline):
    model = models.Tag
    verbose_name = "Tag"
    verbose_name_plural = "Tags"
    extra = 0  # Do not show any empty entries by default


class ImageAdmin(admin.ModelAdmin):
    inlines = [TagsInline]


admin.site.register(models.Image, ImageAdmin)
admin.site.register(models.Tag)
