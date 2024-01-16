from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, graph, chat_view
urlpatterns = [
    path('', chat_view,name='blog-home'),
    path('graph/', graph, name='graph'),
    path('about/', views.about, name='blog-about')
]