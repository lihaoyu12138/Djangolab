from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'course'
urlpatterns = [
  path('', views.IndexView.as_view(), name='index'),
  path('<int:pk>/detail/', views.DetailView.as_view(), name='detail'),
  path('<int:pk>/class/', views.ClassView.as_view(), name='class'),
  path('<int:pk>/classdetail', views.ClassdetailView.as_view(), name='classdetail'),
]
