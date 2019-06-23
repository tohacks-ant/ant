from django.db import models

# Create your models here.

class Project(models.Model):
    project_name = models.CharField(max_length=50)
    posted_by = models.ForeignKey('users.Organization', on_delete=models.CASCADE)
    posted_time = models.DateField(auto_now_add=True)
    description = models.TextField()
    project_details = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    skills_required = models.TextField()

    def __str__(self):
        return self.project_name
