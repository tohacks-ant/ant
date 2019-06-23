from django.db import models

# Create your models here.
class StuProfile(models.Model):
    last_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    school = models.CharField(max_length=50)
    student_id = models.IntegerField()
    skills = models.TextField()
    description = models.TextField()
    resume = models.FileField(upload_to='resume/%Y/%m/%d')
    photo = models.ImageField(upload_to='avatar/%Y/%m/%d')
    user = models.OneToOneField('users.Student', unique=True, on_delete=models.CASCADE)

    def get_full_name(self):
        return self.first_name + ' ' + self.first_name

    def __str__(self):
        return self.get_full_name()

class OrgProfile(models.Model):
    organization_name = models.CharField(max_length=50)
    organization_logo = models.ImageField(upload_to='logo/%Y/%m/%d')
    category_of_industry = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    description = models.TextField()
    logo = models.ImageField(upload_to='avatar/%Y/%m/%d',
                                 null=True, blank=True)
    user = models.OneToOneField('users.Organization', unique=True, on_delete=models.CASCADE)


class Profile_relationship(models.Model):
    profile_id = models.IntegerField()
    project_id = models.IntegerField()
    org_id = models.IntegerField()
    createdate = models.DateTimeField(auto_now_add=True)
