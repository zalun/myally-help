# Generated by Django 3.0.4 on 2020-03-22 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("causes", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cause",
            name="website",
            field=models.URLField(blank=True, null=True),
        ),
    ]
