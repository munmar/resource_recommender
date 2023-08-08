from django.urls import path
from . import views

# URLConf
urlpatterns = [
  path('', views.index, name='app-index'),
  path('recommendation/', views.recommendation_view, name='app-recommendations')
]