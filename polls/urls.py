from django.urls import path

from . import views

urlpatterns = [
    path('gk/', views.index, name='gk'),
    path('chinmay/', views.indexchinmay, name='chinmay'),
    path('gaurav/', views.gaurav, name='gaurav'),
]
