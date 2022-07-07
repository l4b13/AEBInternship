from asyncio.windows_events import NULL
from importlib.resources import path
from django.contrib import admin
from .models import St_user, University, Degree, Post

import io
import mimetypes
import os
import datetime
import smtplib as smtp
from email.mime.text import MIMEText
from email.header import Header

from django.urls import path


from django.http import FileResponse, HttpResponse, HttpResponseRedirect
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

@admin.action(description='Игнорировать выбранные заявки')
def ignore_selected(self, request, queryset):
    queryset.update(is_accepted='I')
    self.message_user(request, "Выбранные заявки были проигнорированы.")

@admin.action(description='Принять выбранные заявки')
def accept_selected(self, request, queryset):
    queryset.update(is_accepted='A')
    self.message_user(request, "Выбранные заявки были приняты.")

@admin.action(description='Отклонить выбранные заявки')
def reject_selected(self, request, queryset):
    queryset.update(is_accepted='R')
    self.message_user(request, "Выбранные заявки были отклонены.")

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
    self.message_user(request, "Приложение к договору было создано.")

class St_userAdmin(admin.ModelAdmin):
    change_list_template = '../templates/admin/cb.html'
    list_display = ('email', 'surname', 'name', 'patronymic', 'institute', 'current_degree', 'kurs', 'skills', 'reg_date', 'is_accepted')
    # list_display_links = ('surname', 'name')
    search_fields = ('skills', 'surname', 'name', 'patronymic')
    list_editable = ('is_accepted',)
    list_filter = ('is_accepted', 'institute', 'current_degree', 'reg_date',)

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('send_email/', self.send_email),
            path('ignoreall/', self.ignoreall),
            path('acceptall/', self.acceptall),
            path('rejectall/', self.rejectall),
        ]
        return my_urls + urls

    def send_email(self, request):
        login = 'team33maet@gmail.com'
        password = 'cuhymfdwgcsxapme'

        server = smtp.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(login, password)

        qs = St_user.objects.values_list('email', 'is_accepted',)
    
        subject = 'AEB.Internship ' + str(datetime.date.today().year)

        text1 = 'Поздравляем, Ваша заявка принята!\n\nПриходите в наш офис по адресу г. Якутск, ул. Ленина д.1, 2 этаж 17 июня в 10:00.\n\nДополнительную информацию можете получить в нашем telegram чате *ссылка*\n\n\n\n--\nС уважением,\nРуководство ДИТ'
        text2 = 'Нам очень жаль, но Ваша заявка была отклонена.\n\n\n\n--\nС уважением,\nРуководство ДИТ'

        mime1 = MIMEText(text1, 'plain', 'utf-8')
        mime2 = MIMEText(text2, 'plain', 'utf-8')
        mime1['Subject'] = Header(subject, 'utf-8')
        mime2['Subject'] = Header(subject, 'utf-8')
    
        for item in qs:
            if item[1] == 'A':
                server.sendmail(login, item[0], mime1.as_string())
            elif item[1] == 'R':
                server.sendmail(login, item[0], mime2.as_string())

        self.message_user(request, "Письма были отправлены.")
        return HttpResponseRedirect("../")
    
    def ignoreall(self, request):
        self.model.objects.all().update(is_accepted='I')
        self.message_user(request, "Все заявки были проигнорированы.")
        return HttpResponseRedirect("../")

    def acceptall(self, request):
        self.model.objects.all().update(is_accepted='A')
        self.message_user(request, "Все заявки были приняты.")
        return HttpResponseRedirect("../")
    
    def rejectall(self, request):
        self.model.objects.all().update(is_accepted='R')
        self.message_user(request, "Все заявки были отклонены.")
        return HttpResponseRedirect("../")

    actions = [make_attachment, ignore_selected, accept_selected, reject_selected]

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