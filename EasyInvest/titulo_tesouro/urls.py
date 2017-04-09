from django.conf.urls import url
from titulo_tesouro import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^titulo_tesouro/$', views.titulo_tesouro_list),
    url(r'^titulo_tesouro/(?P<pk>[0-9]+)/$', views.titulo_tesouro_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)