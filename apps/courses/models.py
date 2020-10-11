from django.db import models
import uuid
from typing import Optional, Union

from uuid import UUID


class Course(models.Model):
    id: Union[str, UUID] = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    name = models.TextField(default="")
