from django import forms
from django.shortcuts import redirect, render
from .forms import QuestionCreateForm
from a_posts.models import Question

# Create your views here.

def home_view(request):
    all_questions =Question.objects.all()
    context = {'questions': all_questions}
    return render(request, 'posts/home.html', context)



def question_create_view(request):
    form = QuestionCreateForm()

    if request.method == 'POST':
        form = QuestionCreateForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect('home-page')
    
    return render(request, 'posts/post_question.html', {'form': form})
        

def question_edit_view(request,pk):
    question = Question.objects.get(id=pk)
    form = QuestionCreateForm(instance=question)

    if request.method == 'POST':
        form = QuestionCreateForm(request.POST, request.FILES, instance=question)
        
        if form.is_valid():
            form.save()
            return redirect('home-page')
    
    return render(request, 'posts/edit_question.html', {'form': form})



def delete_question_view(request,pk):
    
    question = Question.objects.get(id=pk)
    
    if request.method == 'POST':
        question.delete()
        return redirect('home-page')
    else:
        
        return render(request,'question/confirm_delete.html',{'question':question})
        
        