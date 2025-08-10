from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    github_username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=100)
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.github_username


class UserProfile(models.Model):
    ROLE_CHOICES = [
        ("student", "Student"),
        ("instructor", "Instructor"),
        ("staff", "Staff"),
        ("customer", "Customer"),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} ({self.role})"


class Course(models.Model):
    COURSE_TYPES = [
        ("self-paced", "Self-paced"),
        ("instructor-led", "Instructor-led"),
    ]
    VENDOR_CHOICES = [
        ("IBM", "IBM"),
        ("MICROSOFT", "Microsoft"),
        ("COMPTIA", "CompTIA"),
        ("GOOGLE", "Google"),
        ("AWS", "AWS"),
        ("GITHUB", "GitHub"),
        ("ORACLE", "Oracle"),
        ("HPE", "HPE"),
        ("DELL_EMC", "Dell/EMC"),
        ("EC_COUNCIL", "EC-Council"),
        ("PCEB", "PCEB"),
        ("SAFE", "SAFe"),
        ("BROADCOM", "Broadcom"),
        ("CISCO", "CISCO"),
        ("PALO_ALTO", "Palo Alto"),
        ("FORTINET", "Fortinet"),
        ("HUAWEI", "Huawei"),
        ("CODING", "Coding"),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    vendor = models.CharField(max_length=20, choices=VENDOR_CHOICES)
    course_type = models.CharField(max_length=20, choices=COURSE_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
