# Generated by Django 4.1.7 on 2023-03-15 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cvmsapp', '0003_remove_addvisitor_admin_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='addvisitor',
            name='remark',
            field=models.CharField(default=None, max_length=250),
        ),
    ]