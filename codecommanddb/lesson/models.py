from django.db import models
import uuid
from django.utils.translation import gettext_lazy as _

class Lesson(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=256, unique=True)
    description = models.TextField()
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)

    def __str__(self):
        return self.title

class Token(models.Model):
    '''
    assigns random token for user
    may be used for user to restore their submissions
    needs to be stored in local storage
    '''
    created = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    
class Content(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    media = models.FileField(editable=True,)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE,related_name='contents')

class Question(models.Model):
    class Type(models.TextChoices):
        SINGLE = 'SIN', _('Single Choice')
        MULTI = 'MUL', _('Multiple Choice')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    text = models.TextField()
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    content = models.ForeignKey(Content, null=True, blank=True, on_delete=models.CASCADE, related_name='contents')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='questions')
    type = models.CharField(max_length=32, choices=Type.choices)
    additional_info = models.TextField(null=True, blank=True)

# this model for user response(s) to question
class Submission(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    token = models.ForeignKey(Token, on_delete=models.CASCADE, related_name='tokens')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='questions')

    class Meta:
        unique_together = ['token', 'question']



# this model for correct answers
class Answer(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    text = models.TextField()
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    submissions = models.ManyToManyField(Submission, blank=True, related_name='submissions')




# the model for submission/answer will be many-to-many
# and will be created automatically by db.sqlite3b


  