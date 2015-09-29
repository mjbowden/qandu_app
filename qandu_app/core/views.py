from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.core.urlresolvers import reverse_lazy
from .models import *
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView
# Create your views here.
class Home(TemplateView):
    template_name = "home.html"
class QuestionCreateView(CreateView):
  model = Question
  template_name = "question/question_form.html"
  fields = ['title', 'description']
  success_url = reverse_lazy('question_list')
  
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super(QuestionCreateView, self).form_valid(form)
class QuestionListView(ListView):
    model = Question
    template_name = 'question/question_list.html'
class QuestionDetailView(DetailView):
    model = Question
    template_name = 'question/question_detail.html'
class QuestionUpdateView(UpdateView):
      model = Question
      template_name = 'quextion/question_form.html'
      fields = ['title', 'description']