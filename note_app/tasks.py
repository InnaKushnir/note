import random
import string

from celery import shared_task
from note_app.models import GeneratedTitle


@shared_task
def generate_random_title(length: int = 10) -> None:
    letters = string.ascii_letters
    title = "".join(random.choice(letters) for i in range(length))

    new_title = GeneratedTitle.objects.create(title=title)
    new_title.save()
