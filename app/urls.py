from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^about/$', views.about, name='index'),
    # url(r'^deeper/$', views.deeper, name='deeper'),
    url(r'^building_detail/(?P<building_url>\w+)/', views.building_detail, name='building_detail'),
    url(r'^bathroom_detail/(?P<bathroom_url>\w+)/', views.bathroom_detail, name='bathroom_detail'),
    url(r'^get_comments/(?P<bathroom_url>\w+)/', views.get_comments, name='get_comments'),
    url(r'^add_comment/$', views.add_comment, name='add_comment')
]