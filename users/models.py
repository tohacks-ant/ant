from django.db import models
from django.contrib.auth.hashers import make_password, check_password


class Organization(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=128)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        self.password = set_password(self.password)
        super(Organization, self).save(*args, **kwargs)


class Student(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=128,)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        self.password = set_password(self.password)
        super(Student, self).save(*args, **kwargs)


def set_password(password):
    password_hash = make_password(password)
    return password_hash


def check_password_hash(password, password_hash):
    return check_password(password, password_hash)
