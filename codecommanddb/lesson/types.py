from email import contentmanager
from importlib.resources import path
from random import choices
from django.forms import MultipleChoiceField
import strawberry
from strawberry.django import auto
from . import models
from typing import Dict, List

@strawberry.django.type(models.Answer)
class Answer:
    text: str
    uuid: auto
    is_correct: bool
    question: 'Question'
    # TODO: submissions: choices next line ... now with bool instead of choices no error thrown ... better option than bool
    submissions: bool

@strawberry.django.type(models.Question)
class Question:
    # TODO: add subclass for Type (sin; mul)
    text: str
    uuid: auto
    # TODO: better option that str for next line content 
    content: str
    lesson: 'Lesson'
    # TODO: next code line throws erro
    # type: MultipleChoiceField
    additional_info: str
    # TODO: graphql ui errors re: answers of Answer must have multiple selections ...
    answers: List[Answer]

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
    # TODO: better option than list for next line
    questions: List[Question]

@strawberry.django.type(models.Token)
class Token:
    uuid: auto
    tokens: auto
    submissions: bool

@strawberry.django.type(models.Submission)
class Submission:
    uuid: auto
    token: 'Token'
    question: 'Question'

