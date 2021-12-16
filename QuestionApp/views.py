from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.utils import timezone

from .models import Question, Comment

# Create your views here.
class HomepageView(ListView):
    model = Question
    template_name = 'QuestionApp/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_list'] = Comment.objects.all()
        return context

class QuestionView(DetailView):
    model = Question
    template_name = 'QuestionApp/detail.html'

class CommentAddView(CreateView):
    model = Comment
    template_name = 'QuestionApp/comment_add.html'
    fields = ['comment_title', 'comment_content']

    def form_valid(self, form):
        form.instance.user_name = 'test_user'
        form.instance.comment_date = timezone.now()
        return super().form_valid(form)

class CommentDetailView(DetailView):
    model = Comment
    template_name = 'QuestionApp/comment_detail.html'

class CommentUpdateView(UpdateView):
    model = Comment
    template_name = 'QuestionApp/comment_add.html'
    fields = ['comment_title', 'comment_content']

class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'QuestionApp/comment_del.html'
    def get_success_url(self):
        return reverse_lazy('home')

'''
def homepage_view(request):
    q_list = Question.objects.all()
    context = {'question_list':q_list}
    return render(request,'QuestionApp/home.html', context)
    '''
'''
def homepage_view(request):
    q_list = Question.objects.all()
    if q_list:
        content = '<br>'.join(['<li>'+q.question_text+'</li>' for q in q_list])
    else:
        content = r'There is no question yet.'
    html = r'<!DOCTYPE html> <html><head><title>'+\
        r'my investigation Questionnaire'+\
        r'</title></head><body>'+\
        r'<h1>my investigation Questionnaire</h1>'+\
        r'<ol>'+content+r'<ol>'+\
        r'</body></html>'
    return HttpResponse(html)
    '''