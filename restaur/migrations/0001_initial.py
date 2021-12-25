# Generated by Django 4.0 on 2021-12-25 14:16

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import restaur.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='SomeOne', max_length=100)),
                ('type', models.CharField(choices=[('Individual', 'Individual'), ('Company', 'Company')], default='Individual', max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owners', to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('image', models.ImageField(default='resto/default.jpg', upload_to=restaur.models.upload_to, verbose_name='image')),
                ('rating', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restaurants', to='location.district')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='owners', to='restaur.owner')),
                ('sector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restaurants', to='location.sector')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restaurants', to='auth.user')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
