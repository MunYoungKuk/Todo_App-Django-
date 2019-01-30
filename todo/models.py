from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
    due_date =models.DateField()
    
    def __str__(self):
        return self.title
        
class Comment(models.Model):
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    content = models.CharField(max_length=50)
    
    def __str__(self):
        return self.content
