from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PostForm
from .models import Post, Category
from django.contrib.auth.models import User
from django.views.generic.base import TemplateView

# PAGINA DE INICIO
class HomeListView(ListView):
    model = Post
    paginate_by = 3
    template_name = 'core/home.html'

    def get_queryset(self):
        return Post.objects.filter(published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context

# DETALLE DEL POST
class PostDetailView(DetailView):
    model = Post
    template_name = 'core/detail.html'

#FILTRADO POR CATEGORIA
class CategoryListView(ListView):
    model = Category
    template_name = 'core/category.html'

    def get_queryset(self):
        category_id = self.request.GET['cat']

        if category_id:
            return Post.objects.filter(category=category_id, published=True)

        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['category'] = Category.objects.get(id=self.request.GET['cat'])
        return context

# FILTRADO POR AUTOR
class AuthorListView(ListView):
    model = User
    template_name = 'core/author.html'

    def get_queryset(self):
        author_id = self.request.GET['aut']

        if author_id:
            return Post.objects.filter(author=author_id, published=True)

        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super(AuthorListView, self).get_context_data(**kwargs)
        context['author'] = User.objects.get(id=self.request.GET['aut'])
        return context


# Create your views here.
# def home(request):
#     posts_page = Paginator(Post.objects.filter(published=True), 2)
#     page = request.GET.get('page')
#     posts = posts_page.get_page(page)
#     aux = 'x' * posts.paginator.num_pages
#
#     print(type(posts.paginator.num_pages))
#     return render(request,'core/home.html', {'posts':posts, 'aux':aux})

# Detalle del Post
# def post(request, post_id):
#     # post = Post.objects.get(id=post_id)
#     try:
#         post = get_object_or_404(Post, id=post_id)
#         return render(request, 'core/detail.html', {'post':post})
#     except:
#         return render(request, 'core/404.html')

# Filtrado por Categoría
# def category(request, category_id):
#     try:
#         category = get_object_or_404(Category, id=category_id)
#         return render(request, 'core/category.html', {'category':category})
#     except:
#         return render(request, 'core/404.html')

# # Filtrado por Author
# def author(request, author_id):
#     try:
#         author = get_object_or_404(User, id=author_id)
#         return render(request, 'core/author.html', {'author':author})
#     except:
#         return render(request, 'core/404.html')

def dates(request, month_id, year_id):

    meses = {
        1: 'Enero',
        2: 'Febrero',
        3: 'Marzo',
        4: 'Abril',
        5: 'Mayo',
        6: 'Junio',
        7: 'Julio',
        8: 'Agosto',
        9: 'Septiembre',
        10: 'Octubre',
        11: 'Noviembre',
        12: 'Diciembre',
    }

    if month_id > 12 or month_id < 1:
        return render(request, 'core/404.html')

    posts = Post.objects.filter(published=True, created__month=month_id, created__year=year_id)
    return render(request, 'core/dates.html', {'posts':posts, 'month':meses[month_id], 'year':year_id})

#CREAR POST
class PostCreateView(CreateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('home')

#EDICION DEL POST
class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name_suffix = '_update_form'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('update', args=[self.object.id]) + '?ok'


#ELIMINAR POST
class PostDeleteView(DeleteView):
    model = Post
    success_url= reverse_lazy('home')

class AboutPageView(TemplateView):
    template_name = 'core/about.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
