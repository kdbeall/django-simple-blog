# Generated by Django 2.1 on 2018-08-27 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_simple_blog_app', '0004_entry_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='last_modified',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='published',
            field=models.BooleanField(default=False),
        ),
    ]
