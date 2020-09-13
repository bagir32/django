from django import forms
from .models import User_Profile
# from multiupload.fields import MultiFileField

#DataFlair #File_Upload
class Profile_Form(forms.ModelForm):
    class Meta:
        model = User_Profile
        fields = [
        'fname',
        'lname',
        'technologies',
        'email',
        'display_picture',
        #  'new_picture',
        ]