# Generated by Django 3.2.9 on 2022-01-04 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0005_remove_dish_homeimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dish',
            name='image',
        ),
        migrations.RemoveField(
            model_name='dish',
            name='ingredient',
        ),
        migrations.AddField(
            model_name='dishimage',
            name='dish',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dishImages', to='dishes.dish'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='description',
            field=models.TextField(default='This dish is made up eggs, oil, sugger, salt'),
        ),
        migrations.DeleteModel(
            name='Ingredient',
        ),
    ]
