# Generated by Django 2.2.8 on 2019-12-07 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pole', '0003_auto_20191207_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='pole.Pole'),
        ),
    ]