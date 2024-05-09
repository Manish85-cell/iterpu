from django.urls import path
from . import views

urlpatterns =[
    path('', views.index , name="index"),
    path('intro', views.intro, name="intro"),
    path("blog", views.blog, name="blog"),
    path("cv", views.cv, name="cv"),
    path("contact", views.contact, name="contact")
]