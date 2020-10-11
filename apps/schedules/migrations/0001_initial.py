# Generated by Django 3.1.2 on 2020-10-11 08:18

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [("users", "0002_user_updated_at")]

    operations = [
        migrations.CreateModel(
            name="Event",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.TextField(default="")),
                ("due_date", models.DateTimeField()),
                ("description", models.TextField(default="")),
                ("location", models.TextField(default="")),
                ("link", models.TextField(default="")),
                (
                    "added_by",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="added_events",
                        to="users.user",
                    ),
                ),
            ],
        )
    ]
