from django.db import models
from django.core.mail import send_mail


class SendEmailInfo(models.Model):
    subject = models.CharField(max_length=150)
    sender = models.CharField(max_length=100)
    fail_silently = models.BooleanField(default=False)
    created_on = models.DateField(auto_now_add=True)
    modified_on = models.DateField(auto_now=True)

    def __str__(self):
        return self.sender


def send_response_email(message, recipients):
    email_info = SendEmailInfo.objects.all()[:1].get()
    send_mail(
        email_info.subject,
        message,
        email_info.sender,
        recipients,
        fail_silently=email_info.fail_silently,
    )
