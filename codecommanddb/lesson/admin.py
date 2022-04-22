from django.contrib import admin
from .models import Lesson, Token, Content, Question, Submission, Answer

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ["created", "updated", "title", "uuid"]

@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = ["created", "uuid"]

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ["created", "updated", "media", "uuid", "lesson"]

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ["created", "updated", "text", "uuid", "content", "lesson", "type", "additional_info"]

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ["created", "updated", "uuid", "token", "question"]

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ["created", "updated", "text", "uuid", "is_correct", "question"]
# need to eventually add back in "submissions"