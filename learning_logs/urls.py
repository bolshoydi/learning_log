"""определяет схемы URL для learning_logs. """
from django.conf.urls import url
from . import views

urlpatterns = [
    # домащняя страница
    url(r'^$', views.index, name='index'),
    # вывод всех тем
    url(r'^topics/$', views.topics, name='topics'),
    # подробная информация о топике
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    # форма для добавления новой темы
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
    # форма для добавления новой записи в теме
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    # форма для редактирования записей
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
    ]
