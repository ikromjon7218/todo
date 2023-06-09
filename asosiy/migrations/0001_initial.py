# Generated by Django 4.2 on 2023-04-12 15:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bolim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
                ('batafsil', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Profil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=40)),
                ('tugilgan_sana', models.DateField(blank=True, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sarlavha', models.CharField(max_length=20)),
                ('batafsil', models.CharField(max_length=300)),
                ('oxirgi_muddat', models.DateField()),
                ('zarurlik', models.CharField(choices=[('shart', 'shart'), ('foydali', 'foydali'), ('hayot_mamot', 'hayot_mamot'), ('qiziqishga', 'qiziqishga')], max_length=12)),
                ('bajarildi', models.BooleanField(default=False)),
                ('sana', models.DateField(auto_now=True)),
                ('bolim', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='asosiy.bolim')),
                ('profil', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='asosiy.profil')),
            ],
        ),
        migrations.AddField(
            model_name='bolim',
            name='profil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='asosiy.profil'),
        ),
    ]
