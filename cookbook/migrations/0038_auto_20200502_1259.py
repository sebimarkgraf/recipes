# Generated by Django 3.0.5 on 2020-05-02 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0037_userpreference_search_style'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipebook',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='recipebook',
            name='icon',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
    ]