# Generated by Django 4.1.2 on 2022-11-11 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("experiences", "0002_rename_experiencemodel_experience"),
    ]

    operations = [
        migrations.AddField(
            model_name="experience",
            name="address",
            field=models.CharField(default="", max_length=250),
        ),
        migrations.AlterField(
            model_name="experience",
            name="price",
            field=models.PositiveIntegerField(),
        ),
    ]
