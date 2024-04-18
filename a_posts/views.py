from django import forms
from django.shortcuts import redirect, render

from a_posts.models import Question

# Create your views here.

def home_view(request):
    all_questions =Question.objects.all()
    context = {'questions': all_questions}
    return render(request, 'posts/home.html', context)


class QuestionCreateForm(forms.ModelForm):
    class Meta:
        model = Question
        fields ="__all__"
        
        widgets = {
            'problem_body': forms.Textarea(attrs={'rows':5,'Palceholder':'What is in your mind?','class':'px-2 py-2.5 border border-gray-400 rounded-md focus:outline-none'}),
            'title': forms.TextInput(attrs={'Placeholder':'e.g what is the vector scale?','class':'border border-gray-400 rounded-md px-2 py-2.5 focus:outline-none'}),
            'image': forms.FileInput(attrs={'class':' border-none rounded-md px-2 py-2.5 focus:outline-none'}),
        }

def question_create_view(request):
    form = QuestionCreateForm()

    if request.method == 'POST':
        form = QuestionCreateForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect('home-page')
    
    return render(request, 'posts/post_create.html', {'form': form})
        