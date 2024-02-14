# Generated by Django 4.1.7 on 2023-03-14 07:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cvmsapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddVisitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=150)),
                ('mobilenumber', models.IntegerField(max_length=10)),
                ('address', models.CharField(max_length=250)),
                ('whomtomeet', models.CharField(max_length=250)),
                ('department', models.CharField(max_length=250)),
                ('reasontomeet', models.CharField(max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
