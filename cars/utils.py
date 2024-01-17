from django.db.models import Count

from .models import *

menu = [
        {'title': "Add Article", 'url_name': 'add_page'},
        {'title': "FeedBack", 'url_name': 'contact'},
]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.annotate(Count('car'))

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(0)

        context['menu'] = user_menu

        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context