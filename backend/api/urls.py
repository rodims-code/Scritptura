from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views


urlpatterns = [
    path('cursus/', views.CursusViewSet.as_view, name='cursus'),
    path('livrets/', views.LivretViewSet.as_view, name='livrets'),
    path('lecons/', views.LeconViewSet.as_view, name='lecons'),
    path('questions/', views.QuestionViewSet.as_view, name='questions'),
    path('answers/', views.UserAnswerViewSet.as_view, name='answers'),
    path('progressions', views.UserProfileView.as_view, name='progression')
  
]