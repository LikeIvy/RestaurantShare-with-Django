# Generated by Django 4.1.7 on 2023-05-04 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("shareRes", "0003_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Restaurant",
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
                ("restaurant_name", models.CharField(max_length=100)),
                ("restaurant_link", models.CharField(max_length=500)),
                ("restaurant_content", models.TextField()),
                ("restaurant_keyword", models.CharField(max_length=50)),
                (
                    "category",
                    models.ForeignKey(
                        default=3,
                        on_delete=django.db.models.deletion.SET_DEFAULT,
                        to="shareRes.category",
                    ),
                ),
            ],
        ),
    ]
