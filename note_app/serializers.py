from rest_framework import serializers

from note_app.models import Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ("id", "title", "content", "created_at", "updated_at", "user")


class NoteCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["title", "content"]
