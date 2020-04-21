from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from scrappers.views import EventList, EventUpdate

urlpatterns = [
    path(r'events', EventList.as_view()),
    path(r'update/<str:id>', EventUpdate.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)