from django.contrib import admin
from django.http import FileResponse
from .models import St_user, University, Degree, Post

import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter, A4

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Register your models here.

prac_period = "17.06.2022 - 08.07.2022"


@admin.action(description='Составить приложение для договора')
def make_attachment(self, request, queryset):
    documentTitle = 'Attachment'
    fName = 'templates/Attachment.pdf'
    pdfmetrics.registerFont(TTFont('timesnrcyrmt', 'templates/timesnrcyrmt.ttf'))
    
    data = []
    qs = queryset.values_list('institute', 'group', 'surname', 'name', 'patronymic')
    # qs1 = St_user.objects.filter(is_accepted='A').values('institute', 'group', 'surname', 'name', 'patronymic')
    # randlist = list(qs)
    data.append([])
    data[0].append("№")
    data[0].append("Учебное подразделение")
    data[0].append("Группа")
    data[0].append("ФИО обучающихся")
    data[0].append("Сроки практики")
    i = 1
    for item in qs:
        data.append([])
        data[i].append(str(i))
        data[i].append(item[0])
        data[i].append(item[1])
        data[i].append(item[2] + " " + item[3] + " " + item[4])
        data[i].append(prac_period)
        i += 1
    pdf = SimpleDocTemplate(
        fName,
        pagesize=A4

    )
    # pdf.setFont('Times', 12)
    table = Table(data)

    style = TableStyle([
        ('FONTNAME', (0,0), (999, 999), 'timesnrcyrmt')
    ])
    table.setStyle(style)

    elems = []
    elems.append(table)

    pdf.build(elems)

    # return FileResponse(buffer, as_attachment=True, filename=fName)


class St_userAdmin(admin.ModelAdmin):
    list_display = ('email', 'surname', 'name', 'patronymic', 'institute', 'current_degree', 'kurs', 'skills', 'reg_date', 'is_accepted')
    # list_display_links = ('surname', 'name')
    search_fields = ('skills', 'surname', 'name', 'patronymic')
    list_editable = ('is_accepted',)
    list_filter = ('is_accepted', 'institute', 'current_degree', 'reg_date',)
    actions = [make_attachment]

class UniversityAdmin(admin.ModelAdmin):
    list_display = ('uname',)

class DegreeAdmin(admin.ModelAdmin):
    list_display = ('degree_name',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'post_date', 'mod_date', 'author',)
    list_filter = ('post_date', 'mod_date', 'author')
    search_fields = ('title', 'description',)

admin.site.register(St_user, St_userAdmin)
admin.site.register(University, UniversityAdmin)
admin.site.register(Degree, DegreeAdmin)
admin.site.register(Post, PostAdmin)