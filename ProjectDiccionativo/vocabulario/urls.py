# vocabulario/urls.py

from django.urls import path
from .views import (
    WordListView,
    WordDetailView,
    WordCreateView,
    WordUpdateView,
    WordDeleteView,
)

urlpatterns = [
    path("", WordListView.as_view(), name="word_list"),
    path("word/<int:pk>/", WordDetailView.as_view(), name="word_detail"),
    path("word/new/", WordCreateView.as_view(), name="word_create"),
    path("word/<int:pk>/edit/", WordUpdateView.as_view(), name="word_update"),
    path("word/<int:pk>/delete/", WordDeleteView.as_view(), name="word_delete"),
]
