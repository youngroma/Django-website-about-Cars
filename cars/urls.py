from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', CarHome.as_view(), name='home'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', CarCategory.as_view(), name='category'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('contact/', ContactFormView.as_view(), name='contact'),    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),

    # path('cats/<slug:cat>/', categories),
    # re_path(r'^archive/(?P<year>[0-9]{4})/', archive),
]