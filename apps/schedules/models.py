import uuid
from datetime import datetime
from django.db import models
from typing import Optional, Union
from apps.users.models import User

from uuid import UUID


class Event(models.Model):
    id: Union[str, UUID] = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    created_at: datetime = models.DateTimeField(auto_now_add=True)
    updated_at: datetime = models.DateTimeField(auto_now=True)

    added_by: Optional[User] = models.ForeignKey(
        User, models.SET_NULL, related_name="added_events", null=True
    )

    name = models.TextField(default="")
    due_date = models.DateTimeField()
    description = models.TextField(default="")
    location = models.TextField(default="")
    link = models.TextField(default="")

    def add_to_gcal(self):
        # Create function that decodes JWT, invites via GCal.
        pass
