import strawberry

from typing import List
from .types import Lesson

@strawberry.type
class Query:
    lessons: List[Lesson] = strawberry.django.field()

schema = strawberry.Schema(query=Query)

