from django.urls import path

from . import views

urlpatterns = [
    path('gk/', views.index, name='gk'),
    path('chinmayy/', views.indexchinmay, name='chinmay'),
]