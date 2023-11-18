from rest_framework import viewsets

from note_app.models import Note
from note_app.serializers import NoteSerializer


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    model = Note

