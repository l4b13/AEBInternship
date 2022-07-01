# Generated by Django 4.0.5 on 2022-06-30 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_university_remove_st_user_birthdate_st_user_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='st_user',
            name='is_accepted',
            field=models.CharField(default='0', max_length=1),
        ),
        migrations.AlterField(
            model_name='st_user',
            name='university',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.university'),
        ),
    ]