# Generated by Django 3.2.9 on 2022-01-02 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0003_dish_homeimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='description',
            field=models.TextField(default="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,"),
        ),
    ]
