# Generated by Django 4.1.7 on 2023-02-22 23:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("portafolio", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=250)),
                ("email", models.EmailField(max_length=254)),
                ("asunto", models.CharField(max_length=100)),
                ("message", models.TextField(max_length=3000)),
            ],
        ),
        migrations.AlterField(
            model_name="project",
            name="image",
            field=models.ImageField(upload_to="portafolio/images/"),
        ),
    ]
