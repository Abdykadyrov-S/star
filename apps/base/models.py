from django.db import models

# Create your models here.

class Application(models.Model):
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    email = models.EmailField()
    cause = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return f"Заявка от {self.name}"
    
    class Meta :
        verbose_name = ""
        verbose_name_plural = "Заявки"