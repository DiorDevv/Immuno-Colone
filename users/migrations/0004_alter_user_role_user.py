# Generated by Django 5.1.7 on 2025-03-08 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role_user',
            field=models.CharField(choices=[('TTB', 'TTB'), ('VSSB', 'VSSB'), ('Bosh_M', 'Bosh M'), ('Vazir', 'Vazir')], default='TTB', max_length=50),
        ),
    ]
