from django.urls import path
from .views import dates, HomeListView, PostDetailView, CategoryListView, AuthorListView, PostCreateView, \
    PostUpdateView, PostDeleteView, AboutPageView

urlpatterns = [

    # PAGINA DE INICIO
    path('', HomeListView.as_view(), name='home'),
    # DETALLE DEL POST
    path('post/<int:pk>', PostDetailView.as_view(), name='post'),
    # FILTRADO POR CATEGORIA
    path('category/', CategoryListView.as_view(), name='category'),
    # FILTRADO POR AUTHOR
    path('author/', AuthorListView.as_view(), name='author'),
    # CREAR POST
    path('create/', PostCreateView.as_view(), name='create'),
    #EDITAR POST
    path('update/<int:pk>', PostUpdateView.as_view(), name='update'),
    #ELIMINAR POST
    path('delete/<int:pk>', PostDeleteView.as_view(), name='delete'),
    #ABOUT-ACERCA DE NOSOTROS
    path('about/',AboutPageView.as_view(), name='about'),





    #PAGINA DE INICIO
    #path('', home, name='home'),

    #PAGINA FILTRADO DE CATEGORIAS
    #path('category/<int:category_id>', category, name='category'),

    #PAGINA FILTRADO DE AUTOR
    #path('author/<int:author_id>', author, name='author'),

    #PAGINA FILTRADO POR FECHA
    path('dates/<int:month_id>/<int:year_id>', dates, name='dates'),



    #path('post/<int:post_id>', post, name='post'),
]