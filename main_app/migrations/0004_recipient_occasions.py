# Generated by Django 4.2.7 on 2023-11-23 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_remove_gift_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipient',
            name='occasions',
            field=models.ManyToManyField(to='main_app.occasion'),
        ),
    ]
