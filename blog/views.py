from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.decorators import login_required
from plotly.offline import plot
from plotly.graph_objs import Scatter
import plotly.express as px


@login_required
def home(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'Home'
    }
    return render(request, 'blog/home.html',context)


class PostListView(ListView):
    model = Post
    fields = '__all__'
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post
    fields = '__all__'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = Post
    success_url = "/blog"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


@login_required
def about(request):
    return render(request, 'blog/about.html',{'title':'About'})

@login_required
def graph(request):
    x_data = [0, 1, 2, 3]
    y_data = [x ** 2 for x in x_data]
    z_data = [x ** 1.5 for x in x_data]

    trace1 = Scatter(x=x_data, y=y_data, mode='lines', name='Ideal Glucose Level', opacity=0.8, line=dict(color='green'))
    trace2 = Scatter(x=x_data, y=z_data, mode='lines', name='Your Glucose Level', line=dict(color='blue'))
    layout = dict(
        title='Glucose Level Chart',
        xaxis=dict(title='Day'),
        yaxis=dict(title='Glucose Levels'),
        title_x = 0.5
    )
    fig = dict(data=[trace1, trace2], layout=layout)
    plot_div = plot(fig, output_type='div')
    return render(request, "blog/graph.html", context={'plot_div': plot_div})
