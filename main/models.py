from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    text = models.TextField()
    expires_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'

    def __str__(self):
        return self.text





