# Generated by Django 4.2 on 2023-04-14 23:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0005_alter_bolim_batafsil'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profil',
            name='user',
        ),
        migrations.RemoveField(
            model_name='plan',
            name='bolim',
        ),
        migrations.RemoveField(
            model_name='plan',
            name='profil',
        ),
        migrations.DeleteModel(
            name='Bolim',
        ),
        migrations.DeleteModel(
            name='Profil',
        ),
    ]
