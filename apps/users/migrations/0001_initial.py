# Generated by Django 3.1.2 on 2020-10-11 08:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("wat_id", models.TextField(default="")),
                ("email", models.TextField(default="")),
                ("first_name", models.TextField(default="")),
                ("last_name", models.TextField(default="")),
                ("auth_id", models.TextField(default="")),
            ],
        )
    ]
