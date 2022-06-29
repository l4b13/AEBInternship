from django.contrib import admin
from .models import St_user

# Register your models here.

class WebAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name', 'patronymic', 'age', 'university', 'kurs', 'skills', 'is_accepted')
    # list_display_links = ('surname', 'name')
    search_fields = ('university', 'skills', 'surname', 'name', 'patronymic')
    list_editable = ('is_accepted',)
    list_filter = ('is_accepted',)

admin.site.register(St_user, WebAdmin)