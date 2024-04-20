from django import forms
from a_posts.models import Question



class QuestionCreateForm(forms.ModelForm):
    class Meta:
        model = Question
        fields ="__all__"
        
        widgets = {
            'problem_body': forms.Textarea(attrs={'rows':5,'Palceholder':'What is in your mind?','class':'px-2 py-2.5 border border-gray-400 rounded-md focus:outline-none'}),
            'title': forms.TextInput(attrs={'Placeholder':'e.g what is the vector scale?','class':'border border-gray-400 rounded-md px-2 py-2.5 focus:outline-none'}),
            'image': forms.FileInput(attrs={'class':' border-none rounded-md px-2 py-2.5 focus:outline-none'}),
        }


class AnswersForm(forms.ModelForm):
    pass 