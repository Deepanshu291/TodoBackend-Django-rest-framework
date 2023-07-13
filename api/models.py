from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.

#Base Class for  some common attribute 
class BaseModal(models.Model):
    uuid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    created_at = models.DateField( auto_now=True,null=True,blank=True)
    updated_at = models.DateField( auto_now_add=True,null=True, blank=True)

    class Meta:
        abstract = True

class Todo(BaseModal): # here BaseCLass inherite to get Some attribute
    title = models.CharField( max_length=50)
    is_done = models.BooleanField(default=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='todo_user')