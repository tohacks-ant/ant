from django import forms
from .models import OrgProfile, StuProfile

class StuProfileForm(forms.ModelForm):
    class Meta:
        model = StuProfile
        fields = ['last_name', 'first_name', 'school', 'student_id', 'skills',
                  'description', 'resume', 'photo']

class OrgProfileForm(forms.ModelForm):
    class Meta:
        model = OrgProfile
        fields = ['organization_name', 'organization_logo',
                  'category_of_industry', 'location', 'description', 'logo']
