from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Article, ArticleCategory
from .forms import ArticleForm, CommentForm

# Create your views here.

class WikiListView(ListView):
    model = Article
    template_name = 'wiki_list.html'

    def get_queryset(self):
        queryset = Article.objects.all()
        if self.request.user.is_authenticated:
            queryset = queryset.filter(author=self.request.user.profile)
        return queryset

    def get_context_data(self, **kwargs):
        if self.request.user.is_authenticated:
            context = super().get_context_data(**kwargs)
            context['all_articles'] = Article.objects.exclude(author=self.request.user.profile)
        else:
            context = super().get_context_data(**kwargs)
        return context

class WikiDetailView(FormMixin, DetailView):
    model = Article
    template_name = 'wiki_detail.html'
    context_object_name = 'article'

    def get_success_url(self):
        return reverse_lazy('wiki:wiki-detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = self.get_object()
        context['other_articles'] = Article.objects.filter(author=article.author).exclude(pk=article.pk)[:2]
        context['all_comments'] = article.comments.all().order_by('-created_on')
        context['comment_form'] = CommentForm()
        context['can_edit'] = self.request.user == article.author.user
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        form.instance.article = self.get_object()
        form.save()
        return super().form_valid(form)


class WikiCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'wiki_create.html'
    fields = ['title', 'category', 'entry', 'header_image']
    success_url = reverse_lazy('wiki:article_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ArticleCategory.objects.all()
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class WikiUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    fields = ['title', 'category', 'entry', 'header_image']
    template_name = 'wiki_update.html'
    success_url = reverse_lazy('wiki:article_list')

    def get_form(self, form_class = None):
        form = super().get_form(form_class)
        form.fields['category'].queryset = ArticleCategory.objects.all()
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update'] = True
        return context

    def get_initial(self):
        initial = super().get_initial()
        initial['author'] = self.request.user
        return initial

    def form_valid(self, form):
        return super().form_valid(form)
