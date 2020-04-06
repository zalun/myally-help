# Generated by Django 3.0.4 on 2020-04-04 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("causes", "0003_cause_slug"),
        ("therapists", "0005_auto_20200322_2209"),
    ]

    operations = [
        migrations.AlterField(
            model_name="therapist",
            name="causes",
            field=models.ManyToManyField(
                blank=True, related_name="therapists", to="causes.Cause"
            ),
        ),
    ]
