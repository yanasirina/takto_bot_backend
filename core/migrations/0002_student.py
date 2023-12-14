# Generated by Django 4.2 on 2023-12-14 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Student",
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
                (
                    "telegram_id",
                    models.BigIntegerField(unique=True, verbose_name="User_id"),
                ),
                (
                    "username",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="User_name"
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="Имя")),
                (
                    "phone_number",
                    models.CharField(max_length=255, verbose_name="Номер телефона"),
                ),
            ],
            options={
                "verbose_name": "Студент",
                "verbose_name_plural": "Студенты",
            },
        ),
    ]
