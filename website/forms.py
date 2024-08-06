from django import forms
from .models import Message

class MessageForm (forms.ModelForm):
    class Meta:
        model = Message
        fields = "__all__"
        labels = {
            "name" : "Your Name",
            "email" : "E-mail address",
            "message" : "Message"
        }