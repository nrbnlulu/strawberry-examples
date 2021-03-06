# Generated by Django 3.1.7 on 2021-02-28 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Hero",
            fields=[
                (
                    "id",
                    models.CharField(max_length=100, primary_key=True, serialize=False),
                ),
                ("color", models.CharField(max_length=100)),
                ("name", models.CharField(max_length=100, null=True)),
                ("updatedAt", models.FloatField(max_length=100, null=True)),
                ("deleted", models.BooleanField(default=True)),
            ],
        ),
    ]