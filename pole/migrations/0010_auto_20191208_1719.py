# Generated by Django 2.2.8 on 2019-12-08 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pole', '0009_auto_20191208_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poleimage',
            name='pole',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='pole.Pole'),
        ),
    ]
