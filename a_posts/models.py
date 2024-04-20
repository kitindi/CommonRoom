import uuid
from django.db import models

# Create your models here.


class Question(models.Model):
    title = models.CharField(max_length=300)
    image = models.ImageField(upload_to="uploads/", null=True, blank=True)
    problem_body = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    id =models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering =['-created']
        


class Answer(models.Model):
    content = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    question_id = models.ForeignKey(Question, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.content
    
    class Meta:
        ordering =['-created_at']