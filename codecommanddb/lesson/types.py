
import strawberry
from strawberry.django import auto
from . import models
from typing import List, Optional

@strawberry.django.type(models.Answer)
class Answer:
    text: str
    uuid: auto
    is_correct: bool
    question: 'Question'
    

@strawberry.django.type(models.Question)
class Question:
    text: str
    uuid: auto
    content: str
    lesson: 'Lesson'
    type: str
    additional_info: str
    answers: List[Answer]
    submission: Optional['Submission']

@strawberry.django.type(models.Content)
class Content:
    media: str
    uuid: auto
    lesson: 'Lesson'

@strawberry.django.type(models.Lesson)
class Lesson:
    title: str
    description: str
    uuid: auto
    contents: List[Content]
    questions: List[Question]

@strawberry.django.type(models.Token)
class Token:
    uuid: auto
    submissions: List['Submission']

@strawberry.django.type(models.Submission)
class Submission:
    uuid: auto
    token: 'Token'
    question: 'Question'
    answers: List[Answer]

@strawberry.input
class SubmissionInput:
    token: str
    question: str
    answers: List[str]



  

