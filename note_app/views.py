from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from note_app.models import Note
from note_app.serializers import NoteSerializer, NoteCreateSerializer


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.action == "create":
            return NoteCreateSerializer
        return NoteSerializer
