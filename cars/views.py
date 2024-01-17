from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *
from .forms import *
from .utils import *
# Create your views here.



class CarHome(DataMixin, ListView):
    model = Car
    template_name = 'index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Home")
        return {**context, **c_def}

    def get_queryset(self):
        return Car.objects.filter(is_published=True).select_related('cat')


# def index(request):
#     posts = Car.objects.all()
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': 'Главная страница',
#         'cats_selected': 0,
#
#     }
#     return render(request, "index.html", context=context)


class ContactFormView(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'contact.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Feedback")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')
def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>нема такой бибики</h1>')

class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'addpage.html'
    login_url = reverse_lazy('home')
    success_url = reverse_lazy('home')  #ПЕРЕНАПРАВЛЕНИЕ ПОСЛЕ ДОБАВЛЕНИЯ СТАТЬИ

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Add Article")
        return {**context, **c_def}

# def addpage(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             try:
#                 Car.objects.create(**form.cleaned_data)
#                 return redirect('home')
#             except:
#                 form.add_error(None, 'Ошибка добавления поста')
#
#     else:
#         form = AddPostForm()
#     return render(request, "addpage.html", {'form': form, 'menu': menu, 'title': 'Add article'})


#
# def login(request):
#     return HttpResponse("Авторизация")

class ShowPost(DataMixin, DetailView):
    model = Car
    template_name = 'post.html'
    slug_url_kwarg = 'post_slug'
    # pk_url_kwarg = 'pk'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return {**context, **c_def}
# def show_post(request, post_slug):
#     post = get_object_or_404(Car, slug=post_slug)
#
#     context = {
#         'post': post,
#         'menu': menu,
#         'title': post.title,
#         'cat_selected': post.cat_id,
#     }
#
#     return render(request, 'post.html', context=context)

class CarCategory(DataMixin, ListView):
    model = Car
    template_name = 'index.html'
    context_object_name = 'posts'
    allow_empty = False


    def get_queryset(self):
        return Car.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Category - ' + str(context['posts'][0].cat),
                                      cat_selected=context['posts'][0].cat_id)
        return {**context, **c_def}



# def show_category(request, cat_id):
#     posts = Car.objects.filter(cat_id=cat_id)
#
#     if len(posts) == 0:
#         raise Http404()
#
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': 'Отображение по рубрикам',
#         'cats_selected': cat_id,
#     }
#
#     return render(request, 'index.html', context=context)

class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Register")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return redirect('login')