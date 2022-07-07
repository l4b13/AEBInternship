from importlib.resources import path
from django.contrib import admin
from .models import St_user, University, Degree, Post

import io
import mimetypes
import os
import smtplib as smtp
from email.mime.text import MIMEText
from email.header import Header


from django.http import FileResponse, HttpResponse
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter, A4

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.lib.units import cm

admin.site.site_header = 'Администрирование AEB.Internship'


# Register your models here.

prac_period = "17.06.2022 - 08.07.2022"

@admin.action(description='Send E-mail')
def send_email(self, request, queryset):
    login = 'team33maet@gmail.com'
    password = 'cuhymfdwgcsxapme'

    server = smtp.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(login, password)

    subject = 'AEB.Internship'
    text = 'Поздравляем, Ваша заявка принята!\n\nПриходите в наш офис по адресу г. Якутск, ул. Ленина д.1, 2 этаж 17 июня в 10:00\n\nДополнительную информацию можете получить в нашем telegram чате \{ссылка\}'

    mime = MIMEText(text, 'plain', 'utf-8')
    mime['Subject'] = Header(subject, 'utf-8')

    qs = queryset.values_list('email',)
    for item in qs:
        server.sendmail(login, item[0], mime.as_string())


@admin.action(description='Составить приложение для договора')
def make_attachment(self, request, queryset):
    documentTitle = 'Attachment'

    fName = '../docs/Attachment.pdf'
    
    pdfmetrics.registerFont(TTFont('timesnrcyrmt', 'templates/timesnrcyrmt.ttf'))
    
    data = []
    qs = queryset.values_list('institute', 'group', 'surname', 'name', 'patronymic')
    data.append([])
    data[0].append("№")
    data[0].append("Учебное\nподразделение")
    data[0].append("Группа")
    data[0].append("ФИО обучающихся")
    data[0].append("Сроки практики")
    i = 1
    for item in qs:
        data.append([])
        data[i].append(str(i))
        data[i].append(item[0])
        data[i].append(item[1])
        data[i].append(item[2] + " " + item[3] + "\n" + item[4])
        data[i].append(prac_period)
        i += 1
    
    pdf = SimpleDocTemplate(
        fName,
        pagesize=A4,
        rightMargin=2*cm,leftMargin=2*cm,
        topMargin=2*cm,bottomMargin=2*cm
    )
    table = Table(data)

    style = TableStyle([
        ('FONTNAME', (0,0), (999, 999), 'timesnrcyrmt'),
        ('FONTSIZE', (0,0), (999, 999), 14),
        ('VALIGN', (0,0), (999, 999), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (999, 999), 9),
    ])
    table.setStyle(style)

    borders = TableStyle([
        # ('BOX', (0,0), (999, 999), 1, colors.black)
        ('GRID', (0,0), (999, 999), 1, colors.black)
    ])
    table.setStyle(borders)

    # s = " "
    # for j in range(50):
    #     s += " "
    d1 = [["                                                                          ", "Приложение №3\nк Договору практической подготовке\n№_________ от ____________"],[" ", " "]]
    t1 = Table(d1)
    t1.setStyle(style)

    d2 = [[" ", "Список обучающихся", " "],[" ", " ", " "]]
    t2 = Table(d2)
    t2.setStyle(style)

    d3 = [[" ", " "], ["Руководитель практики:                                 / Васильева Н.В.    / ", "                             "],[" ", " "],["Дата: "],]
    t3 = Table(d3)
    t3.setStyle(style)

    elems = []

    elems.append(t1)
    elems.append(t2)
    elems.append(table)
    elems.append(t3)

    pdf.build(elems)

    # path = open(fName, 'r')
    # mime_type, _ = mimetypes.guess_type(fName)
    # response = HttpResponse(path, content_type=mime_type)
    # response['Content-Disposition'] = "attachment; filename=%s" % fName
    # return response

class St_userAdmin(admin.ModelAdmin):
    list_display = ('email', 'surname', 'name', 'patronymic', 'institute', 'current_degree', 'kurs', 'skills', 'reg_date', 'is_accepted')
    # list_display_links = ('surname', 'name')
    search_fields = ('skills', 'surname', 'name', 'patronymic')
    list_editable = ('is_accepted',)
    list_filter = ('is_accepted', 'institute', 'current_degree', 'reg_date',)
    actions = [make_attachment, send_email]

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