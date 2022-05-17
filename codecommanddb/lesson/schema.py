
import strawberry
from strawberry_django import mutations
from typing import List
from .types import Lesson, Submission, SubmissionInput
from . import models

@strawberry.type
class Query:
    lessons: List[Lesson] = strawberry.django.field()
    submissions: List[Submission] = strawberry.django.field()

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_submission(self, submission_input: SubmissionInput) -> Submission:
        print(f'Submitting your responses!')
        token = models.Token.objects.get(uuid=submission_input.token)
        question = models.Question.objects.get(uuid = submission_input.question)
        answers = models.Answer.objects.filter(uuid__in=submission_input.answers)

        submission, created = models.Submission.objects.update_or_create(
            token=str,
            question=str,
            defaults={"token":"", "question":""},
            ).set(answers)
        return submission, created

schema = strawberry.Schema(query=Query, mutation=Mutation)
