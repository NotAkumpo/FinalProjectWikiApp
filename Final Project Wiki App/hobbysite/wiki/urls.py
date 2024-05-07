from django.urls import path
from .views import WikiListView, WikiDetailView, WikiCreateView, WikiUpdateView

urlpatterns = [
    path('articles/', WikiListView.as_view(), name = 'wiki-list'),
    path('article/<int:pk>/', WikiDetailView.as_view(), name = 'wiki-detail'),
    path('article/add/', WikiCreateView.as_view(), name = 'wiki-add'),
    path('article/<int:pk>/edit/', WikiUpdateView.as_view(), name = 'wiki-update'),
]
app_name = 'wiki'