from django import forms
from django.shortcuts import redirect, render
from .forms import QuestionCreateForm, AnswerForm
from a_posts.models import Question, Answer
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST
# Create your views here.

def home_view(request):
    answer_form = AnswerForm()
    all_questions =Question.objects.all()
    
    if request.method == 'POST':
        
        if ' reply_question' in request.POST:
            form = AnswerForm(request.POST)
            if form.is_valid():
                reply =form.save(commit=False)
                reply.user = request.user
                reply.save()
                return redirect('home-page')
            
    context = {'questions': all_questions, 'answer_form': answer_form}
    return render(request, 'posts/home.html', context)



def question_create_view(request):
    form = QuestionCreateForm()
    

    if request.method == 'POST':
        print(request.method)
        
        form = QuestionCreateForm(request.POST, request.FILES)
        
        if form.is_valid():
            qn = form.save(commit=False)
            qn.user = request.user
            form.save()
            
            return redirect('home-page')
    
    return render(request, 'posts/post_question.html', {'form': form})
        

def question_edit_view(request,pk):
    question = Question.objects.get(id=pk)
    form = QuestionCreateForm(instance=question)

    if request.method == 'POST':
        form = QuestionCreateForm(request.POST, request.FILES, instance=question)
        
        if form.is_valid():
            qn =form.save(commit=False)
            qn.user = request.user
            qn.save()
            return redirect('home-page')
    
    return render(request, 'posts/edit_question.html', {'form': form})



def delete_question_view(request,pk):
    question = Question.objects.get(id=pk)
    if request.user.id == question.user.id:
    # delete
         question.delete()
            
    return redirect('home-page')
        

# create comment system for the given question
@require_POST
def reply_question_view(request, question_id):
    # get question
    question = Question.objects.get(id=question_id)
    
    # answer form 
    
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if 'reply_question' in request.POST:
            print(request.user.username)
        else:
            print("doesnt exist")
    
    return redirect('home-page') 
    
        
        