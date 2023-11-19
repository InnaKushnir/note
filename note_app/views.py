from rest_framework import viewsets, status
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from note_app.models import Note
from note_app.serializers import NoteSerializer, NoteCreateSerializer


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        note = self.get_object()
        if note.user == self.request.user or self.request.user.is_staff:
            serializer.save()
        else:
            raise PermissionDenied("You are not allowed to update this note.")

    def perform_destroy(self, instance):
        if instance.user == self.request.user or self.request.user.is_staff:
            instance.delete()
        else:
            raise PermissionDenied("You are not allowed to delete this note.")

    def get_serializer_class(self):
        if self.action == "create":
            return NoteCreateSerializer
        return NoteSerializer
