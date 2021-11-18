from django.urls import path

from .views import HomepageView, QuestionView

urlpatterns = [
    path('question/<int:pk>/', QuestionView.as_view(), name='question_detail'),
    path('', HomepageView.as_view(), name='home'),
]