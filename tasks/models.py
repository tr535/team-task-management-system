from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    ROLE_CHOICES = [('manager', 'מנהל'), ('employee', 'עובד')]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    team_name = models.CharField(max_length=100) # ניהול כמה צוותים ללא חפיפה [cite: 99]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} ({self.get_role_display()})"

class Task(models.Model):
    STATUS_CHOICES = [('new', 'חדש'), ('in_progress', 'בתהליך'), ('completed', 'הושלם')]
    title = models.CharField(max_length=200) # שם המשימה [cite: 87]
    description = models.TextField() # תיאור המשימה [cite: 88]
    deadline = models.DateField() # תאריך יעד לסיום [cite: 89]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new') # סטטוס ראשוני "חדש" [cite: 90]
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True) # מבצע המשימה [cite: 91]
    team_name = models.CharField(max_length=100) # הפרדה בין צוותים [cite: 99]

    def __str__(self):
        return self.title