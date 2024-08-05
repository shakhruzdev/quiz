from django.urls import path
from .views import GetAllSubjectsViewSet, QuizAllSubjectsViewSet, QuizViewSet

urlpatterns = [
    path('subjects/', GetAllSubjectsViewSet.as_view({'get': 'get_all'})),
    path('quiz/', QuizAllSubjectsViewSet.as_view({'get': 'get_all'})),
    path('quiz/start/<int:pk>/', QuizViewSet.as_view({'post': 'start'})),
    path('quiz/next/<int:answer_sheet_id>/', QuizViewSet.as_view({'get': 'next_question'})),
    path('quiz/answer/<int:answer_sheet_id>/', QuizViewSet.as_view({'post': 'answer_the_question'}))
]