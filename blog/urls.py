from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView,PostUpdateView,PostDeleteView, home
urlpatterns = [
    path('', PostListView.as_view(),name='blog-home'),
    path('post/<int:pk>/', home,name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(),name='post-delete'),
    path('post/new/', PostCreateView.as_view(),name='post-create'),
    path('glucosegraph/', views.graph, name='glucose-graph'),
    path('about/', views.about, name='blog-about')
]