from rest_framework import routers
from django.urls import include, path

from note_app.views import NoteViewSet

router = routers.DefaultRouter()
router.register("notes", NoteViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "note_app"
