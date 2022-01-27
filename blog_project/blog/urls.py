from django.urls import path
# from blog import views as blog_views
from . import views


urlpatterns = [
    path('about_us/', views.about, name='blog-about' ),
    path('', views.home, name='blog-home' )
]
