# Generated by Django 3.1.1 on 2020-10-08 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20201008_1337'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='entry_text',
            new_name='content',
        ),
        migrations.AlterField(
            model_name='entry',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]