from django.db import models

# Create your models here.

class LogMessage(models.Model):
    message = models.CharField(max_length=300)
    log_date = models.DateTimeField("date logged")

    def __str__(self):
        """Returns a string representation of a message."""
        return f"'{self.message}' logged on {self.log_date.strftime('%A, %d %B, %Y at %X')}"
