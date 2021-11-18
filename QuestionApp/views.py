from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from .models import Question

# Create your views here.
class HomepageView(ListView):
    model = Question
    template_name = 'QuestionApp/home.html'

class QuestionView(DetailView):
    model = Question
    template_name = 'QuestionApp/detail.html'

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