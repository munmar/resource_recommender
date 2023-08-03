from django.urls import path
from . import views

# URLConf
urlpatterns = [
  # path('', views.recommend_courses),
  path('recommendation/', views.recommendation_view)
]