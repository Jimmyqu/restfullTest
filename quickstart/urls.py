from django.conf.urls import url
from quickstart import views
from quickstart import view_base
from .views import AllList,UsersApi
from .models import Artical,NewsCategory

urlpatterns = [
   # url(r'test$', views.upload_image),
    url(r'list/$', AllList.as_view()),
    url(r'users/$', UsersApi.as_view()),
    # url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
]

