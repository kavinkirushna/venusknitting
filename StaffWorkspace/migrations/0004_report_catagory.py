# Generated by Django 2.1.2 on 2018-10-28 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AdminWorkspace', '0004_auto_20181018_0715'),
        ('StaffWorkspace', '0003_auto_20181013_2205'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='catagory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='AdminWorkspace.Catagory'),
            preserve_default=False,
        ),
    ]