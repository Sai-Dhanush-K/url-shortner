from django.db import models
import uuid

STATUS_CHOICES=[
    ("ac","Active"),
    ("ia","Inactive"),
    ("ex","Expired"),
    ('de',"Deleted"),
]
class shortlink(models.Model):
    ID=models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    code= models.CharField(max_length=16)
    Actual_URL= models.URLField()
    clicks=models.IntegerField(default=0)
    status=models.CharField(choices=STATUS_CHOICES, default="ac")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    expires_at=models.DateTimeField(blank=True, null=True)
