from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'), # regex r'^$' means empty (or base url)
    url(r'^browse$', views.browse_page, name='browse_page'),
]