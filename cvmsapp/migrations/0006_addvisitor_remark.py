# Generated by Django 4.1.7 on 2023-03-19 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cvmsapp', '0005_remove_addvisitor_remark'),
    ]

    operations = [
        migrations.AddField(
            model_name='addvisitor',
            name='remark',
            field=models.CharField(default=0, max_length=250),
        ),
    ]
