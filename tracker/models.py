from django.db import models
from django.contrib.auth.models import User

class Application(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    
    STATUS_CHOICES = [
        ('Applied', 'Applied'),
        ('Screening', 'Screening'),
        ('Interview', 'Interview'),
        ('Offer', 'Offer'),
        ('Rejected', 'Rejected'),
    ]

    SOURCE_CHOICES = [
        ('LinkedIn', 'LinkedIn'),
        ('Rozee', 'Rozee'),
        ('Indeed', 'Indeed'),
        ('Referral', 'Referral'),
        ('Company Website', 'Company Website'),
    ]

    company = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    location = models.CharField(max_length=200, blank=True)

    salary = models.CharField(
        max_length=100,
        blank=True
    )

    source = models.CharField(
        max_length=50,
        choices=SOURCE_CHOICES
    )

    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='Applied'
    )

    applied_date = models.DateField()

    notes = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.company} - {self.position}"
    
class Profile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    target_applications = models.IntegerField(
        default=100
    )

    def __str__(self):
        return self.user.username