from django.urls import path

from .views import HomepageView, QuestionView
from .views import CommentAddView, CommentDeleteView, CommentUpdateView, CommentDetailView
from .views import VotingStartView, VotingView, VotedView
#start_vote, voting, voted

urlpatterns = [
    path('voting/done', VotedView.as_view(), name='voted'),
    path('voting/<int:pk>/', VotingView.as_view(), name='voting'),
    path('voting/start/', VotingStartView.as_view(), name='start_vote'),
    path('comment/add/',CommentAddView.as_view(), name='comment_add'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(),name='comment_del'),
    path('comment/<int:pk>/edit/',CommentUpdateView.as_view(),name='comment_edit'),
    path('comment/<int:pk>/', CommentDetailView.as_view(), name='comment_detail'),
    path('question/<int:pk>/', QuestionView.as_view(), name='question_detail'),
    path('', HomepageView.as_view(), name='home'),
]