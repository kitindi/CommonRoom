from django import forms
from a_posts.models import Question, Answer



class QuestionCreateForm(forms.ModelForm):
    class Meta:
        model = Question
        fields ="__all__"
        
        widgets = {
            'problem_body': forms.Textarea(attrs={'rows':5,'Palceholder':'What is in your mind?','class':'px-2 py-2.5 border border-gray-400 rounded-md focus:outline-none'}),
            'title': forms.TextInput(attrs={'Placeholder':'e.g what is the vector scale?','class':'border border-gray-400 rounded-md px-2 py-2.5 focus:outline-none'}),
            'image': forms.FileInput(attrs={'class':' border-none rounded-md px-2 py-2.5 focus:outline-none'}),
        }


class AnswerForm(forms.ModelForm):
    reply_question = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = Answer
        fields = "__all__"
        
        widgets = {
            'content': forms.Textarea(attrs={'rows':3,'Palceholder':'What is in your mind?','class':'w-full px-2.5 py-2.5 text-[12px] test-slate-600 focus:outline-none'}),
            }
