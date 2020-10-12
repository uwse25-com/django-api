import uuid
from datetime import datetime
from django.db import models
from typing import Optional, Union


from uuid import UUID

# Create your models here.
class User(models.Model):
    id: Union[str, UUID] = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    updated_at: datetime = models.DateTimeField(auto_now=True)
    wat_id = models.TextField(default="")
    email = models.TextField(default="")
    first_name = models.TextField(default="")
    last_name = models.TextField(default="")
    auth_id = models.TextField(default="")
