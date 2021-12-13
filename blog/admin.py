from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Blog, Categories

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_filter = ("title","is_home","categories")
    list_display = ("title","is_home","is_active","slug","selected_category")
    search_fields = ("title","description",)
    list_editable = ("is_home","is_active",)
    readonly_fields = ("slug",)
    



    def selected_category(self,obj):
        #admin panel category listeleme
        html = "<ul>"

        for categories in obj.categories.all():
            html += "<li>" + categories.name + "</li>"

        html+="</ul>"

        return mark_safe(html)


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ("name","slug",)
