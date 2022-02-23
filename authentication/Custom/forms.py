from django.contrib.auth.forms import UserCreationForm
from .models import profiles

class Uregistration(UserCreationForm):
    class Meta:
        model = profiles
        fields= '__all__'
       